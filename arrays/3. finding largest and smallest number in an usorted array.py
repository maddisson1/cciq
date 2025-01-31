'''
Задача заключается в том, чтобы найти минимальное и максимальное
число в неотсортированном массиве.
Для начала нам нужно отсортировать массив , используем для этого
метод сортировки bubble sort. Суть метода состоит в том, чтобы
проходиться по элементам попарно, если нынешний элемент больше 
следующего, то они меняются местами.
Далее нам остается лишь вывести первый и последние элементы 
с массива
'''

arr = [6, 4, 2, 7, 8, 1] # создаем неотсортированный массив
for i in range(len(arr)): # проходимся по массиву
    for j in range(len(arr)-i-1): # запускаем диапазон от последнего 
                                # до -i
        if arr[j] > arr[j+1]: # если элемент больше следующего
            arr[j], arr[j+1] = arr[j+1], arr[j] # меняем их местами
                                            # так, чтобы больший элемент 
                                            # оказался в конце массива
min = arr[0] # сохраняем первый элемент (наименьший)
max = arr[-1] # сохраняем последний элемент (наибольший)
print('Smallest number is: ', min) 
print('Largest number is: ', max) 

