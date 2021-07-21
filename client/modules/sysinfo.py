import platform, socket, re, uuid, logging, sys, json # modules
def sysinfo():
	try:
		info={}
		info['platform'] = platform.system() # system name
		info['platform-release'] = platform.release() # system release
		info['platform-version'] = platform.version()	# release version
		info['architecture'] = platform.machine() # system architecture
		info['hostname'] = socket.gethostname() # local device hostname
		info['local-ip-address'] = socket.gethostbyname(socket.gethostname()) # the device's IP within its network
		info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode())) # physical MAC address
		info['processor'] = platform.processor() # device processor

		# Info related to public IP
		if sys.version_info[0] > 2:
			from urllib.request import urlopen
		else:
			from urllib2 import urlopen
		response = urlopen('http://ipinfo.io').read()
		json_data = json.loads(response)

		latitude, longitude = json_data.get('loc').split(',')
		info['position'] = (latitude, longitude) # the device's position in lat/long
	
	except Exception as e:
		logging.exception(e)

	return info

