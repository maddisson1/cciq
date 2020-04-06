def isdigit(string):
    for l in string:
        if (l >= 'a' and l <= 'z') or (l >= 'A' and l <= 'Z'):
            return True
        else:
            return False 
string = input()
if isdigit(string):
    print('yes')
else:
    print('no')