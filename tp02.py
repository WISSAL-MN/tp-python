from math import pi

val=[]
circ=[]
sur=[]
for x in range(4):
    x=input()
    val.append(int(x))
    circ.append(round(int(x)*pi*2,2))
    sur.append(round(int(x)**2*pi,2))
print (val),
print(circ),
print(sur) , 

    
