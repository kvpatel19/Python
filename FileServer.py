import socket
server_address = ('localhost', 60000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)
print("Server is listening...")
connection, client_address = server_socket.accept()
print(f"Connection from {client_address}")
filename = 'file_to_send.txt'
with open(filename, 'rb') as file:
    file_data = file.read()
    connection.sendall(file_data)
connection.close()
print("File sent successfully.")
