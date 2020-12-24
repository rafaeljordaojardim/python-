# classes
# it means this class inheritance of the default class "object"
class MyRouter(object):
    "This is a class that describes the characteristics of a router"
    # this is the way that python identify a special method, putting __ before and after word
    # we have to put "self" in all class methods
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    # putting other methods
    def print_router(self, manuf_date):
        print(self.routername, self.model, self.serialno, self.ios)


router = MyRouter('r1', '2600', '123456', '12.4')

router.model

router.ios = 'other value'

# another way to get an attribute object
getattr(router, "ios")

# another way to set an attribute object
setattr(router, "ios", "new value")

# verify if there is an object, return true or false
hasattr(router, "ios")

#delete an attribute of a object
delattr(router, "ios")

isinstance(router, MyRouter)

# creating an child class
class MyNewRouter(MyRouter):
    "It is a child class"
    def __init__(self, routername, model, serialno, ios, portno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portno = portno

    def print_new_router(self, string):
        print(string + self.model)
    
# a class can take more than one parent
# class ChildClass(Parent1, Parent2, Parent3):
#     pass

issubclass(MyNewRouter, MyRouter)