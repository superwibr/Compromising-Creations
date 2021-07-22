"""
	Colorize: non-messy ANSI Select Graphic Rendition implementation
"""

C = { # reference dict
	'modifiers':{
			'reset': 0,
			'bold': 1,
			'dim': 2,
			'italic': 3,
			'underline': 4,
			'overline': 53,
			'inverse': 7,
			'hidden': 8,
			'strikethrough': 9,
			'blink':5 # only included slow blink.
	},
	'colors':{
		'black': 30,
		'red': 31,
		'green': 32,
		'yellow': 33,
		'blue': 34,
		'magenta': 35,
		'cyan': 36,
		'white': 37,

		'blackBright': 90,
		'redBright': 91,
		'greenBright': 92,
		'yellowBright': 93,
		'blueBright': 94,
		'magentaBright': 95,
		'cyanBright': 96,
		'whiteBright': 97
	}
}

def _mkseq(code):
	return f'\033[{code}m'

def info(message, appname):
	if not appname:
		appname = 'i'

	template = f"{_mkseq('1;34')}[{appname}] {_mkseq('0;94')}{message}"
	print(template)

def done(message, appname):
	if not appname:
		appname = '\u2713'

	template = f"{_mkseq('1;32')}[{appname}] {_mkseq('0;92')}{message}"
	print(template)

def warn(message, appname):
	if not appname:
		appname = '!'

	template = f"{_mkseq('1;33')}[{appname}] {_mkseq('0;93')}{message}"
	print(template)

def err(message, appname):
	if not appname:
		appname = '\u26A0'

	template = f"{_mkseq('1;31')}[{appname}] {_mkseq('0;91')}{message}"
	print(template)
