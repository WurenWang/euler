def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p*p <=n:
        if n % p == 0:
            return False
        p += 2
    return True
listpri = '1379'
cirprime = 0
for num in range(2, 1000001):
    for z in str(num):
        if z not in listpri:
            continue
    if isprime(num):
        pristr = str(num)
        con = 0
        for long in range(1,len(str(num))+1):
             pritest = str(num)[long:] + str(num)[:long]
             if isprime(int(pritest)):
                 con +=1
        if con == len(str(num)):
            cirprime += 1
print(cirprime)
