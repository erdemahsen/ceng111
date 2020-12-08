
def ListeYokedici(liste):
    lenliste=len(liste)
    i=10
    n=0
    while n < lenliste:
        
        if type(liste[n-1])==list:
            del liste[n-1]

        else: 
            n=n+1    
    return liste        
liste=[1,2,3,[1,2],[1,23]]
print(ListeYokedici(liste))        


      
