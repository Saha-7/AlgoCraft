def chekPal(str):
    str=str.lower()
    if len(str)<=1:
        return True
    
    # if str[0]==str[len(str)-1]:
    #     return chekPal(str[1:len(str)-1])
    # else:
    #     return False

    if str[0]==str[-1]:
        return chekPal(str[1:-1])
    else:
        return False

ans=chekPal("aabaa")
print(ans)