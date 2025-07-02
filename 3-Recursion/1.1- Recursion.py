def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n)
    fun(n - 1)


fun(3)

# fun(3)->fun(2)->fun(1)->fun(0)

# 1 2 1 3 1 2 1 
