#! /usr/bin/env python3

import os, shutil
import setup.modules.colorize as color

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
		color.err('Not an option!')
	else:
		break
ASK = True
while ASK:
	delete = str(input('Delete files after pass? (yes/no) > '))
	if delete != 'yes' and delete != 'no':
		color.err('Not an option!')
	else:
		break
color.info(f"Selected: {t[select]}")

color.info("Copying modules...")
def cpmod(mod):
	shutil.copyfile(f"./setup/modules/{mod}.py", f"./{t[select]}/modules/{mod}.py")
cpmod('socketnoise')
cpmod('colorize')
color.done(f"Modules copied to ./{t[select]}/modules/")

color.info('Installing default SSL Root certificates...')
exec(open('./setup/install_certifi.py').read())
color.done('Installed.')

if delete == 'yes':
	color.info(f"Deleting {t['n'+select]}...")
	shutil.rmtree(f"./{t['n'+select]}/")
	color.done("Deleted.")