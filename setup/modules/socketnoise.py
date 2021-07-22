"""
	Socket Noise: a socket utility
"""

import struct

def _recvall(s, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = s.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

def _recvpack(s):
	# Read message length and unpack it into an integer
    raw_msglen = _recvall(s, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return _recvall(s, msglen)

def _pack(msg):
	msg = struct.pack('>I', len(msg)) + msg.encode('utf-8')
	return msg

def _talker(s, parm, function):
	# Helper function to write less/more lines than ever before!
	s[function](parm)


# default ask
def ask(s, msg):
	msg = _pack(str(msg))			# pack length in message
	_talker(s, msg, 'sendall')	# send message
	res = _recvpack(s)			# expect response
	return res					# return response

# default answer
def answer(s, callback):
	msg = _recvpack(s).decode('utf-8')	# receive message
	res = callback(msg)					# handle message
	_talker(_pack(res))					# respond
	return

# sync answer
def hear(s):
	msg = _recvpack(s).decode('utf-8')
	return msg
def respond(s, res):
	_talker(s, _pack(res))