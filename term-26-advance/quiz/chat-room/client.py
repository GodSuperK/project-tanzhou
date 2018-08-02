import socket
import json

client = socket.socket()
try:
    client.connect(('127.0.0.1', 9995))
except ConnectionRefusedError as e:
    print(e)
else:
    print("The connection is successful")


def user_input():
    # 输入模式
    data = input('(输入模式)> ')
    return data.encode('utf8')


def show_info():
    # 和查看模式
    client.send('show'.encode('utf8'))
    room_bytes = client.recv(1024)
    room = json.loads(room_bytes.decode('utf8'))
    for i in room:
        print(i)


def main():
    print('1: 输入模式 \n2:查看所有消息')
    while True:
        command = input('(命令模式)>>> ')
        if command == '1':
            data = user_input()
            client.send(data)
        elif command == '2':
            show_info()


if __name__ == '__main__':
    main()
