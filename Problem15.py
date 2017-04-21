# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

def Problem15 (n) :

    M = [1] * n

    for i in range (n) :

        for j in range (i) :

            M[j] = M[j] + M[j-1]

        M[i] = 2 * M[i - 1]

    return M[n - 1]
 
print (Problem15 (20))
