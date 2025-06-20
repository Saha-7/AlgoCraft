start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

def sumOfRange(s,e):
    total=0

    for i in range(s,e+1):
        total+=i
    return total


if (start<end and start>0):
    print(f"sum of Natural numbers from {start} to {end} is", sumOfRange(start, end))
else:
    print("Please check your input values according to the conditions")