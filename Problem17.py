# python implementation
zn = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}
tnn = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
tn = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}
td = {0: 10, 1: 13, 2: 13, 3: 15, 4: 14, 5: 14, 6: 13, 7: 15, 8: 15, 9: 14}
znt = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19 :8}

def Problem17(n) :

  if n < 10 :             
  
    return zn[n % 10]

  elif n < 100 :
  
    if n < 20 :
    
      return(tnn[n])    
      
    else :
    
      return(tn[n / 10] + zn[n % 10])
      
  elif n < 1000 :     
  
    if n % 100 == 0 :
    
      return zn[n / 100] + 7   
      
    elif n % 100 < 20 :
    
      return td[n / 100] + znt[n % 100] 
      
    else :
    
      return td[n / 100] + tn[(n % 100) / 10] + zn[n % 10]

count = 0 

for i in range(1,1000) : 
  count = count + Problem17 (i)
 
print count + 11
