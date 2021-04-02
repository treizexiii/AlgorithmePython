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

#En php
# function fibonacci($n)
# {
#     $sequence = [0, 1];

#     for ($i = 2; $i < $n; $i++) {
#         $sequence[$i] = $sequence[$i-1] + $sequence[$i-2];
#     }

#     return $sequence;
# }