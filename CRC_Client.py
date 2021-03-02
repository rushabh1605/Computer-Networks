import socket
def ascii_hex(sdata):
    s = sdata.encode()
    return s.hex()
def hex_bin(data):
    bin_f=''
    for i in range(0,len(data),2):
        temp_data = data[i:i+2]
        bin_p = "{0:08b}".format(int(temp_data, 16))
        bin_f = bin_f + bin_p
    return bin_f
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
	data = ascii_hex(data)
	data = hex_bin(data)
	l_key = len(key) 
	# Appends n-1 zeroes at end of data 
	appended_data = data + '0'*(l_key-1) 
	remainder = m2d(appended_data, key) 
	# Append remainder in the original data 
	codeword = data + remainder 
	print("Remainder : ", remainder) 
	print("Encoded Data (Data + Remainder) : ", codeword) 
	return codeword
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
# Create a socket object
port = 12345                # Reserve a port for your service.
key = "1101"
s.connect(("192.168.43.160", port)) # connect with server running on localhost
data = input('Enter a message to send: ')
new_data = encodeData(data, key)
#print(new_data)
s.send(new_data.encode())
print(s.recv(1024).decode())
