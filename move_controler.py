import os
import view
import data_manager as data
import character_selection


#character = character_selection.character_selection()
def moves(table,input,x,y, character):
    if input == 's' and table[y+1][x] != '#':
        table[y] = data.replace_in_string(table[y],x,'.')
        table[y+1] = data.replace_in_string(table[y+1],x, character)
        y = y + 1
    if input == 'w' and table[y-1][x] != '#':
        table[y] = data.replace_in_string(table[y],x,'.')
        table[y-1] = data.replace_in_string(table[y-1],x, character)
        y = y - 1
    if input == 'd' and table[y][x+1] != '#':
        table[y] = data.replace_in_string(table[y],x,'.')
        table[y] = data.replace_in_string(table[y],x+1, character)
        x = x + 1
    if input == 'a' and table[y][x-1] != '#':
        table[y] = data.replace_in_string(table[y],x,'.')
        table[y] = data.replace_in_string(table[y],x-1, character)
        x = x - 1
    o = [table,x,y]
    return o

def teleport(table,input,x,y,cover_table, character):
    if input == 't':
        view.print_table(cover_table)
        input = data.getch()
        if input == 's' and table[y+2][x] != '#':
            table[y] = data.replace_in_string(table[y],x,'.')
            cover_table[y] = data.replace_in_string(cover_table[y],x,'.')
            table[y+2] = data.replace_in_string(table[y+2],x, character)
            y = y + 2
        if input == 'w' and table[y-2][x] != '#':
            table[y] = data.replace_in_string(table[y],x,'.')
            cover_table[y] = data.replace_in_string(cover_table[y],x,'.')
            table[y-2] = data.replace_in_string(table[y-2],x, character)
            y = y - 2
        if input == 'd' and table[y][x+2] != '#':
            table[y] = data.replace_in_string(table[y],x,'.')
            cover_table[y] = data.replace_in_string(cover_table[y],x,'.')
            table[y] = data.replace_in_string(table[y],x+2, character)
            x = x + 2
        if input == 'a' and table[y][x-2] != '#':
            table[y] = data.replace_in_string(table[y],x,'.')
            cover_table[y] = data.replace_in_string(cover_table[y],x,'.')
            table[y] = data.replace_in_string(table[y],x-2, character)
            x = x - 2
    o = [table,x,y]
    os.system("clear")
    return o

def gate_teleport(table,cover_table,coordinates_a_b,x,y, character):
    if coordinates_a_b[0] == x and coordinates_a_b[1] == y:
        table[y] = data.replace_in_string(table[y],x,'a')
        cover_table[y] = data.replace_in_string(cover_table[y],x,'a')
        x = coordinates_a_b[2]
        y = coordinates_a_b[3]+1
        table[y] = data.replace_in_string(table[y],x, character)
    if coordinates_a_b[2] == x and coordinates_a_b[3] == y:
        table[y] = data.replace_in_string(table[y],x,'b')
        cover_table[y] = data.replace_in_string(cover_table[y],x,'b')
        x = coordinates_a_b[0]
        y = coordinates_a_b[1]-1
        table[y] = data.replace_in_string(table[y],x, character)
    l = [x,y,table]
    return l


def water(coordinates_water,x,y):
    for i in coordinates_water:
        if i[0] == x and i[1] == y:
            exit()

def dolars(coordinates_dolars,x,y):
    coordinates = []
    for i in coordinates_dolars:
        if i[0] == x and i[1] == y:
                continue
        coordinates = coordinates + [i]
    if coordinates_dolars == []:
        exit()
    return coordinates
