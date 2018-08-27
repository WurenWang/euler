def isnb(n):
    l = []
    for i in range(1,n):
        if n % i ==0:
            l.append(i)
    if sum(l) > n:
        return True
listnb = []
for i in range(12,28123):
    if isnb(i):
        listnb.append(i)
listall = [x+y for x in listnb for y in listnb]
summ =0
for z in range(12,28123):
    if z not in listall:
        summ += z
print(summ)
