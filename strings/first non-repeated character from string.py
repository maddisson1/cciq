def fn(s):
  order = []
  counts = {}
  for x in s: #пробегаемся по строке
    if x in counts: # если символ уже в counts (повторяется)
      counts[x] += 1 # то считаем
    else: # в ином случае
      counts[x] = 1 # добавляем в counts со значением 1
      order.append(x) # добавляем в массив с уникальными элементами

  for x in order: # пробегаемся по массиву 
    if counts[x] == 1: # если элемент повторяется 1 раз
      return x # возвращаем его 
  return None

s = 'aqebeaqg'
print(fn(s))