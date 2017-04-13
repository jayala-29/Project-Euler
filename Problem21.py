# python implementation
import math

def Problem21 (n) :
  divs = [1]
  result = 1
  for j in xrange (1, n) :
    for i in xrange(2,j) :
      if n % i == 0 :
        divs.append(i)
        result += i
  return result
  
print Problem21 (10000)
