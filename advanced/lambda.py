# lambda functions

a = lambda x, y: x * y

a(5, 3) # it prints 15

#Lambda functions - anonymous functions
# lambda arg1, arg2, ..., arg n: an expression using the arguments #general syntax
    
a = lambda x, y: x * y #defining a lambda function
    
a(20, 10) #result is 200; calling the lambda function
    
#Instead of...
def myfunc(list):
    prod_list = []
    for x in range(10):	
        for y in range(5):
            product = x * y
            prod_list.append(product)
    return prod_list + list
    
#...we can use a lambda function, a list comprehension and concatenation on a single line of code
b = lambda list: [x * y for x in range(10) for y in range(5)] + list

# MAP
def product10(a):
    return a * 10

r1 = range(10)

map(product10, r1) # returns an iterable object

list(map(product10, r1))

map((lambda a: a * 10), r1)

# Filter
filter((lambda a: a > 5), r1) # just return the true statements