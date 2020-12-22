# built-in namespace
    # python built-in functions, sort, max
# global namespace
    # all variables or functions that is defined or imported 
# local namespace
    # only inside in particular function in our program
my_var = 10
# print(list(range(10)))
print(my_var)

def my_var_func():
    my_var = 10
    print(my_var)

my_var_func()

print(my_var * 10) # this var is into a local namespace
##---------------------------------------------##
# if we want to use some global variable we have to specify it
my_var2 = 5
def my_var_func2():
    global my_var2
    print(my_var2)
    my_var2 = 10

my_var_func2()
##----------------------------------------------##
def my_var_returned():
    my_var = 10
    print(my_var)
    return my_var

result = my_var_returned()
print(result * 10)
