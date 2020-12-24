
from itertools import *

list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101,102, 103, 'X', 'Y']
# chain get sequences and chains then together
a = chain(list1, list2)

for i in chain(list1, list2):
    print(i)


list(chain(list1, list2))

# first value is the starting and the second is the step
count(10, 2.5)
for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else: 
        break

# cycle - and it will print with no limit the sequence 11, 12, 13, 14, 15
a = range(11, 16)
for i in cycle(a):
    print(i)

# filterfalse - it is the oposite of filter, it print the false result
filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])

# islice -> 
a = range(10)
list3 = list(a)

islice(a, 2, 9, 2)