
value=int(input('Enter Value: '))

def fun(n):
    if n==0:
        return
    
    print(n)
    fun(n-1)
    

fun(value)