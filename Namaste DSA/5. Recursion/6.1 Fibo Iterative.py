def fibo_Iterative(n):
    if n<=1:
        return n
    
    a, b = 0, 1

    for i in range(2,n+1):
        c = a+b
        a=b
        b=c
    
    return c


print(fibo_Iterative(5))