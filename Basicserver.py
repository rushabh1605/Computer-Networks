# This is Server File

import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
# Create a socket object
port = 12345                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with clients.
	print 'Got connection from', addr
	buf=c.recv(1024)
	print 'received ' + buf + '\n'
	print 'echoing it back\n'
	c.send(buf)
	c.close() 