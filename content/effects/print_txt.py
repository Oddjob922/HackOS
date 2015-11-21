import os, time, sys
def print_txt(path):
	file = open(os.path.normpath(path), 'r')
	for line in file:
		os.system('cls' if os.name == 'nt' else 'clear')
		line = line.strip('\n')
		sys.stdout.write('\r%s' % line)
		time.sleep(1)
		sys.stdout.write('  3')
		time.sleep(1)
		sys.stdout.write('\b  2')
		time.sleep(1)
		sys.stdout.write('\b  1')
		time.sleep(1)
		sys.stdout.write('\r')
		os.system('cls' if os.name == 'nt' else 'clear')
	file.close
	os.system('cls' if os.name == 'nt' else 'clear')
