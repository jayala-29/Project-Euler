# python implementation
def Problem20 (n) :
  
  s = str (reduce (lambda x, y: x * y, [1] + range(1,n+1)))
  count = 1
  result = 0
  
  for character in s :
  
    if (count < len(s)) :
    
      result += int (character)
      
    count += 1
    
  return result
  
print Problem20 (100)
