
def chngord(l,s) :

    if s =="asc":
        l.sort()
        return l

    elif s =="desc":
        l.sort(reverse=True)
        return l

    elif s=="none":
        return l
inputs=input("ENTER THE STRING :")
a=int(input("enter the total lenght of the list :"))
b=[]
for i in range(0,a):
    c=int(input())
    b.append(c)

res=chngord(b,inputs)

print(res)
