#way #1
test_list = [1, 3, 5, 6, 3, 5, 6, 1] 
print(set(test_list))

#way #2
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
res = []
for el in test_list:
    if el not in res:
        res.append(el)
print(res) 
