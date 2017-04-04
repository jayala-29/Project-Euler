# fast and computable version of problem 3

def Problem3(n) :
    q = next (x for x in range(2, n+1) if (n % x ==0))
    if (n == q) :
        return n
    else:
        return max(largest_p(q),largest_p(int(n/q)))

print(largest_p(600851475143))
