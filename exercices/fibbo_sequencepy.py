end = int(input('Type the end/limit of fibbo: '))
fib = [1]
for n in range(end+1):
    fib.append((fib[n-1] + (fib[n])))
    #print(n + (fib[n-1]))

print(fib)