
def combinations(n,r):
    
    if r == 0 or r == n:
        return 1
     
    c = combinations(n-1,r-1) + combinations(n-1,r)
    return c


print(combinations(4,3))