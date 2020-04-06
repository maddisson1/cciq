def reverse(string):
    if string == "":
        return string
    else:
        return string[-1] + reverse(string[:-1])

string = input()
print(reverse(string))