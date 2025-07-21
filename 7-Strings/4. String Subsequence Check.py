def ChackSubsequence(str1, str2):
    """
    Check if str1 is a subsequence of str2.
    
    :param str1: The string to check as a subsequence.
    :param str2: The string in which to check for the subsequence.
    :return: True if str1 is a subsequence of str2, False otherwise.
    """
    S1=len(str1)
    S2=len(str2)
    j=0

    if S1==0: return True
    if S1>S2: return False

    for i in range(S2):
        if str1[j]==str2[i]:
            if j==S1-1:
                return True
            j+=1
    return False


ans=ChackSubsequence("ac","ahbgdc")
print(ans)

