import getpass, sys, time, os
def UPgrab2():
	os.system('cls' if os.name == 'nt' else 'clear')
	time.sleep(1.5)
	os.system('cls' if os.name == 'nt' else 'clear')
	empty_input = True
	while empty_input == True:
		user = raw_input('Username: ')
		if user == '' or user.isspace():
			print 'Please set a valid username!'
		else:
			empty_input = False
		
	p_match = False
	while p_match == False:
		passwd1 = getpass.getpass()
		passwd2 = getpass.getpass('Confirm Password: ')
		if passwd1.isspace() or passwd1 == '':
			print 'Please set a valid password!'
		else:	
			if passwd1 == passwd2:
				p_match = True
			else:
				print 'Passwords did not match, try again'
				time.sleep(1)

	U = open('content/info/U.txt', 'w')
	U.write(user)
	U.close
	P = open('content/info/P.txt', 'w')
	P.write(passwd1)
	P.close
	save = open('content/info/save.txt', 'w')
	save.write('creds = True\n')
	save.close()
	
def UPgrab():
	save = open('content/info/save.txt', 'rw+')
	save_contents = save.read(); save_contents = save_contents.strip('\n')
	if save_contents == '':
		UPgrab2()
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print "It has been detected that an existing save file already exists, would you like to proceed? [y/n]"
		choice = raw_input('')
		if choice == 'y':
			print "ALL SAVE DATA WILL BE ERASED! Would you like to proceed? [y/n]"
			finalchoice = raw_input('')
			if finalchoice == 'y':
				print "Wiping save data and starting new game..."
				time.sleep(1.5)
				save.truncate(0)
				save.close()
				UPgrab2()
			else:
				sys.exit(0)
		else:
			sys.exit(0)
	