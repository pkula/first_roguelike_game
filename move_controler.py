def move(table,input):
    if input == 's' and table[y+1][x] != '#':
        os.system("clear")
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y+1] = view.replace_in_string(table[y+1],x,'@')
        y = y + 1
        view.print_table(table)

    if input == 'w' and table[y-1][x] != '#':
        os.system("clear")
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y-1] = view.replace_in_string(table[y-1],x,'@')
        y = y - 1
        view.print_table(table)

    if input == 'd' and table[y][x+1] != '#':
        os.system("clear")
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y] = view.replace_in_string(table[y],x+1,'@')
        x = x + 1
        view.print_table(table)


    if input == 'a' and table[y][x-1] != '#':
        os.system("clear")
        table[y] = view.replace_in_string(table[y],x,'.')
        table[y] = view.replace_in_string(table[y],x-1,'@')
        x = x - 1
        view.print_table(table)





def teleport():
