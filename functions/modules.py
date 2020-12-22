# this is the app
# when a module is imported it is executed only once 
# (into the same file) no matter how many times it was imported
import module_example

print("This is the app ")

print(module_example.my_var)

module_example.my_function()

# reduce the resources into a program
# it just import the my_function
from module_example import my_function, my_var



# HELPFUL functions
import sys
help(sys) # it shows about the description and documentation

dir(sys) # list the available functions and attribuites

