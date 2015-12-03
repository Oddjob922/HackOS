def telnet_is_cmd_error(command):
    cmd_list = open('content/console/telnet_known_cmds.txt', 'r')
    cmds = cmd_list.read(); cmds = cmds.replace('\n', '')
    if command in cmds:
        return False
    else:
        return True

