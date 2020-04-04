'''
Задача состоит в том, чтобы найти пропущенный элемент в массиве.
Мы запускаем цикл, который проходится от минимального до 
максимального числа и проверяет, есть ли это число в массиве. 
Если числа нет, то распечатывает его
'''

min = 1 # задаем минимальное число
max = 10 # задаем максимальное число
arr = [1, 2, 3, 4, 6, 8] # создаем массив чисел
for i in range(min, max+1): # запускаем цикл в диапазоне от мин до
                            # макс+1, т.к. последнее не включительно
    if i not in arr: # если элемента нет в массиве
        print(i) # распечатываем
