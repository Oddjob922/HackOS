import sys, time
def progress(step, time_between):
	progress = 0
	progress_animation = ('-' * 50)
	while progress <= 100:
		sys.stdout.write('\r%s%%' % progress) #prints progress as number
		sys.stdout.write('[%s]'% progress_animation + ' ' * 5) #prints progress as "bar"
		time.sleep(time_between) #adds time between updates
		progress = progress + step #changes value of percentage and the "bar"
		progress_left = 100 - progress #calculates how much progress is remaining
		progress_animation = ('#' * (progress/2)) + ('-' * (progress_left/2))
	if progress << 100:
		time.sleep(time_between)
		sys.stdout.write('\r%s%%' % '100')
		sys.stdout.write('[' + '#' * 50 + ']' + ' ' * 5)
		time.sleep(.1)
	else:
		time.sleep(.1)
		

