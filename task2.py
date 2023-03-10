"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
Реализуйте с list comprehension
"""

list_in = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_out = [
    list_in[i] for i in range(1, len(list_in)) if list_in[i] > list_in[i - 1]
]

print(f'Исходный список: {list_in}')
print(f'Результат: {list_out}')
