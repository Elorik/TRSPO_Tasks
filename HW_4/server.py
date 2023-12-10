import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 12345
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print(f"The server is waiting for a connection on {server_ip}:{server_port}")
client_socket, client_address = server_socket.accept()
print(f"Connect with {client_address}")
message_to_send = "Hello, client!"
client_socket.send(message_to_send.encode())
client_message = client_socket.recv(1024)
print(f"Client sent: {client_message.decode()}")
client_socket.close()
server_socket.close()
