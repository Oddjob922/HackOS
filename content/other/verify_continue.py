def verify_continue():
    save = open('content/info/save.txt', 'r')
    save_contents = save.read()
    save.close()
    if save_contents == '':
        return False
    else:
        return True
