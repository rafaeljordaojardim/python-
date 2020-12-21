# if, elseif, else

x = 10

if x > 5:
    print("X is greater than 5")
    print(x * 2)
elif x == 5:
    print("x is 5")
else:
    print("X is not greater than 5")

if x == 5 and type(x) is int:
    print("x is 5 and type is int")
elif x == 10 and type(x) is int:
    print("x is 10 and type is int")
