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
	if delete != 'yes' and delete != 'no':
		print('Not an option!')
	else:
		break
print(f"Selected: {t[select]}")

print("Copying modules...")
def cpmod(mod):
	shutil.copyfile(f"./.setup/modules/{mod}.py", f"./{t[select]}/modules/{mod}.py")
cpmod('socketnoise')
cpmod('colorize')
print(f"Modules copied to ./{t[select]}/modules/")

print('Installing default SSL Root certificates...')
exec(open('./.setup/install_certifi.py').read())
print('Installed.')

if delete == 'yes':
	print(f"Deleting {t['n'+select]}...")
	shutil.rmtree(f"./{t['n'+select]}/")
	print("Deleted.")