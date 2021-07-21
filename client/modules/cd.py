import getpass, os, platform
def cd(command):
	path = command.strip('\r\n')[3:]

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
