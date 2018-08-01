import socket
import multiprocessing

"""
多进程并发服务器
"""


class MyTcpServer(object):

    def __init__(self, address, num=5):
        self.server = socket.socket()
        self.server.bind(address)
        self.server.listen(num)

    def start(self):
        print("服务器已经成功启动")
        while True:
            conn, addr = self.server.accept()
            print('{}已经连接'.format(addr[0]))
            p = multiprocessing.Process(target=self._handler, args=(conn, addr))
            p.start()

    def _handler(self, conn, addr):
        while True:
            data = conn.recv(1024)
            if not data:
                conn.close()
                print('{}已经断开'.format(addr[0]))
                break
            else:
                print(data.decode('utf8'))
                conn.send(data)


def main():
    server = MyTcpServer(('127.0.0.1', 9999))
    server.start()


if __name__ == '__main__':
    main()
