# python implementation
def Problem15 (n) :

    M = [1] * n

    for i in range (n) :

        for j in range (i) :

            M[j] = M[j] + M[j-1]

        M[i] = 2 * M[i - 1]

    return M[n - 1]
 
print (Problem15 (20))
