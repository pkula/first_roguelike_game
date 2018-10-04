import view
import os
import move_controler as moves
import data_manager as data

#coordinates = [x,y]
def run():
    x = 3
    y = 3
    table = view.get_table_from_file("table.txt")
    cover_table = view.get_empty_table(table)
    print("Press something to start")
    coordinates_a_b = data.find_a_b(table)
    coordinates_water = data.find_water(table)
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
        w = moves.gate_teleport(table,cover_table,coordinates_a_b,x,y)
        x = w[0]
        y = w[1]
        table = w[2]

        moves.water(coordinates_water,x,y)

        data.discover_table(table,cover_table,x,y)
        view.print_table(cover_table)
