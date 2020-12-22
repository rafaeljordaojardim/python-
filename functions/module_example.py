my_var = 10

def my_function():
    print("This is the function inside the module!")

if __name__ == "__main__": # if it is imported in another module, it don't execute that
    print("This will be executed")