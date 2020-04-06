def count(string):

    vowels = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    count_vowels = 0
    count_consonants = 0
    for l in string:
        if l in vowels:
            count_vowels+=1
        else:
            count_consonants+=1
    print('Vowels: ', count_vowels)
    print('Consonants: ', count_consonants)

string = input()
count(string)