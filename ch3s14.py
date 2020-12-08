L=["Middle","East","Tech","Uni"]
l=len(L)
for i in range(l):
    a=L[i][0]
    print(a,end="")

#Let's use mapping
alist=[]
for j in range(l):
    alist.append(L[j][0])
maple= "".join(map(str,alist))  
print(maple)  
