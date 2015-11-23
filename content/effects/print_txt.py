import os, time, sys
def print_txt(path):
	file = open(os.path.normpath(path), 'r')
	for line in file:
		line = line.strip('\n')
		print ('\r%s' % line)
		time.sleep(2)
	file.close()
