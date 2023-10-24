import socket
import struct

def receive_message(socket):
    packed_length = socket.recv(4)
    if not packed_length:
        return None
    message_length = struct.unpack('!I', packed_length)[0]
    message = socket.recv(message_length).decode()
    return message

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '127.0.0.1'
server_port = 12345
client_socket.connect((server_ip, server_port))
print(f"Connected to the server {server_ip}:{server_port}")
for i in range(1, 101):
    received_message = receive_message(client_socket)
    if received_message:
        print(f"Received: {received_message}")

client_socket.close()
