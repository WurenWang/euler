fibo1,fibo2, index = 1, 1, 2
while len(str(fibo2)) < 1000:
    temp = fibo2
    fibo2 = fibo1 +fibo2
    fibo1 = temp
    index += 1
print(index)
