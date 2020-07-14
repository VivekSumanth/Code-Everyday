
def add_two_binary(a1,a2):
    
    leng = max(len(a1),len(a2))
    a1 = a1.zfill(leng)
    a2 = a2.zfill(leng)
    
    print(a1,a2)
    added = ''
    carry = 0
    
    for i in range(leng-1,-1,-1):
        k = int(a1[i])+int(a2[i]) + carry
        if k <= 1:
            added = str(k) + added
            carry = 0
        else:
            carry = 1
            if k > 2: 
                added =  '1' + added 
            else:
                added =  '0' + added
    if carry:
        return (str(carry)+added)
    return (added)
        
    

print(add_two_binary("1011","1"))
