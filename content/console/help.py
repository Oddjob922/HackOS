def help():
    file = open('content/console/known_cmds.txt', 'r')
    for line in file:
        print line
    file.close()