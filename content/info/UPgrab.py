import getpass
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

	file = open('..\\info\\UP.txt', 'a')
	file.read
	file.write('%s\n' % user)
	file.write('%s' % passwd1)
	file.close