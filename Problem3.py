# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def Problem3(n) :
    q = next (x for x in range(2, n+1) if (n % x ==0))
    if (n == q) :
        return n
    else:
        return max(largest_p(q),largest_p(int(n/q)))

print(largest_p(600851475143))
