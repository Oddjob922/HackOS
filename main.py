import os, random, sys, time
from content.effects.startup import startup
from content.tutorial.intro import tutorialP1
from content.info.UPgrab import UPgrab
from content.info.login import login
from content.other.verify_continue import verify_continue
def console():
	startup()
	login()
	

def menu():
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''HackOS Boot sequence activated, please type 'new' to format drive and begin a new game or type 'continue' to restore your previous session :'''
	option = raw_input('\n>')
	if option == 'new':
		UPgrab()
		tutorialP1()
		print "In order to make changed to the system, a restart is required"
		time.sleep(1)
		print "Restarting..."
		time.sleep(1)
		menu()
	elif option == 'continue':
		verify = verify_continue()
		if verify == True:
			console()
		else:
			print "Error: No save file detected. Please start a new game"
			time.sleep(1)
			menu()
	else:
		print 'Not a recognized command'
		time.sleep(.2)
		menu()
menu()
