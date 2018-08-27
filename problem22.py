filepath = '/Users/richardwang/Downloads/names.txt'
f = open(filepath, 'r')
data = f.read()
listneed = data.split(',')
listadd = []
for z in listneed:
    listadd.append(z[1:-1])
listadd = sorted(listadd)
sumup = 0
for i in range(len(listadd)):
    name = listadd[i]
    addup = sum([ord(j) - ord('A')+1 for j in name])
    sumup += addup * (i+1)
f.close()
print(sumup)
