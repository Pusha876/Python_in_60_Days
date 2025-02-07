# OOP (Object Oriented Programming)

## Class
A class in Python is a **user-defined template for creating objects**. It bundles data and functions together, making it easier to manage and use them. When we create a new class, we define a new type of object. We can then create multiple instances of this object type.
### Create Object
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data

## def __init__
In Python, ```__init__``` is a reserved method that is used to initialize the attributes of an object as soon as the object is formed**. It is known as a constructor in object-oriented programming. The __init__ method is called whenever an object is created from the class, and access is required to initialize the attributes of the class. A default parameter, named ‘```self```’ is always passed in its argument, which represents the object of the class itself.

In this code:
```
class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print self.x + ' ' + foo
```

the ```self``` variable represents the instance of the object itself. Most object-oriented languages pass this as a hidden parameter to the methods defined on an object; Python does not. You have to declare it explicitly. When you create an instance of the ```A``` class and call its methods, it will be passed automatically, 
```
a = A()               # We do not pass any argument to the __init__ method
a.method_a('Sailor!') # We only pass a single argument
```

The __init__ method is roughly what represents a constructor in Python. When you call ```A()``` Python creates an object for you, and passes it as the first parameter to the __init__ method. Any additional parameters (e.g., ```A(24, 'Hello')```) will also get passed as arguments--in this case causing an exception to be raised, since the constructor isn't expecting them.