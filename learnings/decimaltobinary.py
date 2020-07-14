a = 12

def decimaltobinary(a,binary):
    
    if a <= 1:
        return binary
    
    if a > 1:
        binary =  str(round(a%2)) + binary
        a = a//2
        return decimaltobinary(a,binary)
        

print(decimaltobinary(a,'1'))
