class FileCSV():
    def __init__(self, name):
        self.name = name
        
    def get_data(self):
        list = []
        file = open(format(self.name), 'r')

        for line in file:
            elements = line.split(',')
            list.append(elements)
        return list