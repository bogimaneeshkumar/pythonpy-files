l = [1,2,3,56,76,768,8,1]
l.sort()
a = len(l)
i = 0
while i < a:
    p = l[i]
    j = l.count(p)
    l2 = []
    l2.append(j)
    l3 = []
    l3.append(j)
    i += j
l3.sort()
y = len(l3)
a = l3[y-1]
b = l2.index(a)
s = 0
for j in range  (0,b+1):
    h = l2[j]
    s = s + h
print(l[s-1])    