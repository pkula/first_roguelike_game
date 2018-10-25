import os


def menu():
    os.system('clear')
    print("""
    [1] - Start Game
    [2] - Control
    [3] - Exit Game
    """)

    player_choice = input('\nSelect: ')
    return player_choice


def options_menu():
    print("Character control - w, s, a, d")
    print("Inventory - i")
    a = input("\nPress 0 to go back: ")
    return a
