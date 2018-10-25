import os


def rogulike_title():
    print("""
    ██████╗  ██████╗  ██████╗ ██╗   ██╗███████╗██╗     ██╗██╗  ██╗███████╗
    ██╔══██╗██╔═══██╗██╔════╝ ██║   ██║██╔════╝██║     ██║██║ ██╔╝██╔════╝
    ██████╔╝██║   ██║██║  ███╗██║   ██║█████╗  ██║     ██║█████╔╝ █████╗
    ██╔══██╗██║   ██║██║   ██║██║   ██║██╔══╝  ██║     ██║██╔═██╗ ██╔══╝
    ██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║██║  ██╗███████╗
    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝
    """)


def menu():
    os.system('clear')
    rogulike_title()
    print("""
    [1] - Start Game
    [2] - Control
    [3] - Exit Game
    """)

    player_choice = input("""\nSelect: """)
    return player_choice


def options_menu():
    rogulike_title()
    print("Character control - w, s, a, d")
    print("Inventory - i")
    a = input("\nPress 0 to go back: ")
    return a
