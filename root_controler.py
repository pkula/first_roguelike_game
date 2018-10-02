import view
import os
import move_controler as moves
import data_manager as data
x = 3
y = 3
#coordinates = [x,y]
view.print_table(view.get_table_from_file("table.txt"))
table = view.get_table_from_file("table.txt")
cover_table = view.get_empty_table(table)
while True:
    input = data.getch()
    os.system("clear")
    w = moves.moves(table,input,x,y)
    table = w[0]
    x = w[1]
    y = w[2]
    data.discover_table(table,cover_table,x,y)
    w = moves.teleport(table,input,x,y,cover_table)
    table = w[0]
    x = w[1]
    y = w[2]
    data.discover_table(table,cover_table,x,y)
    view.print_table(cover_table)
