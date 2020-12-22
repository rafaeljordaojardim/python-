# Positional arguments
# if we dont call this function with the same required params it throws an error
def my_function(x, y, z):
    return
# my_function(1, 2)

# keyword params - it ignores the order of the param
my_function(x = 1, z = 3, y = 4)

# default value
def my_function_default_value(x, y, z = 3):
    return

# when we dont know how many params we will need
# we can use to key-word args **kwargs
def function1(x, *args):
    print(x)
    for arg in args:
        print(arg)