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
print(f"\033[96mSelected: {t[select]}\033[0m")

print("\033[96mCopying modules...\033[0m")
shutil.copyfile("./.setup/modules/socketnoise.py", f"./{t[select]}/modules/socketnoise.py")
print(f"\033[96mModules copied to ./{t[select]}/modules/\033[0m")

print('\033[96mInstalling default SSL Root certificates...\033[0m')
exec(open('./.setup/install_certifi.py').read())
print('\033[96mInstalled.\033[0m')

if delete == 'yes':
	print(f"Deleting {t['n'+select]}...")
	shutil.rmtree(f"./{t['n'+select]}/")
	print("Deleted.")