x=int(input('posa diastimata exeis ston nou sou gia na dwses?'))
lista=[]
if x<=0:
        while x<=0:
                x=int(input('dwse thetiko arithmo bro'))
for i in range (0,x):
        c=int(input('dwse arxitis  diastimatos'))
        v=int(input('dwse telos diastimatos'))
        la=[c,v]
        lista.append(la)
def sumIntervals(lista):
        
        athri=0
        lst=[]
        mikos=len(lista)
        for i in range(0,mikos):
                if lista[i][0]>=lista[i][1]:
                        suu=lista[i][0]-lista[i][1]
                else:
                        suu=-(lista[i][0])+lista[i][1]
                athri=athri+suu
        
        for z in range(0,mikos):
                lst.append(lista[z][1])
                for g in range(int(lista[z][0]),int(lista[z][1])):
                        lst.append(g)                
        mikoslst=len(lst)
        met=0
        print(lst)
        for i in range(0,mikos):
                for g in range(0,mikoslst):
                        if (i!=g):
                                if (lst[i]==lst[g]):
                                        met=met+1
                                      
        athri=athri-met        
        x="sumIntervals"+"("+str(lista)+")"+"Επιστρέφει"+str(athri)
        
        return x

print(sumIntervals(lista))
