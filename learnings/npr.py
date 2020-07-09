
def permutation(n,r):
    result = 1
    
    for i in range(n,n-r,-1):
        result = result * i
    print(result)   

(permutation(5,3))
