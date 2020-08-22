# CTCI - recursion and dynamic programming.

class steps:
    
    def __init__(self,number):
        self.number = number
    
    def ways(self,number):
        if number == 1:
            return 1
        elif number == 2:
            return 3
        elif number == 3:
            return 4
        return self.ways(number-1) + self.ways(number-2) + self.ways(number-3)

n = steps(5)
print(n.ways(5))