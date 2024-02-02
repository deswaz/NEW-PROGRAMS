import socket

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
mysock.connect(('data.pr4e.org', 80))

# Send a GET request to retrieve the specified URL
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Loop to receive data until there is no more data to receive
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # Print the received data (including headers)
    print(data.decode(), end='')

# Close the socket connection
mysock.close()