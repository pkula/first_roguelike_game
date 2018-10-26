import os
import menu
import colors


def character_selection():
    impossible_character = False
    while not impossible_character:
        os.system('clear')
        menu.rogulike_title()
        possible_characters = ['@', '%', '<', '>', '^', 'R', 'T', 'Y', 'U']
        print("Possible characters: @ , % , < , > , ^ , R , T , Y , U")
        player_character = input(colors.CGREEN2 + '\nPlease choose your character: ' + colors.CEND)
        if player_character in possible_characters:
            impossible_character = True
            return player_character
