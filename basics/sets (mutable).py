# sets is basic a list without duplication elements

list4 = [1, 2, 3, 4, 5, 2, 3]

set(list4)

set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
# other way to create a set is
set2 = {11, 12, 13, 14, 15, 15, 15, 11}
type(set2)
len(set2) # 5

11 in set2 # true

10 in set2 # false

10 not in set2 # true

# add value
set2.add(16)

# remove element
set2.remove(11)

# operations and methods 
set1 = {1, 2, 3, 4}
set2 = {3, 5, 8}

# intersection method, what elements are equal in both sets
set1.intersection(set2)

# difference between two sets what set1 has more than set2
set1.difference(set2)

# unify two methods
set1.union(set2)

set1.pop() # remove first element of the set remove it randomly

set1.clear() # it clears the all elements stored into the set