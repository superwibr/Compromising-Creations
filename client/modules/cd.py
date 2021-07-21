import getpass, os, platform
def cd(command):
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
		os.chdir(homedir.format(getpass.getuser()))
		res['path'] = homedir
	else:
		os.chdir(path)
		res['path'] = path
	return res
