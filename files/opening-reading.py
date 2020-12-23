# manipulating files
# r - reading
# w - writing
# a - appending
# b - binary
# x - exclusive creation
# w+ - write and read at the same time

myfile = open("./file.txt", "r")

myfile.mode # returns the mode opened

# when we read a file the cursor stops in the end of the file
# we have to use the seek method to put it on the beginning
myfile.read() # it returns a entire content of the file 

# with this method you can set the position of the cursor in bytes
myfile.seek(0)

# it returns the position of the cursor
myfile.tell()

myfile.read(5) # it returns the first-five bytes of the file

# it returns each line in each call
myfile.readline()

# it returns a list of lines
myfile.readlines()

for line in myfile.readlines():
    if line.startswith("a"): # it is case sensitive
        print(line)

# a way to scape the the \ is
# the R before string indicates as raw, it is treated as literal string
f = open(r"D:\Users\Tedoasd\pass")

# we can open the file in apending mode
myfile = open("./file.txt", "a")
