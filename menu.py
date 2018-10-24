def menu():
    print("""
    [1] - Start Game
    [2] - Control
    [3] - Exit Game
    """)

    player_choice = input('\nSelect: ')
    return player_choice

def options_menu():
    print("""
    Character control - w,s,a,d
    """)

    a = input('\n Press 0  to go back: ')
    return a
