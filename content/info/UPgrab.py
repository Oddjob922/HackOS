import getpass, sys
def UPgrab():
	user = raw_input('Username: ')
	p_match = False
	while p_match == False:
		passwd1 = getpass.getpass()
		passwd2 = getpass.getpass('Confirm Password: ')
		if passwd1 == passwd2:
			p_match = True
		else:
			print 'Passwords did not match, try again'

	U = open('content/info/U.txt', 'a')
	U.read
	U.write('%s' % user)
	U.close
	P = open('content/info/P.txt', 'a')
	P.read
	P.write('%s' % passwd1)
	P.close