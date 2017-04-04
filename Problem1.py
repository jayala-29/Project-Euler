# Python implementation
 
 def Problem1 (n) :
        total = 0
        n -= 1
        while (n > 0) :
                if (n % 3 == 0 or n % 5 == 0) :
                        total += n
                n -= 1
        return total

print (Problem1(1000))
