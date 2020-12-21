my_string = '''
test
multiple
lines
'''
string1 = "Cisco Router"
string1[0] # return the first character
# we can put negative numbers to get the last to the first
string1[-1]


# Methods
var = "cisco router"
len(var) # return the number of string
var.index("i") # return teh index of the first occurrence of the letter
var.count("i") # return the number of the letters in the string
var.find("sco") # return the initial letter of the finding, if it doenst exist returns -1
var.lower() # lower string
var.upper() # upper string
var.startswith("C") # true or false
var.endswith("r") # true or false
var.strip() # it is the same of trim()
var.strip("$") # it removes this $ characters
var.replace(" ", "") # replace method
var.split(",") # return a list
"_".join(var) # put _ after each character

# Operators and formatting
# concatenate vara + varb
# return string three times var * 3
x = "Cisco"
y = " Switch"
"o" in x # returns true
"o" not in x # returns false

"Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
# we can put %.1f or %.2f to formatting the float numbers
# Other possible solution
"Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)
# we can put the index of the param
"Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)
# Formatting using F-Strings
model = '2600XM'
slots = 4
ios = 12.3

f"Cisco model: {model}, {slots} WAN slots, IOS {ios}"

# Slices
string1 = "o E2 10.110.8.9 the rest"
string1[5: 15] # starts on 1 up to but not including 15 -> if we pass just first it just cut the string
string1[::-1] # reverse the string

# slicing a string using a step mystring[start : stop: step]
my_string = "0123456789"
my_string[::2] # it returns the even index
my_string[1:7:2] # step is how many index it will skip

