N=10
def f(N):
    
    N=N*N
    
        
    print ("N = ",N)
def g():
    N=0
    print ("N = ", N)
    
def h():
    global N 
    f(N)
    g()
    return 
           
print(h()) #niye none çıkıo la

'''soru5 a=10
b=a+1
c=b+1
if a<=b<=c:
    print ("a")
    if c>b>a:
        print("b")
        if (c>b)>a:
            print("c")
        if (c>a) or (c==a):
            print("d")
    else:
        print("E")'''            




'''soru 4 if a<=b:
    print("A")
    if a/10 !=1:
        print("b")
    else:
        print("c")
if b>=a:
    print("C")  '''              