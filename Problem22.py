# python implementation
from string import ascii_uppercase

def Problem22 (word) :
    return sum (ascii_uppercase.index (c) + 1 for c in word.strip ('"'))

with open('names.txt') as f :
  names = f.read().split(',')
  names.sort()
  
print sum(i * Problem22 (x) for i, x in enumerate (names, 1))
