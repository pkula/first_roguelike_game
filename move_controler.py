import os
import view
import data_manager as data

def moves(table,input,x,y):
    if input == 's' and table[y+1][x] != '#':
        table[y] = data.replace_in_string(table[y],x,'.')
        table[y+1] = data.replace_in_string(table[y+1],x,'@')
        y = y + 1
    if input == 'w' and table[y-1][x] != '#':
        table[y] = data.replace_in_string(table[y],x,'.')
        table[y-1] = data.replace_in_string(table[y-1],x,'@')
        y = y - 1
    if input == 'd' and table[y][x+1] != '#':
        table[y] = data.replace_in_string(table[y],x,'.')
        table[y] = data.replace_in_string(table[y],x+1,'@')
        x = x + 1
    if input == 'a' and table[y][x-1] != '#':
        table[y] = data.replace_in_string(table[y],x,'.')
        table[y] = data.replace_in_string(table[y],x-1,'@')
        x = x - 1
    o = [table,x,y]
    return o



def teleport(table,input,x,y):
    if input == 't':
        view.print_table(table)
        input = data.getch()
        if input == 's' and table[y+2][x] != '#':
            table[y] = data.replace_in_string(table[y],x,'.')
            table[y+2] = data.replace_in_string(table[y+2],x,'@')
            y = y + 2
        if input == 'w' and table[y-2][x] != '#':
            table[y] = data.replace_in_string(table[y],x,'.')
            table[y-2] = data.replace_in_string(table[y-2],x,'@')
            y = y - 2
        if input == 'd' and table[y][x+2] != '#':
            table[y] = data.replace_in_string(table[y],x,'.')
            table[y] = data.replace_in_string(table[y],x+2,'@')
            x = x + 2
        if input == 'a' and table[y][x-2] != '#':
            table[y] = data.replace_in_string(table[y],x,'.')
            table[y] = data.replace_in_string(table[y],x-2,'@')
            x = x - 2
    o = [table,x,y]
    os.system("clear")
    return o
