import socket

# Create a socket and bind to an address/port.
socket = socket.socket()
socket.bind(('localhost', 8001))

# Start listening (500 clients can connect at a time).
socket.listen(500) 
print('Server listening on port 8001...')

# Loop forever.
while True:

    # Wait for a client to connect to us.
    conn, addr = socket.accept()

    # Keep receiving data from that client, until they send "quit".
    # Every message the client sends, echo a response in uppercase.	
    while True:	
        databytes = conn.recv(1024).decode()
        datastr = str(databytes)
        if datastr == 'quit':
            print('Client asked to quit, so connection closed')
            conn.close()		
            break			
        else:
            print('Data received from client: %s' % datastr)
            conn.send(datastr.upper().encode())
