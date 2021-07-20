# Server-side transfer
def transfer(conn,command):

    conn.send(command)
    f = open('./recieved.tmp','wb')
    while True: 
        bits = conn.recv(1024)
        if 'Unable to locate the file' in bits:
            print ('[Error!] Unable to locate the file')
            break
        if bits.endswith('DONE'):
            print('[CCCtrl] Transfer completed ')
            f.close()
            break
        f.write(bits)