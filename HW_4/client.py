import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 12345

client_socket.connect((server_ip, server_port))
print(f"Connected to the setver {server_ip}:{server_port}")
server_message = client_socket.recv(1024)
print(f"Server sent: {server_message.decode()}")
message_to_send = "Hello, server!"
client_socket.send(message_to_send.encode())
client_socket.close()
