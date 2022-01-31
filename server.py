# Built-in imports
import socket   
import threading

# Self imports
from resources.commons import InlineCommands

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
print(f"Server running on {host}:{port}")

clients = []
usernames = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message.encode('utf-8'))

def direct_message(original_message, _client):
    # Separa el encabezado del mensaje
    message_start_index = original_message.index(':')
    author = original_message[:message_start_index]
    message = original_message[message_start_index + 2:]
    # Encuentra al usuario objetivo y envia mensaje
    try: 
        taget_user_separator_index = message.index(':')
        target_user = message[1:taget_user_separator_index]
        content = message[taget_user_separator_index + 1:].strip()
        target_user_index = usernames.index(target_user) 
        user, client = usernames[target_user_index], clients[target_user_index]
        client.send(f'DM from {author}: {content}'.encode('utf-8'))
    # Lanza error en server y al usuario en cuestion
    except Exception as e:
        print(f'Direct Message (DM) error in \'{author}s\' thread: ', str(e))
        _client.send(f"User {target_user} wasn\'t found!".encode('utf-8'))

# NOTE: Se manejan los mensajes como strings y se codifican 
#       individualmente en cada envio
def handle_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            # NOTE: Mensajes directos
            if InlineCommands.DM in message:
                direct_message(message, client)
                continue
            broadcast(message, client)
        except Exception as e:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f"ChatBot: {username} disconnected", client)
            clients.remove(client)
            usernames.remove(username)
            client.close()
            exit(0)


def receive_connections():
    while True:
        client, address = server.accept()

        client.send("@username".encode("utf-8"))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{username} is connected with {str(address)}")

        message = f"ChatBot: {username} joined the chat!"
        broadcast(message, client)
        client.send("Connected to server".encode("utf-8"))

        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()

receive_connections()

