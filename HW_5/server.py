import socket
import struct

def send_message(socket, message):
    message = message.encode()
    message_length = len(message)
    packed_length = struct.pack('!I', message_length)
    socket.sendall(packed_length)
    socket.sendall(message)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 12345
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print(f"The server is waiting for a connection on {server_ip}:{server_port}")
client_socket, client_address = server_socket.accept()
print(f"Connected with {client_address}")
for i in range(1, 101):
    message = f"Hello client, message {i}"
    send_message(client_socket, message)

client_socket.close()
server_socket.close()
