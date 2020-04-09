def isPalindrome(x):
        
    rev = str(x)[::-1]
    if rev == str(x):
        return True
    else:
        return False

x = int(input())
if isPalindrome(x):
    print('true')
else:
    print('false')
