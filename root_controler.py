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
#coordinates = [x,y]
view.print_table(view.get_table_from_file("table.txt"))
table = view.get_table_from_file("table.txt")
while True:
    input = getch()
    os.system("clear")
    w = move.move(table,input,x,y)
    table = w[0]
    x = w[1]
    y = w[2]
    #k = move.teleport(table,input,x,y)
    view.print_table(table)
