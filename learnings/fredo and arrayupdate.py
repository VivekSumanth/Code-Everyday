def num(arr):
    arrsum = sum(arr)
    minm = max(arr)*(len(arr))
    
    for i in range(max(arr),-1,-1):
        
        if (i*(len(arr)) > arrsum):
            minm = min(minm ,i*(len(arr)))
            answer = i
        else:
            break
        
    return answer

print(num([9,10,5,6,1,2]))