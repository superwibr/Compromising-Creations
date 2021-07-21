import getpass, os, platform
from logging import ERROR
def cd(s, command):
	res = {}
	path = command[3:]

	if path == '~':
		system = platform.system()
		homedir = "/"
		if system == 'Linux':
			homedir = "/home/{}"
		elif system == "Darwin":
			homedir = "/Users/{}"
		elif system == "Windows":
			homedir = "/"
		path = homedir.format(getpass.getuser())

	try:
		os.chdir(path)
		s.send('[CCCli] Changed directory to {}'.format(path))
	except ERROR as e:
		s.send('[{}] Cannot find "{}"'.format(e, path).encode())
	return path
