import random, time
from content.console.telnet_known_cmds import telnet_is_cmd_error
def telnet_parse(command):
    if command == 'porthack':
        pass
    elif command == 'dc':
        session = False
    elif command == 'help' or command == '?':
        help_txt = open('content/console/telnet_help_txt.txt', 'r'); help_txt = help_txt.read()
        print help_txt
    

def telnet():
    ip = raw_input('IP Address?\n>')
    iplist = open('content/console/ip_list.txt', 'r'); iplist = iplist.read()
    print 'Trying to connect...'
    time.sleep(random.randint(1, 3))
    if ip == '' or ip.isspace():
        print "Connection failed, check to make sure you entered the IP correctly"
    else:
        if ip in iplist:
            print "Connected to %r" % ip
            session = True
            while session == True:
                command = raw_input('\n>')
                cmd_error = telnet_is_cmd_error(command)
                if cmd_error == False:
                    telnet_parse(command)
                else:
                    print "Not a recognized command. Type 'help' for a list of known commands"
