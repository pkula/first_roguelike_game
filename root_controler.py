import view
import os
import move_controler as move
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
x = 3
y = 3
coordinates = [x,y]
view.print_table(view.get_table_from_file("table.txt"))
table = view.get_table_from_file("table.txt")
while True:
    input = getch()
    if input == 's' and table[y+1][x] != '#':
        os.system("clear")
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y+1] = view.replace_in_string(table[y+1],x,'@')
        y = y + 1
        view.print_table(table)

    if input == 'w' and table[y-1][x] != '#':
        os.system("clear")
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y-1] = view.replace_in_string(table[y-1],x,'@')
        y = y - 1
        view.print_table(table)

    if input == 'd' and table[y][x+1] != '#':
        os.system("clear")
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y] = view.replace_in_string(table[y],x+1,'@')
        x = x + 1
        view.print_table(table)


    if input == 'a' and table[y][x-1] != '#':
        os.system("clear")
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y] = view.replace_in_string(table[y],x-1,'@')
        x = x - 1
        view.print_table(table)
