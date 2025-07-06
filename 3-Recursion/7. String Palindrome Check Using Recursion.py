def Palindrome(strng):
    strng=strng.lower()
    if len(strng)<=1:
        return True
    
    if (strng[0]==strng[len(strng)-1]):
        return Palindrome(strng[1:len(strng)-1])
    else:
        return False
    

# val = input("Enter Vlaue: ")

ans=Palindrome("Madam")
print(ans)