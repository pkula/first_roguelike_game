import view
import os
import move_controller as moves
import data_manager as data
import menu
import character_selection
import table as t
import inventory as inv


# coordinates = [x,y]
def run():
    choice_from_menu = False
    while not choice_from_menu:
        player_choice = menu.menu()
        if player_choice == '1' or player_choice == '2' or player_choice == '3':
            choice_from_menu = True
        else:
            print("\nThere is no such choice!")
            input()

    if player_choice == '1':
        os.system('clear')
        x = 3
        y = 3
        inventory = []
        table = t.create_table()
        cover_table = view.get_empty_table(table)
        coordinates_a_b = data.find_a_b(table)
        coordinates_water = data.find_water(table)
        coordinates_dolars = data.find_dolars(table)
        coordinates_items = data.find_item(table)
        character = character_selection.character_selection()
        enter_pressed = False
        while not enter_pressed:
            os.system('clear')
            menu.rogulike_title()
            enter_input = input("Press ENTER to start\n")
            if enter_input == "":
                enter_pressed = True

        while True:
            inp = data.getch()
            if inp == "i":
                os.system("clear")
                print(inv.print_table(inventory))
                print("\nPress ENTER to return")
                quit_inventory = input()
            os.system("clear")
            w = moves.moves(table, inp, x, y, character)
            table = w[0]
            x = w[1]
            y = w[2]
            data.discover_table(table, cover_table, x, y)
            w = moves.teleport(table, inp, x, y, cover_table, character)
            table = w[0]
            x = w[1]
            y = w[2]
            data.discover_table(table, cover_table, x, y)
            w = moves.gate_teleport(table, cover_table, coordinates_a_b, x, y, character)
            x = w[0]
            y = w[1]
            table = w[2]
            moves.water(coordinates_water, x, y)
            coordinates_dolars = moves.dolars(coordinates_dolars, x, y)
            inventory = moves.get_inventory(coordinates_items, x, y, inventory)
            coordinates_items = moves.items(coordinates_items, x, y)
            data.discover_table(table, cover_table, x, y)
            view.print_table(cover_table)

    if player_choice == '2':
        os.system('clear')
        valid_input = False
        while not valid_input:
            os.system('clear')
            a = menu.options_menu()
            if a == '0':
                valid_input = True
                os.system('clear')
                run()

    if player_choice == '3':
        os.system('clear')
        os._exit(0)
