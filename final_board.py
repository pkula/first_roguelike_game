import time
import sys
import os
import colors


def loose_information():
    loose = (colors.CBOLD + colors.CVIOLET + """
 __     __           _
 \ \   / /          | |
  \ \_/ /__  _   _  | | ___   ___  ___  ___
   \   / _ \| | | | | |/ _ \ / _ \/ __|/ _ |
    | | (_) | |_| | | | (_) | (_) \__ \  __/
    |_|\___/ \__,_| |_|\___/ \___/|___/\___|


    """ + colors.CEND)

    for char in loose:

        sys.stdout.write(char)
        time.sleep(0.02)
    return loose.center(os.get_terminal_size().columns)


def win_information():
    win = (colors.CBOLD + colors.CVIOLET + """
 __     __                    _
 \ \   / /                   (_)
  \ \_/ /__  _   _  __      ___ _ __
   \   / _ \| | | | \ \ /\ / / | '_ \
    | | (_) | |_| |  \ V  V /| | | | |
    |_|\___/ \__,_|   \_/\_/ |_|_| |_|

    """ + colors.CEND)

    for char in win:
        sys.stdout.write(char)
        time.sleep(0.02)
    return win
