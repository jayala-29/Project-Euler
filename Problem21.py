# python implementation
def Problem21 (first, last):
    
    tracker = []
    
    for i in range (first, last + 1) :
      s = 0
      for j in range (1,i) :
        if i % j == 0 : 
          s += j
      tracker += [s]
      
    pairs = []
    
    for i in range(last - first + 1) :
        ind = tracker[i]
        if i + first < ind and first <= ind and ind <= last and tracker[ind - first] == i + first :
            pairs.append ([i + first, ind])
    return pairs
 
print sum ([sum (pair) for pair in Problem21 (1,10000)])
