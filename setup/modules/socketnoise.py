"""
	Socket Noise: a socket utility
"""

import struct

def _recvall(conn, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = conn.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

def _recvpack(conn):
	# Read message length and unpack it into an integer
    raw_msglen = _recvall(conn, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return _recvall(conn, msglen)

def _pack(msg):
	msg = struct.pack('>I', len(msg)) + msg.encode('utf-8')
	return msg

def _talker(conn, parm, function):
	# Helper function to write less/more lines than ever before!
	getattr(conn, function)(parm)


# default ask
def ask(conn, msg):
	msg = _pack(str(msg))					# pack length in message
	_talker(conn, msg, 'sendall')	# send message
	res = _recvpack(conn)					# expect response
	return res								# return response

# default answer
def answer(conn, callback):
	msg = _recvpack(conn).decode('utf-8')	# receive message
	res = callback(msg)						# handle message
	_talker(conn, _pack(res), 'sendall')	# respond
	return

# sync answer
def hear(conn):
	msg = _recvpack(conn).decode('utf-8')
	return msg
def respond(conn, res):
	res = _pack(str(res))
	_talker(conn, res, 'sendall')