from functools import reduce
a=eval(input())
l=[]
n=1
while n<a:
    if a//n==a/n:
        l.append(n)
    n+=  1  
def Max(c,d):
    if c>d:
        return c
    else :
        return d    
l=reduce(Max,l)
print(l)