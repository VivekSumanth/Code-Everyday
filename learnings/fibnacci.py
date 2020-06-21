#fibnocii
# 1,2,3,5,8,13,21,.....
# fn = fn-1 + fn-2

            #                          fib(5)   
            #                       /           \
            #               fib(4)                fib(3)   
            #             /        \              /       \ 
            #         fib(3)      fib(2)         fib(2)   fib(1)
            #         /    \       /    \        /      \
            #       fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
            #       /     \
            #      fib(1) fib(0)


def recursion(count):

    if count == 0:
        return 0
    elif count == 1:
        return 1
    else:
        print(count)
        return recursion(count-1) + recursion(count-2)
        
print(recursion(9))