def listekesen(L=[1,2,10,20]):
    L=list(L)
    length=len(L)
    a=length/2
    a=int(a)

    return L[a:]+L[:a]
print(listekesen())    