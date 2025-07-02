def fun(n):
    if n == 0:
        return
    print(n)
    fun(n - 1)
    print(n)


fun(3)


fun(3)
# → print(3)
# → fun(2)
    # → print(2)
    # → fun(1)
        # → print(1)
        # → fun(0)
            # → return (base case)
        # ← back from fun(0)
        # → print(1)  ← fun(1) resumes after fun(0)
    # ← back from fun(1)
    # → print(2)  ← fun(2) resumes after fun(1)
# ← back from fun(2)
# → print(3)  ← fun(3) resumes after fun(2)
