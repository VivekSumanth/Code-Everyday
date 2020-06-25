# Counting Number of primes under given number
# sieve of eratosthenes
# count number of primes below some range

# take range of numbers
# 0 and 1 are not primes
# n starts from 2
# remove all the elements which are divisible by n and n**n

def countprimes(ran):
    
    arr = range(2,ran)

    k = 2
    
    while(k <= ran):
        for i in range(k*k,ran,k):
            if i in arr:
                arr.remove(i)
        k = k + 1
    print(arr)    
    
countprimes(100)
