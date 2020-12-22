# it is defined used def key word
#you can define params
def my_first_function():
    "This describe the function and is named doc string"
    print("Hello Pyton")

help(my_first_function)

def my_first_function2(x):
    "This describe the function and is named doc string"
    print(x)

my_first_function2("some param")

def sumnum(x, y):
    return x + y

sumnum(1, 1)