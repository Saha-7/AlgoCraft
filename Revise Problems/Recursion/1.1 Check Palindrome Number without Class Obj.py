# WITHOUT CLASS - Using Functional programing

def isPalin(N):
    """Main function to check if number is palindrome"""
    return checkpal(N, N, 0)

def checkpal(original, current, reverse):
    """Helper function to check palindrome recursively"""
    if current == 0:
        if reverse == original:
            return 1
        else:
            return 0
    
    lastDigit = current % 10
    reverse = reverse * 10 + lastDigit
    current = current // 10
    
    return checkpal(original, current, reverse)

# Test the functions
print("=== Without Class Version ===")
print(isPalin(121))  # Output: 1
print(isPalin(100))  # Output: 0
print(isPalin(0))    # Output: 1
print(isPalin(5))    # Output: 1
print(isPalin(1221)) # Output: 1
print(isPalin(123))  # Output: 0

# User input version
n = int(input("Enter a number: "))
result = isPalin(n)
print(result)