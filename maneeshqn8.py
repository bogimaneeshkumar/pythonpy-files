x=input("enter the string")
b=len(x)
y=0
for i in range(0,b):
    if x[i].isnumeric():
        y+=int(x[i])
print("the result of addition is :{}".format(y))    
    
