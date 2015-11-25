import os, random, sys, time
from content.effects.startup import startup
from content.tutorial.intro import tutorialP1
from content.info.UPgrab import UPgrab
from content.info.login import login
from content.other.verify_continue import verify_continue
from content.console.known_cmds import is_cmd_error


def parse(command):
	pass

def determine_if_error(command):
	error = True
	while error == True:
		cmd_error = is_cmd_error(command)
		if cmd_error == True:
			return True
		else:
			return False

def console():
	session = 'active'
	while session == 'active':
		command = raw_input('\n>')
		determine_if_error = determine_if_error(command)
		if determine_if_error == True:
			print "Not a recognized command. Enter 'help' for a list of useable commands."
		elif determine_if_error == False:
			parse(command)
			
	

def menu():
	print '''HackOS Boot sequence activated, please type 'new' to format drive and begin a new game or type 'continue' to restore your previous session :'''
	option = raw_input('\n>')
	if option == 'new':
		tutorialP1()
		UPgrab()
		print "In order to make changes to the system, a restart is required"
		time.sleep(1)
		print "Restarting..."
		time.sleep(1)
		menu()
	elif option == 'continue':
		verify = verify_continue()
		if verify == True:
			startup()
			login()
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
