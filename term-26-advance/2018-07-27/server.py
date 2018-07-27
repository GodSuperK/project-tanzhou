from socketserver import ThreadingTCPServer, BaseRequestHandler


class MyHandler(BaseRequestHandler):

    def handle(self):
        user = self.client_address[0]
        print(user, '已经加入聊天室')
        self.request.send("亲爱的访客, 您已经成功加入聊天室".encode())

        while True:
            try:
                info = self.request.recv(1024)
                # 如果 receive 空消息, 表示客户端已断开连接
                if not info:
                    print(user, '已经退出聊天室')
                    break
                print(user, '说: ', info.decode())
                self.request.send(info)

            except ConnectionResetError:
                print(user, '已经退出聊天室')
                break


if __name__ == '__main__':
    server = ThreadingTCPServer(('0.0.0.0', 8877), MyHandler)
    server.serve_forever()
    print("Vian 聊天室已经成功启动")
