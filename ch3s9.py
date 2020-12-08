def Distance(a=0,b=0,c=0,d=0):
    a=float(a)
    
    b=float(b)
    
    c=float(c)
    
    d=float(d)
    
    distance= ((a-c)**2+(b-d)**2)**(1/2)
    return distance

print(Distance(3))