# decorator allow us insert behavior without modify the code
# the name of the params isn't related with the functionally
def dec_func(tarFunc):
    def func_wrapp():
        return "Python is such a " + tarFunc() + "language!"
    return func_wrapp

@dec_func
def dummy_func():
    return "cool"


# course annotations
#Decorators - functions that take another function as a parameter and extend its functionality and behavior without modifying it
def my_decorator(target_function):
    def function_wrapper():
        return "Python is the " + target_function() + " programming language!"
    return function_wrapper
    
@my_decorator
def target_function():
    return "coolest"
    
target_function() #returns 'Python is the coolest programming language!'