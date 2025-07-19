def Palindrome(strng):
    strng=strng.lower()
    if len(strng)<=1:
        return True
    
    if (strng[0]==strng[len(strng)-1]):
        return Palindrome(strng[1:len(strng)-1])
    else:
        return False
    # if str[0]==str[len(str)-1]:
    #     return Palindrome(str[1:len(str)-1])
    # else:
    #     return False
    

# val = input("Enter Vlaue: ")

ans=Palindrome("Madam")
print(ans)