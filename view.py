def get_table_from_file(file_name = "table.txt"):

    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "") for element in lines]
    return table
'''
def write_table_to_file("table.txt", get_table_from_file("table.txt")):

    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")

'''
def print_table(table):
    for i in table:
        print(i)


def replace_in_string(string,nb_replace,char_to_replace):
    string = string[:nb_replace] + char_to_replace + string[nb_replace + 1 :]
    return string
