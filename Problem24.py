from math import factorial
 
def Problem24 (s):
    seq = list(s)
 
    for x in range(factorial(len(seq))):

        if x == 999999:
          return (''.join(seq))
 
        p = len(seq) - 1
        while p > 0 and seq[p - 1] > seq[p]:
            p -= 1
 
        seq[p:] = reversed(seq[p:])
 
        if p > 0:
            q = p
            while seq[p - 1] > seq[q]:
                q += 1

            seq[p - 1], seq[q] = seq[q], seq[p - 1]
 
print Problem24("0123456789")
