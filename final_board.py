import time
import sys

def board_view():
    print("""
    
      ___           ___           ___           ___                    ___                         ___           ___     
     /\__\         /\  \         /\  \         /\__\                  /\  \          ___          /\__\         /\  \    
    /:/ _/_       /::\  \       |::\  \       /:/ _/_                /::\  \        /\  \        /:/ _/_       /::\  \   
   /:/ /\  \     /:/\:\  \      |:|:\  \     /:/ /\__\              /:/\:\  \       \:\  \      /:/ /\__\     /:/\:\__\  
  /:/ /::\  \   /:/ /::\  \   __|:|\:\  \   /:/ /:/ _/_            /:/  \:\  \       \:\  \    /:/ /:/ _/_   /:/ /:/  /  
 /:/__\/\:\__\ /:/_/:/\:\__\ /::::|_\:\__\ /:/_/:/ /\__\          /:/__/ \:\__\  ___  \:\__\  /:/_/:/ /\__\ /:/_/:/__/___
 \:\  \ /:/  / \:\/:/  \/__/ \:\~~\  \/__/ \:\/:/ /:/  /          \:\  \ /:/  / /\  \ |:|  |  \:\/:/ /:/  / \:\/:::::/  /
  \:\  /:/  /   \::/__/       \:\  \        \::/_/:/  /            \:\  /:/  /  \:\  \|:|  |   \::/_/:/  /   \::/~~/~~~~ 
   \:\/:/  /     \:\  \        \:\  \        \:\/:/  /              \:\/:/  /    \:\__|:|__|    \:\/:/  /     \:\~~\     
    \::/  /       \:\__\        \:\__\        \::/  /                \::/  /      \::::/__/      \::/  /       \:\__\    
     \/__/         \/__/         \/__/         \/__/                  \/__/        ~~~~           \/__/         \/__/    

    """)


board_view()


def loose_information():
    loose = ("""
 __     __           _                      
 \ \   / /          | |                     
  \ \_/ /__  _   _  | | ___   ___  ___  ___ 
   \   / _ \| | | | | |/ _ \ / _ \/ __|/ _ |
    | | (_) | |_| | | | (_) | (_) \__ \  __/
    |_|\___/ \__,_| |_|\___/ \___/|___/\___|
    
    
    """)

    for char in loose:
       sys.stdout.write(char)
       time.sleep(0.02)
    return loose


def win_information():
    win = """
 __     __                    _       
 \ \   / /                   (_)      
  \ \_/ /__  _   _  __      ___ _ __  
   \   / _ \| | | | \ \ /\ / / | '_ \ 
    | | (_) | |_| |  \ V  V /| | | | |
    |_|\___/ \__,_|   \_/\_/ |_|_| |_|
    
    """

    for char in win:
        sys.stdout.write(char)
        time.sleep(0.02)
    return win





def points_holder():
    """
    information holder for user_hp
    win or loose result information
    :return:
    string with points value and message for user
    """

    user_hp = 0

    if user_hp <= 0:
        loose_information()
        print("Try again")
    elif user_hp > 100:
        win_information()
        print("Points or game inventory")

