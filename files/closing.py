
# when we use write it creates the file or replace an existing file
newfile = open("D:\\newfile.txt", "w")

# close file
newfile.close()
newfile.closed

# other way to close the file, it is closed automatically
with open("D:\\newfile.txt", "w") as f:
    f.write("Hello python")