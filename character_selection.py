import os

def character_selection():
    possible_characters = ['@', '%', '<', '>', '^', 'R', 'T', 'Y', 'u']
    print("""
    Possible characters: @ , % , < , > , ^ , R , T , Y , U
    """)
    player_character = input('\nPlease choose your character: ')
    if player_character in possible_characters:
        return player_character
    else:
        os.system('clear')
        print("Choose character from list! ")
        character_selection
