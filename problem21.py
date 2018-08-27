def isamicable(n):
    listorg = []
    for i in range(1,n):
        if n % i == 0:
            listorg.append(i)
    pair = sum(listorg)
    listpair = []
    for j in range(1,pair):
        if pair % j == 0:
            listpair.append(j)
    if n == sum(listpair) and n != pair:
        return True
summ = 0
for n in range(10001):
    if isamicable(n):
        summ +=n
print(summ)
