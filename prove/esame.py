
class MovingAverage():
    def __init__(self, finestra):
        self.finestra=finestra

    def compute(self,list):
        lista_medie=[]
        if self.finestra==1:
            return list
        if self.finestra > len(list):
            return 'imposibiluu, too big'
        for i in range(0,len(list)-1):
            media=0
            somma=0
            for x in range(self.finestra):
                somma=somma+list[self.finestra-1+i-x]
            media=somma/self.finestra
            lista_medie.extend([media])
            if i==len(list)-self.finestra:
                break
        return lista_medie
        


#questo anche nel esame!!
class ExamException(Exception):
    pass




moving_average = MovingAverage(3)
result = moving_average.compute([1,2,3,4,5,6,7,8,9])
for item in result:
    print(item)