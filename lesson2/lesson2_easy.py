# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', "банан", "киви", "арбуз"]
idx = 0
for var in fruits:
    idx += 1
#    print(idx, '.', var)
    print('{0}. {1}'.format(idx, var))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

from random import sample
list1 = sample(range(0, 11), 5)
list2 = sample(range(0, 11), 5)
print(list1)
print(list2)
c = []
for i in list1:
    for j in list2:
        if i == j:
            list1.remove(i)
            break

print (list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

#list1 = [2, 7, 5, 6, 9, 15]
from random import sample
list1 = sample(range(0, 11), 5)
new_list = []
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        new_list.append(list1[i] / 4)
    else:
        new_list.append(list1[i] * 2)
print(new_list)