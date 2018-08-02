import multiprocessing
import socket

"""
用面向对象的方式实现并发服务器

主进程管理客户端的连接
新建进程管理服务器和客户端的通信
"""


class CommunicationProcess(multiprocessing.Process):

    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                print('{}已经断开连接'.format(self.addr))
                self.conn.close()
                break
            print(data.decode('utf8'))
            self.conn.send(data)


def create_server(address, listen_num=4):
    server = socket.socket()
    server.bind(address)
    server.listen(listen_num)
    return server


def main():
    server = create_server(('127.0.0.1', 9999))
    while True:
        conn, addr = server.accept()
        print("{}已经连接".format(addr))

        p = CommunicationProcess(conn, addr)
        p.start()


if __name__ == '__main__':
    main()
