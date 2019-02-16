x=[]
mik=int(input('dwse mikos listas'))
for i in range(mik):
    a=int(input('dwse stoixio listas'))
    x.append(a)
def maxSequence(x):
    mikos=len(x)
    dg=0
    for i in range(0,mikos-1):
        lista=str(x[i])
        sigk=int(x[i])
        for g in range(i+1,mikos):
            sigk=sigk+int(x[g])
            if dg==0:
                max1=sigk
                dg=1
            lista=lista+","+str(x[g])
            
            if sigk>max1:
                max1=sigk
                emf=lista
                               
    epistrofi=str(max1)+":"+"["+emf+"]"        
        
    return epistrofi
        
        
        
print(maxSequence(x))
