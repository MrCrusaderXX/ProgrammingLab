class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        
    def get_data(self):

        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except:
            raise ExamException('Non posso aprire o leggere il file')
            
        one_char = my_file.read(1)
        if not one_char:
            raise ExamException('il file è vuoto')
            
        my_file.close()
        
        temp_list = []
        
        file = open(format(self.name), 'r')
        
        for line in file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip()
            if elements[0] != 'epoch':
                temp_list.append(elements)
                
        file.close()

        
        list=[]
        duplicates=[]
        
        for row in temp_list:
            numerical_row=[]
            
            for i,element in enumerate(row):
                if i == 0:
                    try:
                        numerical_row.append(int(element))                        
                    except:
                        break
                else:
                    try:
                        numerical_row.append(float(element))
                        break
                    except:
                        break
                        
            if numerical_row[0] not in duplicates:
                duplicates.append(int(numerical_row[0]))
            else: raise ExamException('timestamp duplicata')            
            
                
            if len(numerical_row)==2:
                list.append(numerical_row)
            else: duplicates.pop()

        chek_list=[]
        
        for item in list:
            chek_list.append(item[0])
            
        if(all(chek_list[i] <= chek_list[i + 1] for i in range(len(chek_list)-1))):
            pass
        else:
            raise ExamException('timestamp non ordinate')
            
        return list

def difference(lista):
    if len(lista)==1:
        return None
    else:
        min=lista[0]
        max=lista[0]
        for item in lista:
            if item > max:
                max=item
            if item < min:
                min=item
        return max-min
        

def compute_daily_max_difference(list):
    inizio_g = list[0][0] - (list[0][0] % 86400)
    fine_g = inizio_g + 86400
    g_finale= list[-1][0] - (list[-1][0] % 86400) + 86400
    
    temperature_giornata=[]
    
    risultati=[]
    
    while fine_g <= g_finale:
        for item in list:
            if item[0] >= inizio_g and item[0] < fine_g:
                temperature_giornata.append(item[1])
                
        risultati.append(difference(temperature_giornata))
        
        temperature_giornata.clear()
        
        inizio_g=fine_g
        fine_g+=86400
        
    return risultati


time_series_file = CSVTimeSeriesFile(name='ddd.csv')


time_series = time_series_file.get_data()

print(compute_daily_max_difference(time_series))