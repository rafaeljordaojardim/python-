# List / Set / Dictionary comprehensions

list1 = []

for i in range(10):
    result = i ** 2
    list1.append(result)

list2 = [x ** 2 for x in range(10)]

list3 = [x ** 2 for x in range(10) if x > 5]

# using sets
set1 = { x ** 2 for x in range(10) }
set1
type(set1)

# dictionary
dict1 = { x: x * 2 for x in range(10) }

# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list4 = [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]