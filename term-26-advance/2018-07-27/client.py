import socket

client = socket.socket()

client.connect(('127.0.0.1', 8877))
info = client.recv(1024)
print(info.decode())

while True:
    message = input("> ")
    if not message:
        continue

    if message == 'q':
        break

    client.send(message.encode())
    recv_info = client.recv(1024)
    print('SERVER 说: ', recv_info.decode())

client.close()
