class FileCSV():
    def __init__(self, name):
        self.name = name
        
    def get_data(self):
        list = []
        file = open(self.name, 'r')
        for line in file:
            if (file == 0):
                return None
            elements = line.split(',')
            list.append(elements)
        return list
