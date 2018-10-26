import os
import colors


def rogulike_title():
    print(colors.CBEIGE2 + """
    ██████╗  ██████╗  ██████╗ ██╗   ██╗███████╗██╗     ██╗██╗  ██╗███████╗
    ██╔══██╗██╔═══██╗██╔════╝ ██║   ██║██╔════╝██║     ██║██║ ██╔╝██╔════╝
    ██████╔╝██║   ██║██║  ███╗██║   ██║█████╗  ██║     ██║█████╔╝ █████╗
    ██╔══██╗██║   ██║██║   ██║██║   ██║██╔══╝  ██║     ██║██╔═██╗ ██╔══╝
    ██║  ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║██║  ██╗███████╗
    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝
    """ + colors.CEND)


def menu():
    os.system('clear')
    rogulike_title()
    print("""
    [1] - Start Game
    [2] - Control
    [3] - Exit Game
    """)

    player_choice = input(colors.CGREEN2 + """\nSelect: """ + colors.CEND)
    return player_choice


def options_menu():
    rogulike_title()
    print("Character control - w, s, a, d")
    print("Inventory - i")
    a = input(colors.CGREEN2 + "\nPress 0 to go back: " + colors.CEND)
    return a
