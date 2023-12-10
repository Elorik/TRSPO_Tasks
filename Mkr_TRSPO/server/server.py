# server.py

import socket
import pickle
import numpy as np

def multiply_matrices(matrix_1, matrix_2):
    """Обчислює добуток матриць."""
    result = np.dot(matrix_1, matrix_2)
    return result.tolist()

def handle_client_connection(client_socket):
    """Обробляє підключення клієнта."""
    data = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        data += chunk

    matrices_data = pickle.loads(data)
    matrix_1 = np.array(matrices_data['matrix_1'])
    matrix_2 = np.array(matrices_data['matrix_2'])

    result = multiply_matrices(matrix_1, matrix_2)

    serialized_result = pickle.dumps(result)
    client_socket.sendall(serialized_result)
    client_socket.close()

def main():
    """Головна функція."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(5)

    print("Сервер слухає порт 8080...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Прийнято з'єднання від {addr}")
        handle_client_connection(client_socket)

if __name__ == "__main__":
    main()
