l = int(input("enter the first number :"))
u= int(input("enter the second number:"))

for n in range(l,u+1):
    for i in range(2,n):
        if n%i == 0:
            break
    else:

        print(n)
