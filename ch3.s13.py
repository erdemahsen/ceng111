def upperlower(string):
    length=len(string)
    liste=[]
    
    for i in range(length):
        buyuk=string.upper()
        kucuk=string.lower()
        
        if string[i]==buyuk[i]:
            liste.append(kucuk[i])
        if string[i]==kucuk[i]:
            liste.append(buyuk[i])    
    apo="".join(liste)
    return apo      

print(upperlower("boOK"))        