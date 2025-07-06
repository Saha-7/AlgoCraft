
value=int(input('Enter Value: '))

def fun(n):
    if n==0:
        return
    
    fun(n-1)
    print(n)

fun(value)