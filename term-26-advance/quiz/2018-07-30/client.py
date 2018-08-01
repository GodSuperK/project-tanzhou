import socket

client = socket.socket()
try:
    client.connect(('127.0.0.1', 9999))
except ConnectionRefusedError as e:
    print(e)
else:
    print("The connection is successful")

while True:
    message = input("> ")
    if not message:
        continue

    if message == 'q':
        break

    client.send(message.encode("utf8"))
    recv_info = client.recv(1024)
    print('SERVER 说: ', recv_info.decode("utf8"))

client.close()
