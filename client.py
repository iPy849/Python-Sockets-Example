# Built-in imports
import socket   
import threading

# Self imports
from resources.commons import InlineCommands

username = InlineCommands.DM
while InlineCommands.DM in username:
    username = input("Enter your username: ")

host = '127.0.0.1'
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "@username":
                client.send(username.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error Ocurred")
            client.close()
            exit(0)

def write_messages():
    while True:
        content = input('')
        # NOTE: No mandar mensajes vacios
        if content in [None, '']: continue
        message = f"{username}: {content}"
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()