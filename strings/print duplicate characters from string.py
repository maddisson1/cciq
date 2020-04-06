word = 'Hello'
arr = []
for i in range(len(word)):
    count = 0
    for l in range(i+1):
        if word[l] == word[i]:
            count+=1
    if count >= 2:
        arr.append(word[i])
print(arr)