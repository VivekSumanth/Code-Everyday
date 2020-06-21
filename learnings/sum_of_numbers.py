#recursion.

def sumof(number):
    
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number == 2:
        return 3
    else:
        return number + sumof(number-1)
print(sumof(100))
