arxi=0
prwtos=[]
x=input('dwse onoma arxiou') 
with open(x,'r') as wf:
    
    ana100=wf.read(100)
    while len(ana100)>0:
        pinakas=list(ana100)
        mikos=len(pinakas)
        for g in range (0,(mikos-1)):
            prwtos.append(pinakas[g])
        ana100=wf.read(100)
        

deuteros=set(prwtos)
grammata=list(deuteros)
mikos=len(prwtos)
mikos2=len(grammata)


for i in range (0,mikos2-1):
    if grammata[i]==' ':
        grammata.pop(i)
mikos2=len(grammata)


       
for i in range (0,mikos2-1):
    if grammata[i]=='\n':
        grammata.pop(i)
mikos2=len(grammata)

for i in range (0,mikos2-1):
    if grammata[i]=='\t':
        grammata.pop(i)
mikos2=len(grammata)


au3grammata=sorted(grammata)
fthigrammata=sorted(grammata,reverse=True)
me=1
for g in range (0,mikos2-1):
    if me==1:
        ss=[prwtos.count(grammata[g])]
        me=2
    else:
        f=prwtos.count(grammata[g])
        ss.append(f)
        
kefalaia=[x.upper() for x in fthigrammata]
with open(x,'w') as wf:
    for line in x:
        wf.write('')
for i in range (0,mikos):
    for g in range (0,mikos2):
        if prwtos[i]==au3grammata[g]:
            prwtos[i]=kefalaia[g]
           
      

for i in range (0,mikos):
    if prwtos[i]==" ":
        with open(x,'a') as wf:
            wf.write(" ")
    elif  prwtos[i]=="\n":
        with open(x,'a') as wf:
            wf.write("\n")
    elif prwtos[i]=="\t":
        with open(x,'a') as wf:
            wf.write("\t")
    else:
        a=str(prwtos[i])
        with open(x,'a') as wf:
            wf.write(a)
with open(x,'r') as wf:
        print(wf.read())

                
      
    
