import os, sys, time, random
from content.effects.startup import startup
from content.info.UPgrab import UPgrab
from content.info.login import login
from content.other.verify_continue import verify_continue
from content.console.known_cmds import is_cmd_error
from content.console.help import help
from content.other.ip_rand_gen import ip_rand_gen
from content.console.listip import listip
from content.console.telnet import telnet

def parse(command):
	if command == 'telnet':
		telnet()
	elif command == 'listip':
		listip()
	elif command == 'ipgen':
		ip_rand_gen()
	elif command == 'help' or command == '?':
		help()
	elif command == 'clear':
		os.system('cls' if os.name == 'nt' else 'clear')
	elif command == 'exit':
		print "Terminal closed"
		sys.exit(0)

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
		command = raw_input('\n@')
		determine_if_error = is_cmd_error(command)
		if determine_if_error == True:
			print "Not a recognized command. Enter 'help' for a list of useable commands."
		elif determine_if_error == False:
			parse(command)
			
	

def menu():
	print "HackOS Boot sequence activated. Useable commands: 'new', 'continue'"
	option = raw_input('\n>')
	if option == 'new':
		UPgrab()
		print "In order to make changes to the system, a restart is required"
		time.sleep(1)
		print "Restarting..."
		time.sleep(1)
		menu()
	elif option == 'continue':
		verify = verify_continue()
		if verify == True:
			#startup()
			login()
			console()
		else:
			print "Error: No save file detected."
			time.sleep(1)
			menu()
	else:
		print 'Not a recognized command'
		time.sleep(.2)
		menu()
menu()
