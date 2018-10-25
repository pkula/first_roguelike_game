import view
import os
import move_controler
import move_controler as moves
import data_manager as data
import menu
import character_selection
import table as t

# coordinates = [x,y]
def run():
    player_choice = menu.menu()
    if player_choice == '1':
        os.system('clear')
        x = 3
        y = 3
        table = t.create_table()
        cover_table = view.get_empty_table(table)
        coordinates_a_b = data.find_a_b(table)
        coordinates_water = data.find_water(table)
        coordinates_dolars = data.find_dolars(table)
        character = character_selection.character_selection()
        os.system('clear')
        print("Press ENTER to start")
        while True:
            input = data.getch()
            os.system("clear")
            w = moves.moves(table,input,x,y, character)
            table = w[0]
            x = w[1]
            y = w[2]
            data.discover_table(table,cover_table,x,y)
            w = moves.teleport(table,input,x,y,cover_table, character)
            table = w[0]
            x = w[1]
            y = w[2]
            data.discover_table(table,cover_table,x,y)
            w = moves.gate_teleport(table,cover_table,coordinates_a_b,x,y, character)
            x = w[0]
            y = w[1]
            table = w[2]
            moves.water(coordinates_water, x, y)

            coordinates_dolars = moves.dolars(coordinates_dolars, x, y)

            data.discover_table(table, cover_table, x, y)
            view.print_table(cover_table)

    if player_choice == '2':
        os.system('clear')
        a = menu.options_menu()
        if a == '0':
            os.system('clear')
            run()

    if player_choice == '3':
        os.system('clear')
        os._exit(0)
