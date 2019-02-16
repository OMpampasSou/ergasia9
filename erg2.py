print ("hello")
x=input('dwse arithmo')

while int(x) <= -1000000 or int(x) >= 1000000 :
     x=input('dwse arithmo')         
print ("twra tha emfanisw ton arithmo pou mou edwses ws ginwmena prwtwn")
thetik=1
die=2
pro=1
x=int(x)
stoix=0
ari=[0]
dinami=[0]
emfanise=""
if x<0:
     thetik=0
     x=-(x)
if x==1:
    print(1)
while x!=1:
    upol=x%die
 
    
    if upol!=0:
        protos=0
        while protos==0:
            die=die+1
            met=0
            for i in range (2,(die+1)):
             
                if (die%i)==0:
                    met=met+1
            if met ==1:
                protos=1
                 
        
    elif upol==0:
         if pro==1:
              ari[0]=die
              dinami[0]=1
              pro=0
         else:
              th=ari.count(die)
              if th==0:
                   stoix=stoix+1
                   ari.append(die)
                   dinami.append(1)
                  
              else:
                   dinami[ari.index(die)]=dinami[ari.index(die)]+1  
         x=x/die
         die=2
         
  
for z in range (0,(stoix+1)):
     if dinami[z]==1:
          emfanise= emfanise+"("+str(ari[z])+")"
     else:
          emfanise=emfanise+"("+str(ari[z])+"**"+str(dinami[z])+")"
     
if thetik==0:
     print("-",emfanise)
else:
     print(emfanise)
