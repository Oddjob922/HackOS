def is_cmd_error(command):
    cmds = ['ssh','listip']
    if command in cmds:
        return False
    else:
        return True
