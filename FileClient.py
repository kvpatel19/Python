import socket
server_address = ('localhost', 60000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
print("Connected to the server.")
file_data = b""
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    file_data += data
filename = 'received_file.txt'
with open(filename, 'wb') as file:
    file.write(file_data)
client_socket.close()
print("File received successfully.")
