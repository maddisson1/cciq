def palindrome(string):

    rotation = string[::-1]

    if rotation == string:
        return 'hell yeah'
    else:
        return 'f no('

string = input()
print(palindrome(string))