def Problem2 (n) :
    sum = 0
    fib1 = 1
    fib2 = 1
    fib = fib1 + fib2
    while fib <= n :
        if fib % 2 == 0 :
            sum += fib
        fib1 = fib2
        fib2 = fib

        fib = fib1 + fib2
    return sum

print (Problem2 (4000000))
