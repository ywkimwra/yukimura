x = int(input("Enter your number: "))

def isPalindrome(x):
    return str(x) == str(x)[::-1]

print(isPalindrome(x))