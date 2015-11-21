import getpass
def login():
    usr_input = raw_input("Username: ")
    pw_input = getpass.getpass()
    creds_usr = open('content/info/U.txt', 'r')
    creds_pw = open('content/info/P.txt', 'r')
    username = creds_usr.read(); username = username.strip('\n')
    password = creds_pw.read(); password = password.strip('\n')
    if usr_input == username and pw_input == password:
        return True
    else:
        print "Credentials are incorrect"
        os.system('cls' if os.name == 'nt' else 'clear')