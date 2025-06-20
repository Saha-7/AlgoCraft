# num = int(input("Enter number: "))
#
# def checkpalindrome(num):
#     temp = num
#     rev = 0
#     while temp>0:
#         ld = temp%10
#         rev = rev*10 + ld
#         temp=temp//10
#     return rev == num
#
# if checkpalindrome(num):
#     print(f"{num} is palindrome number")
# else:
#     print(f"{num} is not palindrome number")









# num = int(input("Enter number: "))
#
# def checkpalindrome(num):
#     temp = num
#     rev = 0
#     while temp>0:
#         ld = temp%10
#         rev = rev*10 + ld
#         temp=temp//10
#
#     if rev == num :
#         return True
#     else:
#         return False
#
#
#
# print(checkpalindrome(num))







def pal(num):
    rev=0
    temp=num

    while temp!=0:
        ld = temp%10
        rev = rev*10 + ld
        temp = temp//10
    return rev == num


number = int(input("Enter value : "))
print(pal(number))