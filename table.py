import copy


def table_karniak():

    karniak = ["............oooo............",
               "...........oooooo...........",
               "..........oooooooo..........",
                ".........oooooooooo.........",
                ".........oooooooooo.........",
                ".........oooooooooo.........",
                "..........oooooooo..........",
                "..........oooooooo..........",
                "..........oooooooo..........",
                "..........oooooooo..........",
                "..........oooooooo..........",
                "...oooooooooooooooooooooo...",
                ".oooooooooooooooooooooooooo.",
                "oooooooooooooooooooooooooooo",
                "oooooooooooooooooooooooooooo",
                ".oooooooooooo..oooooooooooo.",
                "..oooooooooo....oooooooooo.."]
    return(karniak)


def water1():
    water = ["oooo.....oooo.........oooo...",
             ".oooo...oooo.oooo...oooo.....",
             "..oooo.oooo...oooo.oooo......",
             "...oooo........oooo.........."]
    return(water)


def water2():
    water = ["...oooo.........oooo...",
             "..oooo.oooo...oooo.oooo",
             ".oooo...oooo.oooo...ooo",
             ".........oooo........oo"]
    return(water)


def wall1():
    wall = [".#",
            "##",
            "##",
            "##",
            "#######",
            "#######",
            "##",
            "##",
            "#."]
    return(wall)


def wall2():
    wall = [".##########", "##########."]
    return(wall)


def create_first_table(heigh=30, width=125, width_of_wall=3):

    table = []
    heigh = 30
    width = 125
    width_of_wall = 3

    for i in range(width_of_wall):
        table.append('#'*width)
    for i in range(heigh-2*width_of_wall):
        table.append(width_of_wall*'#'+'.'*(width-2*width_of_wall)+width_of_wall*'#')
    for i in range(width_of_wall):
        table.append('#'*width)
    return(table)



def random_coordinates(obj, table_parameters):
    from random import randint
    y = randint(table_parameters[2] + 1, table_parameters[0] - table_parameters[2] - len(obj))
    x = randint(table_parameters[2] + 1, table_parameters[1] - table_parameters[2] - len(obj[0]))
    coordinates = [x, y]
    return coordinates


def add_object_to_table(table, obj, table_parameters):
    insert = False
    table2 = copy.deepcopy(table)
    while not insert:
        y = random_coordinates(obj, table_parameters)[1]
        x = random_coordinates(obj, table_parameters)[0]
        y1 = y

        for line in obj:
            w = ""
            x1 = x
            table2[y1] = list(table2[y1])
            for i in range(len(line)):
                if table[y1][x1] == 'o' or table[y1][x1] == '#':
                    return table
                table2[y1][x1] = line[i]
                x1 = x1 + 1
            for i in range(len(table2[y1])):
                w = w + table2[y1][i]
            table2[y1] = w
            y1 = y1 + 1
        insert = True
    return table2


def add_object_to_table_necesary(table, obj, table_parameters):
    insert = False
    table2 = copy.deepcopy(table)
    while not insert:
        y = random_coordinates(obj, table_parameters)[1]
        x = random_coordinates(obj, table_parameters)[0]
        y1 = y

        for line in obj:
            w = ""
            x1 = x
            table2[y1] = list(table2[y1])
            for i in range(len(line)):
                if table[y1][x1] == 'o' or table[y1][x1] == '#':
                    x1 = x1 + 1
                    break
                table2[y1][x1] = line[i]
                x1 = x1 + 1
            for i in range(len(table2[y1])):
                w = w + table2[y1][i]
            table2[y1] = w
            y1 = y1 + 1
        insert = True
    return table2


def change_one_character_in_string(string, index, character):
    string = string[:index] + character + string[index+1:]
    return string


def create_table():
    from random import randint

    heigh = 30
    width = 125
    width_of_wall = 3
    table_parameters = [heigh, width, width_of_wall]

    table = create_first_table()

    table = add_object_to_table(table, table_karniak(), table_parameters)
    table = add_object_to_table(table, table_karniak(), table_parameters)
    for i in range(3):
        table = add_object_to_table(table, water1(), table_parameters)
    for i in range(2):
        table = add_object_to_table(table, water1(), table_parameters)
    for i in range(3):
        table = add_object_to_table(table, wall1(), table_parameters)
    for i in range(3):
        table = add_object_to_table(table, wall2(), table_parameters)

    for i in range(20):
        table = add_object_to_table_necesary(table, wall1(), table_parameters)
    for i in range(20):
        table = add_object_to_table_necesary(table, wall2(), table_parameters)

    for i in range(width_of_wall, heigh-width_of_wall*2):
        for w in range(width_of_wall, width-width_of_wall*2):
            if table[i][w] != '#' and table[i][w] != 'o':
                chooser = randint(1, 1000)
                if chooser < 60:
                    table[i] = change_one_character_in_string(table[i], w, '#')
                if chooser > 50 and chooser < 110:
                    table[i] = change_one_character_in_string(table[i], w, 'o')
                if chooser > 200 and chooser < 210:
                    table[i] = change_one_character_in_string(table[i], w, '$')
                if chooser == 1000:
                    table[i] = change_one_character_in_string(table[i], w, '?')

    return(table)

create_table()