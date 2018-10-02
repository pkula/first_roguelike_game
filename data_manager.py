def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch




def replace_in_string(string,nb_replace,char_to_replace):
    string = string[:nb_replace] + char_to_replace + string[nb_replace + 1 :]
    return string
