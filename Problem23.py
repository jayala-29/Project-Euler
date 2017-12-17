def add_proper_divs(x):
  divs = []
  for i in range(1,int(x ** 0.5)+1):
    if (x % i == 0):
      divs.append(i)
      if (i != 1):
        if (i != x / i):
          divs.append(x / i)
  total = 0
  for i in range(0,len(divs)):
    total += divs[i]
  return int(total)
  
def create_abundance(n):
  abundant_nums = []
  for i in range(1,n+1):
    if (i < add_proper_divs(i)):
      abundant_nums.append(i)
  return abundant_nums
  
def find_non_abundant(n, abundant_nums):
  non_abundant_nums = []
  is_abundant = 0
  for i in range(1,n+1):
    for j1 in range(0,len(abundant_nums)):
      if (i < abundant_nums[j1]):
        break
      for j2 in range(0,len(abundant_nums)):
        if (i < abundant_nums[j2]):
          break
        if (abundant_nums[j1] + abundant_nums[j2] == i):
          is_abundant = 1
          break
    if (is_abundant == 0):
      non_abundant_nums.append(i)
    is_abundant = 0
  total = 0
  for i in range(0,len(non_abundant_nums)):
    total += non_abundant_nums[i]
  return int(total)
  
print (find_non_abundant(28123, create_abundance(28123)))
