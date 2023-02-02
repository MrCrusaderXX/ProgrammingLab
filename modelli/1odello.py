class Model():
    def __init__(self,data):
        self.data=data

        
    def fit(self, data):
        
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        
        raise NotImplementedError('Metodo non implementato')

    def evaluate(self,data):

        raise NotImplementedError('Metodo non implementato')



class IncrementModels(Model):

    
    def predict(self, data):
        
        somma_inc=0
        i=0
        new_data=data[-3:]        
        if isinstance(new_data, list):

            for item in new_data:
                if i>0:
                    somma_inc += new_data[i]-new_data[i-1]
                i+=1

            if i <= 1:
                return None

            som_med = somma_inc/(i-1)
            return som_med
    
        else: print('geh')

class FitIncrementModel(IncrementModels):

    def fit(self,data):
        j=len(data)
        j=j-3
        i=0
        somma=0
        for item in data[0:j]:
                if i>0:
                    somma += data[i]-data[i-1]
                i+=1
        if i <= 1:
            return None
        media= somma/(i-1)
        return media

    def finale(self,data):
        final=0
        final=data[-1]+(self.fit(data)+super().predict(data))/2
        return final




dati=[8,19,31,41,50,52,60,67,72,72,67,72]

risultato=FitIncrementModel(dati)
print (risultato.finale(dati))