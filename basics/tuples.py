# tuples are immutable lists, we can't add or modify elements

my_tuple = ()
type(my_tuple)

# if we put just one element inside that we have to put a comma after
my_tuple = (9,) # if missing comma it is recognized as a int

my_tuple = (1, 2, 3, 4, 5)

# some cool things
tuple1 = ("Cisco", "2600", "12.4")
# the assign is propely done putting each value from tuple inside a variable
(vendor, model, ios) = tuple1
# we must put the same number of variables that there are in tuple1

# Tuple vs. Lists
# tuple are immutable, fixed length
# lists are mutable, variable length

# tuple uses ()
# lists uses []

# check the methods available
a = () # tuple
b = [] # list
dir(a)
dir(b)

# Tuple methods
tuple2 = (1, 2, 3, 4)
len(tuple2)

min(tuple2)

max(tuple2)

tuple2 + (5, 6, 7)

tuple2 * 2

tuple2[:2]

3 in tuple2 # true

3 not in tuple2 # false

5 in tuple2 # false

# deleting all tuple
del tuple2