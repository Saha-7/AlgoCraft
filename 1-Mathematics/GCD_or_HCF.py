       ## Naive's approach ##
# a=12, b=15
# We will take the minimum of this two(a,b) numbers, which is 12
# Now will keep on decreasing the value of a by 1 until we get a point that divides both of these numbers.
# Example -> 11,10,9,8,7,6,5,4,3  where 3 is the number that divides both of these numbers.

## Code => 

# def gcd(a,b):
#     i = min(a,b)
#     while i>0:
#         if(a%i==0 and b%i==0):
#             return i
#         i=i-1
    
# print(gcd(18,15))   







            ## Euclidean's Algorithm ##

# def gcd(a,b):
#     while a!=b:
#
#         if a>b:
#             a=a-b
#
#         else:
#             b=b-a
#
#     return a
#
# print(gcd(12,14))



            ## Optimized Euclidean's Approach ##

def gcd(a,b):

    if b==0:
        return a

    return gcd(b,a%b)

print(gcd(10,100))