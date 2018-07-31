import selectors
import socket


def read(connection):
    recv_data = connection.recv(1024)
    if not recv_data:
        admin.unregister(connection)
        connection.close()
        print()
    else:
        print(recv_data.decode('utf8'))
        connection.send(recv_data)


def accept(server):
    conn, address = server.accept()
    admin.register(conn, selectors.EVENT_READ, read)


def main():
    global admin
    admin = selectors.EpollSelector()

    server = socket.socket()
    server.bind(('127.0.0.1', 9999))
    server.listen(5)

    admin.register(server, selectors.EVENT_READ, accept)
    while True:
        events = admin.select()
        for key, mask in events:
            callback = key.data
            sock = key.fileobj
            callback(sock)


if __name__ == "__main__":
    main()
