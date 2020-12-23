# when we use write it creates the file or replace an existing file
newfile = open("D:\\newfile.txt", "w")

# close file
newfile.close()
# we can use a list or a tuple 
newfile.writelines(["word1", "word2", "word3"])
newfile.writelines(("word1", "word2", "word3"))