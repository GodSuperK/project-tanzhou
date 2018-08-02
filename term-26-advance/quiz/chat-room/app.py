import socket
import threading
import time
import json

my_lock = threading.RLock()
# 存储客户端发送的消息
room = []


def recv_thread(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            print('{} offline'.format(addr))
            conn.close()
            break
        # 客户端请求聊天室消息， 将消息发送给客户端
        if data.decode('utf8') == 'show':
            conn.send(json.dumps(room).encode('utf8'))
        else:
            msg = '{} {} say: {}'.format(time.strftime("%H:%M:%S"), addr, data.decode('utf8'))
            print(msg)
            my_lock.acquire()
            room.append(msg)
            my_lock.release()


def create_server():
    server = socket.socket()
    server.bind(('127.0.0.1', 9995))
    server.listen(5)
    return server


def main():
    server = create_server()
    while True:
        conn, addr = server.accept()
        print('{} is onine'.format(addr))
        t = threading.Thread(target=recv_thread, args=(conn, addr))
        t.start()


if __name__ == '__main__':
    main()
