x=input("enter the string")
y=[]
z=len(x)
b=""
for i in range(0,z):
    y.append(x[i])
y.sort()
for i in y:
    b+=i
print(b)    
    
