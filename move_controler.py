import os
import view



def move(table,input,x,y):
    if input == 's' and table[y+1][x] != '#':
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y+1] = view.replace_in_string(table[y+1],x,'@')
        y = y + 1
    if input == 'w' and table[y-1][x] != '#':
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y-1] = view.replace_in_string(table[y-1],x,'@')
        y = y - 1
    if input == 'd' and table[y][x+1] != '#':
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y] = view.replace_in_string(table[y],x+1,'@')
        x = x + 1
    if input == 'a' and table[y][x-1] != '#':
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y] = view.replace_in_string(table[y],x-1,'@')
        x = x - 1
    o = [table,x,y]
    return o



def teleport():
    pass
