num = int(input("Enter the num: "))
original = num

res = 0

while num>0:
    num = num//10
    res+=1

print(f"the num of digits in {original} is ",res)