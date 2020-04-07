def rotation(s1, s2, char):
    if len(s1) != len(s2):
        return False
    else:
        rotate = s1[char:] + s1[:char]
        if rotate == s2:
            return 'yes'
        else:
            return 'no'  


s1 = input()
s2 = input()
char = int(input())
print(rotation(s1, s2, char))