d=input("Enter an equation in the form of 'ax+b' :")
x1=input("Enter a value for x :")
l=len(d)
def sonuc(d,x1):
    l=len(d)
    
    x1=int(x1)
    a=0
    while a<l:
        
        apokus=d[a]
        if apokus.isalpha()==1:
            apokus1=apokus
            a1=a
        a=a+1
    ilksayi= d[0:a1]
    ikincisayi= d[a1+2:l]
    ilksayii= int(ilksayi)
    ikincisayii=int(ikincisayi)
    # operator algılama şeysi :
    operator=d[a1+1]
    sonucc=0
    if operator =="+":
        sonucc = (x1*ilksayii)+ikincisayii
    if operator =="-":
        sonucc = (x1*ilksayii)-ikincisayii
    if operator =="*":
        sonucc = (x1*ilksayii)*ikincisayii
    if operator =="/":
        sonucc = (x1*ilksayii)/ikincisayii   
    return sonucc     
        
print(sonuc(d,x1))    


 
