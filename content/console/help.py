def help():
    file = open('content/console/cmd_help.txt', 'r')
    for line in file:
        print line
    file.close()