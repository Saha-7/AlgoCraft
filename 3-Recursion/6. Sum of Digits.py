def sumDigit(n):
    if n<10:
        return n
    ld=n%10
    nd=n//10

    return ld+sumDigit(nd)

ans=sumDigit(57)

print(ans)