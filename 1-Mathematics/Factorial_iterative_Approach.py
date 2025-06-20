val = int(input("Enter the Number : "))

def fact(n):
    total= 1
    if n==0 or n==1:
        return 1
    if(n>=2):
        for i in range(2,n+1):
            total*=i
        return total


print(fact(val))