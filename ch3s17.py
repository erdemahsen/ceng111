sonuc=1
def Factoriyel(a):
    sonuc=a
    if a !=1:
        sonuc=a*Factoriyel(a-1)
        return sonuc
    else:  
        return sonuc    
print(Factoriyel(eval(input())))        
        
