def getch():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def replace_in_string(string, nb_replace, char_to_replace):
    string = string[:nb_replace] + char_to_replace + string[nb_replace+1:]
    return string


def discover_table(table, cover_table, x, y):
    cover_table[y] = cover_table[y][:x-3] + table[y][x-3:x+4] + cover_table[y][x+4:]
    cover_table[y-1] = cover_table[y-1][:x-2] + table[y-1][x-2:x+3] + cover_table[y-1][x+3:]
    cover_table[y+1] = cover_table[y+1][:x-2] + table[y+1][x-2:x+3] + cover_table[y+1][x+3:]
    cover_table[y-2] = cover_table[y-2][:x-3] + table[y-2][x-3:x+4] + cover_table[y-2][x+4:]
    cover_table[y+2] = cover_table[y+2][:x-3] + table[y+2][x-3:x+4] + cover_table[y+2][x+4:]


def find_a_b(table):
    xA = 0
    yA = 0
    xB = 0
    yB = 0
    for i in range(len(table)):
        for w in range(len(table[i])):
            if table[i][w] == 'a':
                xA = w
                yA = i
            if table[i][w] == 'b':
                xB = w
                yB = i
    coordinates_a_b = [xA, yA, xB, yB]
    return coordinates_a_b


def find_water(table):
    coordinates_water = []
    for i in range(len(table)):
        for w in range(len(table[i])):
            if table[i][w] == 'o':
                coordinates_water = coordinates_water + [[w, i]]
    return coordinates_water


def find_dolars(table):
    n = 0
    coordinates_dolars = []
    for i in range(len(table)):
        for w in range(len(table[i])):
            if table[i][w] == '$':
                n = n + 1
                coordinates_dolars = coordinates_dolars + [[w, i]]
    return coordinates_dolars


def find_item(table):
    coordinates_items = []
    for i in range(len(table)):
        for w in range(len(table[i])):
            if table[i][w] == '?':
                coordinates_items = coordinates_items + [[w, i]]
    return coordinates_items
