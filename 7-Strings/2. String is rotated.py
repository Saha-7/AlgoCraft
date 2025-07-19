def rotate(s1,s2):
    if len(s1)!=len(s2):
        return False
    temp=s1+s1
    if temp.find(s2):
        return True
    else:
        return -1
    

print(rotate("ABCD","CDAB"))
