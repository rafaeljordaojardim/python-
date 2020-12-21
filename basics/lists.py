
list1 = []

type(list1)

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

len(list1) # length of the list
# get elements 
list1[0] # cisco

list1[2] = "HP" 

#list methods
list2 = [-11, 2, 12]
min(list2) # return the min value of the array

max(list2) # return the max number

# append
list2.append(100)

# remove some member, we have three ways
# del list2[3]
list1.pop(0)
list1.remove("Cisco")

# insert, replace in a index
list1.insert(2, "Nortel")

# append one list in another, get the list2 elements and insert inside list1 
list1.extend(list2)

# index value
list1.index(-11)

list1.count(10)

# sort values
list2.sort()
sorted(list2)
# reverse 
list2.reverse()
sorted(list2, reverse=True)

# slicing extract parts of the list
list3 = [1, 2, 3, "a", "b", "c"]
list3[5:10]


