def listip():
    list = open('content/console/ip_list.txt', 'r')
    list_contents = list.read()
    print list_contents
