import os

def character_selection():
    impossible_character = False
    while not impossible_character:
        possible_characters = ['@', '%', '<', '>', '^', 'R', 'T', 'Y', 'u']
        print("""
        Possible characters: @ , % , < , > , ^ , R , T , Y , U
        """)
        player_character = input('\nPlease choose your character: ')
        if player_character in possible_characters:
            impossible_character = True
            return player_character
        else:
            os.system('clear')
            print("Choose character from list! ")
