import socket

client = socket.socket()

client.connect(('39.105.73.108', 8877))
info = client.recv(1024)
print(info.decode(encoding="utf8"))

while True:
    message = input("> ")
    if not message:
        continue

    if message == 'q':
        break

    client.send(message.encode(encoding="utf8"))
    recv_info = client.recv(1024)
    print('SERVER 说: ', recv_info.decode(encoding="utf8"))

client.close()
