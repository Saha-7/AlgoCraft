l=[11,2,33,43,56,43,44,88,70,56,212,34]

def SepEvenOdd(arr):
    even=[]
    odd=[]
    for ele in l:
        if ele%2==0:
            even.append(ele)
        else:
            odd.append(ele)
    
    return (even,odd)

even, odd=SepEvenOdd(l)

print("Even :", even)
print("Odd :", odd)