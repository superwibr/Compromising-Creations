#! /usr/bin/env python3

import os, shutil

select = None
ASK = True
t = {
	'cli':'client',
	'ctrl':'controller',
	'ncli':'controller',
	'nctrl':'client'
}
while ASK:
	select = str(input('select (cli for client, ctrl for controller) > '))
	if select != 'cli' and select != 'cntrl':
		print('Not an option!')
	else:
		break
print(f"Selected: {t[select]}")
print(f"Deleting {t['n'+select]}...")
shutil.rmtree("./controller/")