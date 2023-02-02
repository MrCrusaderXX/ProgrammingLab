class Diff():
    def __init__(self, ratio=1):
        self.ratio=ratio
        

    def compute(self,list):
        lista_diff=[]
        
        for i in range(0,len(list)-1):
            differenza = list[i+1]-list[i]
            differenza=differenza/self.ratio
            lista_diff.extend([differenza])
            
        return lista_diff
        


#questo anche nel esame!!
class ExamException(Exception):
    pass




