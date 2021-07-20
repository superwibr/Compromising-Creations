# Client-side transfer
import os
def transfer(s,path):
	if os.path.exists(path):
		f = open(path, 'rb')
		packet = f.read(1024)
		while packet != '':
			s.send(packet) 
			packet = f.read(1024)
		s.send('DONE')
		f.close()

	else: # the file doesn't exist
		s.send('Unable to find out the file')