# Import the standard socket module.
import socket

# Create a socket object, and connect to the server.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost', 8001))

while True:
    data = input('Data to send [or "quit"]: ')
    socket.send(bytes(data, 'UTF-8'))
    if data == 'quit':
        socket.close()
        break
    else:		
        print(socket.recv(1024).decode())
