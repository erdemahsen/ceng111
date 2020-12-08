toplamUzunluk=0
def desc_length(liste):
    leng=len(liste)
    n=0
    toplamUzunluk=0
    while n<len(liste):
        uzunluk=len(str(liste[n]))
        toplamUzunluk+= uzunluk
        n=n+1
    return toplamUzunluk    
print(desc_length(eval(input())))


