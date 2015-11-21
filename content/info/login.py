import getpass
def login():
    usr_input = raw_input("Username: ")
    pw_input = getpass.getpass()
    creds_usr = open('U.txt', 'r')
    creds_usr.read