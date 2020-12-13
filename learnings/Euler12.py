import math 
from collections import Counter 

flag = True
number = 7000000
n = 500
def primefactors(n):
    factors = []
    while n % 2 == 0: 
        factors.append(2) 
        n = n / 2
      
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            factors.append(i)
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factors.append(n) 
    return Counter(factors)   

while(flag):
    number = number + 1
    result = 1
    j = primefactors(number)
    for i in j.keys():
        result = result *(j[i]+1)
    if result >= 500:
        print(number)
        flag = False