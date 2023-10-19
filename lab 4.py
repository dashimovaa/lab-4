# 1.1 Создание кортежа из пользовательского ввода
user_input = input("Введите строку без пробелов: ")
my_tuple = tuple(user_input) #тут мы создаем кортеж благодаря методу tuple где она берет каждый символ строки и создает кортеж и букв строки в скобках
print("Созданный кортеж:", my_tuple)

# 1.2 Преобразование кортежа в строку
my_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n') #задали кортеж
my_string = ''.join(my_tuple) #и метод .join преобразовывает кортеж в строку 
print("Строка: ", my_string)

# 1.3 Сцепление двух кортежей
tuple_A = (1, 2, 3, 4, 5, 6, 7) #задается кортежи а и б
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
combined_tuple = tuple_A[:4] + tuple_B[4:] # берется первая половина кортежа благодаря двоеточию и потпом пишется 4 а и вторая половина кортежа б наоборот
print(combined_tuple)

# 1.4 Подсчет и создание кортежа с количеством вхождений элементов
my_tuple = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
element_count = {}
for element in my_tuple:
    element_count[element] = element_count.get(element, 0) + 1
result_tuple = tuple((k, v) for k, v in element_count.items())
print("Элементы и их вхождения:", result_tuple) 
#cоздается пустой словарь element_count, в котором ключами являются элементы кортежа, а значениями - количество их вхождений.
#затем проход по my_tuple, и для каждого элемента увеличивается соответствующее значение в словаре.
#cоздается новый кортеж result_tuple, содержащий пары ключ-значение из словаря element_count, представляющие элементы и их вхождения.

# 1.5 Создание кортежей для хранения определенных объектов данных
data = (55, 6, 777, 70.0, '7', 'A')
integers = tuple(x for x in data if isinstance(x, int))
floats = tuple(x for x in data if isinstance(x, float))
strings = tuple(x for x in data if isinstance(x, str))
print(integers)
print(floats)
print(strings)
# есть кортеж data, который содержит разнообразные типы данных, включая целые числа, числа с плавающей запятой и строки.
# затем в коде создаются три новых кортежа: integers, floats и strings, каждый из которых содержит элементы из исходного кортежа data, но только определенного типа данных.
# для этого создается цикл и используется функция isinstance гед она берет опреденный заданный тип данных и дальше все выводится

# Задача 2: Множества и множества по comprehensions
# 2.1 Создание множества из пользовательского ввода с использованием множеств comprehensions
user_input = input("Введите строку без пробелов: ")
my_set = {char for char in user_input}
print("Созданное множество:", my_set)
# создается строка и с помочью множества my_set каждый символ из выведенной строки становится отдельным элементом множества
# и дубликаты элементов удаляются и остальные остаются и выводится

# 2.2 Нахождение разности двух множеств
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
difference_set = set_A.difference(set_B)
print(difference_set)
# создаются два множетва потом выполняется операция разности множеств. Метод .difference() используется для определения элементов, 
# которые присутствуют в set_A, но отсутствуют в set_B. Результат этой операции сохраняется в переменной difference_set.

# 2.3 Удаление элементов из множества А, которые также присутствуют в множестве B
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}
set_A.difference_update(set_B)
print(set_A)
# тут почти тоже самое только метод .difference_update() используется для обновления set_A таким образом, 
# чтобы оно содержало только элементы, которые находятся в set_A, но отсутствуют в set_B. и это сохраняется и выводится

# 2.4 Обновление множеств на основе элементов в множестве C
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}
set_C.update(set_A.intersection(set_C))
set_A.difference_update(set_A.intersection(set_C))
print("Обновленное множество C:", set_C)
# задается 3 множества.set_A.intersection(set_C) находит пересечение множества set_A и set_C, то есть элементы, 
# которые одновременно присутствуют в обоих множествах
# set_C.update(...) обновляет множество set_C, добавляя элементы из результатов пересечения в set_C
# дальше также одни и те же элементы у А и С. Длаьше по методу difference_update удаляются с А одинаковые элементы и дальше выводится строка С

# 2.5 Создание списка множеств размером m из комбинаций из надмножества A
A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5
result = [set(combo) for combo in combinations(A, n)][:m]
print(result)
# задается множество А и переменныe n,где указывается на оличество элементов которые должны быть для каждой комбинации
# и m, где указывает на количество комбинации
# дальше в строке кода создается список result, который содержит m комбинаций из множества A, 
# каждая из которых состоит из n элементов. Это делается с использованием функции combinations() из модуля itertools, 
# которая находит все комбинации элементов множества, и затем выбирается только первые m комбинаций.
#  Каждая комбинация преобразуется в множество и добавляется в список result.

 
# Задача 3: Группировка данных по производителю
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

sorted_cars = sorted(cars_list, key=lambda x: x[0])
for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):
    group_list = list(group)
    count = len(group_list)
    models = [car[1] for car in group_list]
    print(f"{manufacturer} {count} - {', '.join(models)}")

# задается список марок и моделей автомобилей.Далее список cars_list сортируется по первому элементу (по производителю) в каждом кортеже с помощью функции sorted().
# В результате этой операции список sorted_cars будет отсортирован по производителю.
# Затем используется цикл for и функция groupby из модуля itertools для группировки автомобилей по производителю. В этом цикле:
# for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):: Проходим по группам автомобилей, сгруппированным по производителю.
# group_list = list(group): Создаем список group_list, который содержит автомобили данного производителя, сгруппированные в текущей группе.
# count = len(group_list): Определяем количество автомобилей в данной группе.
# models = [car[1] for car in group_list]: Создаем список models, который содержит модели автомобилей в данной группе.
# print(f"{manufacturer} {count} - {', '.join(models)}"): Выводим информацию о производителе, количестве автомобилей и моделях в данной группе. Например, "BMW 1 - X6".
# Этот код выполняет группировку списка автомобилей по производителю и выводит информацию о количестве автомобилей и моделях для каждого производителя.
# 
