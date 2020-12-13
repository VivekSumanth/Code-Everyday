
# Find pair with given sum in an array

def hm(arr,sums):
    ht = dict()
    for i,j in enumerate(arr):
        temp = sums-j
        if temp in ht:
            print(ht[temp],i)
            return 
        ht[j] = i
    print('no pair')
        
hm([10,11,22,23,44],55)