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



def discover_table(table,cover_table,x,y):
    cover_table[y] = cover_table[y][:x-2] + table[y][x-2:x+3] + cover_table[y][x+3:]
    cover_table[y-1] = cover_table[y-1][:x-2] + table[y-1][x-2:x+3] + cover_table[y-1][x+3:]
    cover_table[y+1] = cover_table[y+1][:x-2] + table[y+1][x-2:x+3] + cover_table[y+1][x+3:]
    cover_table[y-2] = cover_table[y-2][:x-2] + table[y-2][x-2:x+3] + cover_table[y-2][x+3:]
    cover_table[y+2] = cover_table[y+2][:x-2] + table[y+2][x-2:x+3] + cover_table[y+2][x+3:]
