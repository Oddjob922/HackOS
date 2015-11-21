import os, random, sys, time
from content.effects.startup import startup
from content.tutorial.intro import tutorialP1
from content.info.UPgrab import UPgrab
from content.info.login import login
def menu():
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''Welcome to my game, please pick an option:
	
	1) New Game

	2) Continue Game'''
	option = raw_input('\n>')
	if option == '1':
		UPgrab()
		
	elif option == '2':
		startup()
		tutorialP1()
		login()
	else:
		print 'Not a valid option!'
		menu()
menu()