from multiprocessing.pool import ThreadPool
import socket


def echo_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            print("{} 断开连接".format(addr))
            conn.close()
            break

        print(data.decode())
        conn.send(data)


def main():
    server = socket.socket()
    server.bind(('127.0.0.1', 8888))
    server.listen(10)
    pool = ThreadPool(20)

    while True:
        conn, addr = server.accept()
        print('{}已连接'.format(addr))
        pool.apply_async(echo_client, args=(conn, addr))


if __name__ == "__main__":
    main()
