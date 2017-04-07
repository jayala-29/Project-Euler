# python implementation
def Problem14 (n) :

    i = 2
    j = 2

    longest = 0
    tracker = 0
    number = 0

    while (i < n) :

        j = i
    
        while (j != 1) :

            if (j % 2 == 0) :

                j /= 2

            else :

                j = 3 * j + 1

            tracker += 1

        if (longest < tracker) :

            longest = tracker
            number = i

        tracker = 0
        i += 1

    return number

print (Problem14 (1000000))
