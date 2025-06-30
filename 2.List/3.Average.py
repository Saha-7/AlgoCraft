l=[10,20,30,40,50]

def getAvg(arr):
    sum=0
    size=len(arr)

    for ele in arr:
        sum+=ele
    
    ans=sum/size
    print(ans)

getAvg(l)