#Q5
print("start entering the numbers")
num=[]
for i in range(0,100):
    inp=input()
    num.append(inp)
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if num[i]==num[j] :
            print("the number which is repeated is : {}".format(num[i]))
            break
        else :
            continue
