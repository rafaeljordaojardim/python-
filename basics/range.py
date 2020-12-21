# it has a default start at 0, but not including the number

range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range(5, 10)

# we can add step
range(0, 10, 2) # [0, 2, 4, 6, 8]

#xrange it is deprecated
# xrange()

r = range(10)

list(r) # returns a list


list(r)[2:5]