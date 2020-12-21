# looping throuth number of iteration pre set

vendors = ["cisco", "hp", "nortel", "avaya", "juniper"]

for each_vendor in vendors:
    print(each_vendor)

my_string = "cisco"
# iterator through a string
for letter in my_string:
    print(letter)

r = range(10)

for i in r:
    print(i * 2)

vendors = ["cisco", "hp", "nortel", "avaya", "juniper"]
len(vendors)

list(range(5))

for element_index in range(len(vendors)):
    print(vendors[element_index])

for index, element in enumerate(vendors):
    print(index, element)
else: # it executes after all loop execution
    print("The end of the list has been reached")

# while iterates while the value is true

x = 1

while x <= 10: 
    print(x)
    x = x + 1
else:
    print("now x is greater than 10")

# nested conditions and loops
x = "cisco"
if "in" in x:
    if len(x) > 3:
        print(x, len(x))

list1 = [4, 5, 6]

list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        print(i * j)
    print(i)

x = 1
while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z +=1

for number in range(10):
    if 5 <= number <= 9:
        print(number)