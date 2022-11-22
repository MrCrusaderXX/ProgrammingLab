def sum_csv(file_name):

    sum=0.0
    
    my_file = open(file_name, 'r')
    if my_file == 0:
        return None

    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            value=elements[1]
            sum+=float(value)
    return sum



print(sum_csv('table.csv'))