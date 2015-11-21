import getpass, sys, time, os
def UPgrab2():
	print "Before the OS can be accessed, credentials must be set."
	time.sleep(1.5)
	os.system('cls' if os.name == 'nt' else 'clear')
	user = raw_input('Username: ')
	p_match = False
	while p_match == False:
		passwd1 = getpass.getpass()
		passwd2 = getpass.getpass('Confirm Password: ')
		if passwd1 == passwd2:
			p_match = True
		else:
			print 'Passwords did not match, try again'
			os.system('cls' if os.name == 'nt' else 'clear')

	U = open('content/info/U.txt', 'w')
	U.write(user)
	U.close
	P = open('content/info/P.txt', 'r')
	P.read
	P.write(passwd1)
	P.close
	
def UPgrab():
	U = open('content/info/U.txt', 'r')
	U_contents = U.read(); U_contents = U_contents.strip('\n')
	if U_contents == "":
		upgrab2()
	else:
		U.close()
		print "It has been detected that existing login information already exists, would you like to proceed? [y/n]"
		choice = raw_input('')
		if choice == 'y':
			UPgrab2()
		else:
			sys.exit(0)
	