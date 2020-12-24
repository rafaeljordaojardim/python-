# Iterators and Generators

# An iterator is an object that contains a countable number of values.

mytuple = ["apple", "banana", "cherry"]
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Generator -> 

def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y

my_object = my_gen(10, 5)
type(my_object)
# it get the first execution and we can take each one by calling next
next(my_object)
# we got in the end the exaut iteration
# WE CAN USE GENERATOR EXPRESSION
gen_exp = (x for x in range(5))
next(gen_exp)