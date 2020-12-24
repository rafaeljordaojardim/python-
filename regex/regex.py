mystr = "YOu can learn any programming language, whether it is Python2, Python3"

import re

# a = re.match(pattern, string, optional flags)
# Try to apply the pattern at the start of the string, 
# returning a match object, or None if no match was found.
a = re.match("You", mystr)

# entire method returned
a = re.match("you", mystr, re.I)

mystr = "can learn any programming language, whether it is Python2, Python3"

# if we want to get in the middle of the string uses search
# a = re.search(pattern, string, optional flags)

a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*" , mystr)

# find all returns a list
#Regular Expressions - the "re.match" and "re.search" methods
# a = re.match(pattern, string, optional flags) #general match syntax; "a" is called a match object if the pattern is found in the string, otherwise "a" will be None
    
mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP."
    
import re #importing the regular expressions module
    
a = re.match("You", mystr) #checking if the characters "You" are indeed at the beginning of the string
    
a.group() #result is 'You'; Python returns the match it found in the string according to the pattern we provided
    
a = re.match("you", mystr, re.I) #re.I is a flag that ignores the case of the matched characters
    
# a = re.search(pattern, string, optional flags) #general search syntax; searching for a pattern throughout the entire string; will return a match object if the pattern is found and None if it's not found
    
arp = "22.22.22.1      0         b4:a9:5a:ff:c8:45 VLAN#222             L"
    
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp) #result is '22.22.22.1'; 'r' means the pattern should be treated like a raw string; any pair of parentheses indicates the start and the end of a group; if a match is found for the pattern inside the parentheses, then the contents of that group can be extracted with the group() method applied to the match object; in regex syntax, a dot represents any character, except a new line character; the plus sign means that the previous expression, which in our case is just a dot, may repeat one or more times; the question mark matching as few characters as possible
    
a.groups() #returns all matches found in a given string, in the form of a tuple, where each match is an element of that tuple
('22.22.22.1', '0', 'b4:a9:5a:ff:c8:45 VLAN#222', 'L')
    
#Regular Expressions - the "re.findall" and "re.sub" methods
a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp) #returns a list where each element is a pattern that was matched inside the target string
['22.22.22.1'] #result of the above operation - a list with only one element, the IP address matched by the regex
    
b = re.sub(r"\d", "7", arp) #replaces all occurrences of the specified pattern in the target string with a string you enter as an argument
'77.77.77.7      7         b7:a7:7a:ff:c7:77 VLAN#777             L   77.77.77.77' #result of the above operation