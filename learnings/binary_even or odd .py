a = 35

def decimaltobinary(a,binary):
    
    if a < 1:
        return binary
        
    if a >= 1:
        binary =  str(round(a%2)) + binary
        a = a//2
        return decimaltobinary(a,binary)
        

digits = (decimaltobinary(a,''))

print(digits)

if digits[-1] is '0':
    print('Even')
else:
    print('ODD')