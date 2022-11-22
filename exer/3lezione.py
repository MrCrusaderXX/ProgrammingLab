def sum_csv(file_name):
    values = []

    my_file = open(file_name, 'r')
    if my_file == 0:
        return None

    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            values.append(value)
    return values