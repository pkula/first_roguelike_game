import view
import os
import move_controler as moves
import data_manager as data
x = 3
y = 3
#coordinates = [x,y]
view.print_table(view.get_table_from_file("table.txt"))
table = view.get_table_from_file("table.txt")
while True:
    input = data.getch()
    os.system("clear")
    w = moves.moves(table,input,x,y)
    table = w[0]
    x = w[1]
    y = w[2]
    w = moves.teleport(table,input,x,y)
    table = w[0]
    x = w[1]
    y = w[2]
    view.print_table(table)
