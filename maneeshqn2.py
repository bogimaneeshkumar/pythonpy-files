def fn(a):
    cd=""
    for i in range(0,16):
        if i>=12:
            cd+=a[i]
        else:
            cd+='*'
    return cd        

x=input("enter your cerdit card number :")
y=fn(x)
print("the result is :",y)
