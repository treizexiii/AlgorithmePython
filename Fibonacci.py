def Fibonnaci(x):
    k = 1
    n = 0
    m = 1
    while(k < x):
        result = n + m
        n = m
        m = result
        k += 1
    return n

fib = Fibonnaci(100000)

print(fib)
