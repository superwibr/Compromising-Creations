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
	if select != 'cli' and select != 'ctrl':
		print('Not an option!')
	else:
		break
ASK = True
while ASK:
	delete = str(input('Delete files after pass? (yes/no) > '))
	if delete != 'yes' and select != 'no':
		print('Not an option!')
	else:
		break
print(f"Selected: {t[select]}")
print("Copying modules...")
shutil.copyfile("./.setup/modules/socketnoise.py", f"./{t['n'+select]}/modules/socketnoise.py")


if delete:
	print(f"Deleting {t['n'+select]}...")
	shutil.rmtree(f"./{t['n'+select]}/")
	print("Deleted.")