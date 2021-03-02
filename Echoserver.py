import socket               # Import socket module
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a socket object
port = 12345                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with clients.
	print 'Got connection from', addr
	while True:
		buf=c.recv(1024)
		print 'received ' + buf + '\n'
		if buf == 'bye':
			break
		msg=raw_input("Enter a msg")
		c.send(msg)
		if msg == 'bye':
			break
	c.close() 