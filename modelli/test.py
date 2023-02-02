        j=len(data)
        j=j-3
        for item in data[0:j]:
                if i>0:
                    somma += data[i]-data[i-1]
                i+=1

            if i <= 1:
                return None
            media= somma/j