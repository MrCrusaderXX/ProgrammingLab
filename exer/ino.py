


file=open('table.csv','r')
somma=0
for line in file:
    diddums=line.split(',')
    if diddums[0] != 'Date':
        somma+=diddums[1]
return somma
