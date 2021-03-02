import socket
def hex_ascii(data): 
    ascii = "" 
    for i in range(0, len(data), 2): 
        part = data[i : i + 2]   
        ch = chr(int(part, 16))
        ascii += ch 
    return ascii
def bin_hex(binary):
    temp = int(binary, 2)
    hexa = hex(temp)
    hexa = hexa[2:len(hexa)]
    return hexa
def xor(a, b):  
	result = [] 
	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 
	return ''.join(result) 
def m2d(divident, divisor):  
	pick = len(divisor) 
	temp = divident[0 : pick] 
	while pick < len(divident): 
		if temp[0] == '1': 
			temp = xor(divisor, temp) + divident[pick] 
		else:  
			temp = xor('0'*pick, temp) + divident[pick] 
		pick += 1
	if temp[0] == '1': 
		temp = xor(divisor, temp) 
	else: 
		temp = xor('0'*pick, temp) 
	checkword = temp 
    return checkword 
def encodeData(data, key):
    remainder = m2d(data, key) 
    print("Remainder : ", remainder)
    remainder = int(remainder,2)
    data = data[0:len(data)-3]
    str_data = bin_hex(data)
    str_data = hex_ascii(str_data)
    if(remainder == 0):
        return True,str_data
    else:
        return False,str_data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
port = 12345                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    signal = c.recv(1024).decode()
    #signal=input('Enter recieved signal : ')
    key = "1101"
    #print(signal)
    #print(msg)
    #print(key)
    ack,data = encodeData(signal,key)
    if(ack == True):
        print("Data : ",data)
        c.send('ACK : Data Received Successfully'.encode())
    else:
        print('Data : ',data)
        c.send('NACK : Data Corrupted..'.encode())
c.close()
