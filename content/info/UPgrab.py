import getpass, sys
def UPgrab():
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
	U.read
	U.write(user)
	U.close
	P = open('content/info/P.txt', 'w')
	P.read
	P.write(passwd1)
	P.close