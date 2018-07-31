import socket

# 非阻塞套接字实现并发服务器

class MyTCPServer(object):

    def __init__(self, address, num=5):
        self.server = socket.socket()
        self.server.bind(address)
        self.server.listen(num)
        self.server.setblocking(False)
        self.connection_pool = []
        self.address_pool = []

    def _session_loop(self):
        # session 轮询
        for conn in self.connection_pool:
            i = self.connection_pool.index(conn)
            ip = self.address_pool[i]
            try:
                data = conn.recv(1024)

                if not data:
                    conn.close()
                    self.connection_pool.remove(conn)
                    self.address_pool.remove(ip)
                    print("客户端 {} 已断开连接".format(ip))

                else:
                    print("{} SEND: {}".format(ip, data.decode('utf8')))
                    conn.send(data)
            except BlockingIOError:
                pass

    def start(self):
        # 服务器启动提示消息
        print("Successfully launched")

        # 轮询
        while True:
            # connect 轮询
            try:
                conn, addr = self.server.accept()
                print("{} 已连接".format(addr[0]))
                conn.setblocking(False)
                self.connection_pool.append(conn)
                self.address_pool.append(addr[0])
            except BlockingIOError as e:
                pass
            # session 轮询
            self._session_loop()


def main():
    server = MyTCPServer(('127.0.0.1', 9001))
    server.start()


if __name__ == "__main__":
    main()
