from collections import Counter
from datetime import date

def Problem19 (n) :
  
  count = Counter()

  for year in xrange (1901, 2001) :
  
    for month in xrange(1, 13) :
      
      day = date (year, month, 1)
      count[day.weekday()] += 1
  
  return count[n]

print Problem19 (6)
