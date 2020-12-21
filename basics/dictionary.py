# unorder set with key->value pairs, it is mutable and we can change it
# it is indexed by key

dict1 = {"vendor": "cisco", "model": 2600, "ios": 12.4, "ports": "4"}
d1 = { 1: "First element", 2: "Second element"}

dict1["vendor"] # returns cisco

dict1["RAM"] = "128" # add new element

# del dict1["ports"]

len(dict1) # returns the length

"ios" in dict1

"ios2" in dict1

"ios" not in dict1

dict1.keys() # returns the keys of the dictionry

dict1.values() # returns the values of the

dict1.items() # it returns a list of tuples with key and value
[("vendor", "cisco"), ("model", "2600")]