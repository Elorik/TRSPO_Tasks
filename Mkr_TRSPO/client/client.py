import random
import socket
import json

def generate_matrices():
    """Генерує дві матриці з випадковими розмірами N x M та M x L."""
    n = random.randint(1001, 10000)
    m = random.randint(1001, 10000)
    l = random.randint(1001, 10000)

    matrix_1 = [[random.randint(-100, 100) for _ in range(n)] for _ in range(m)]
    matrix_2 = [[random.randint(-100, 100) for _ in range(m)] for _ in range(l)]

    return matrix_1, matrix_2

def fill_matrices(matrix_1, matrix_2):
    """Заповнює матриці випадковими числами."""
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            matrix_1[i][j] = random.randint(-100, 100)

    for i in range(len(matrix_2)):
        for j in range(len(matrix_2[i])):
            matrix_2[i][j] = random.randint(-100, 100)

def connect_to_server(host, port):
    """Встановлює з'єднання з сервером через TCP/IP."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

def send_data_to_server(client_socket, matrix_1, matrix_2):
    """Передає розміри та елементи матриць на сервер."""
    data = {
        'matrix_1': matrix_1,
        'matrix_2': matrix_2
    }
    json_data = json.dumps(data)
    client_socket.sendall(json_data.encode())

def receive_result_from_server(client_socket):
    """Отримує результати обчислень від сервера."""
    result = client_socket.recv(1024).decode()
    return result

def main():
    """Основна функція."""
    matrix_1, matrix_2 = generate_matrices()
    fill_matrices(matrix_1, matrix_2)

    client_socket = connect_to_server("server", 8080)
    send_data_to_server(client_socket, matrix_1, matrix_2)
    result = receive_result_from_server(client_socket)

    print(result)

if __name__ == "__main__":
    main()