import getpass, os, platform
import socketnoise
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
		socketnoise.say(s, '[CCCli] Changed directory to {}'.format(path))
	except Exception as e:
		socketnoise.say(s, '[CCli:{}] Cannot find "{}"'.format(e, path))
	return path
