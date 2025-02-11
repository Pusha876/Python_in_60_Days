# OOP Style | Part 3

### Instance Variables vs Class Variables
In Python, variables can be defined at the class level or the instance level. Understanding the difference between these two types of variables is crucial for effective object-oriented programming.

**Class Variables**

Class variables are shared by all instances of a class. They are defined within the class construction but outside any instance methods. These variables are typically placed right below the class header and before the constructor method. Class variables are used when you want to have a common value for all instances of a class.

Example:
```
class Shark:
animal_type = "fish" # Class variable

# Creating an instance of the Shark class
new_shark = Shark()
print(new_shark.animal_type) # Output: fish
```

In this example, ```animal_type``` is a class variable shared by all instances of the ```Shark``` class.

***Instance Variables***

Instance variables are unique to each instance of a class. They are defined within methods, typically the constructor method (**__init__**). Each object or instance of a class has its own copy of the instance variables.

Example:
```
class Shark:
def __init__(self, name, age):
self.name = name # Instance variable
self.age = age # Instance variable

# Creating instances of the Shark class
new_shark = Shark("Sammy", 5)
print(new_shark.name) # Output: Sammy
print(new_shark.age) # Output: 5

stevie = Shark("Stevie", 8)
print(stevie.name) # Output: Stevie
print(stevie.age) # Output: 8
```


In this example, name and ```age``` are instance variables that hold different values for each instance of the ```Shark``` class.

**Working Together**

Class variables and instance variables can be used together within the same class. This allows for shared attributes across all instances while maintaining unique attributes for each instance.

Example:
```
class Shark:
animal_type = "fish" # Class variable
location = "ocean" # Class variable

def __init__(self, name, age):
self.name = name # Instance variable
self.age = age # Instance variable

def set_followers(self, followers):
self.followers = followers # Instance variable
print(f"This user has {followers} followers")

# Creating instances and using both class and instance variables
sammy = Shark("Sammy", 5)
print(sammy.name) # Output: Sammy
print(sammy.location) # Output: ocean

stevie = Shark("Stevie", 8)
print(stevie.name) # Output: Stevie
stevie.set_followers(77) # Output: This user has 77 followers
print(stevie.animal_type) # Output: fish
```

In this example, ```animal_type``` and ```location``` are class variables, while ```name```, ```age```, and ```followers``` are instance variables.

**Conclusion**

Class variables are shared across all instances of a class, while instance variables are unique to each instance. Using both types of variables allows for efficient and organized code, adhering to the DRY (Don't Repeat Yourself) principle.



### Instance Methods vs Class Methods
Instance methods are functions defined within a class that operate on instances of that class. They can access and modify the attributes of the instance they belong to. Instance methods are the most common type of methods used in object-oriented programming in Python.

**Defining and Using Instance Methods**

To define an instance method, you use the def keyword within a class and include ```self``` as the first parameter. The ```self``` parameter refers to the instance of the class and allows access to its attributes and other methods.

Here is an example of defining and using instance methods:
```
class Person:
def __init__(self, name):
self.name = name # Instance attribute

def say_hi(self):
print(f'Hello, my name is {self.name}') # Instance method

# Creating an instance of the Person class
p = Person('Nikhil')
p.say_hi() # Calling the instance method
```

**Output**:
```
Hello, my name is Nikhil
```

In this example, the Person class has an ```__init__ ```method (constructor) that initializes the ```name``` attribute. The ```say_hi``` method is an instance method that prints a greeting using the ```name``` attribute.

### Properties
In Python, the ```property()``` function and the ```@property``` decorator provide a way to manage attributes in classes, allowing you to define methods that act like attributes. This is useful for encapsulation, validation, and creating computed attributes without changing the public API of your class.

**Using @property Decorator**

The ```@property``` decorator is a more Pythonic way to define properties. It allows you to define getter, setter, and deleter methods using decorators.

**Example**
```
class Circle:
def __init__(self, radius):
self._radius = radius

@property
def radius(self):
"""The radius property."""
return self._radius

@radius.setter
def radius(self, value):
self._radius = value

@radius.deleter
def radius(self):
del self._radius
```

In this example, the ```@property``` decorator is used to define the ```radius``` property. The ```@radius.setter``` and ```@radius.deleter``` decorators are used to define the setter and deleter methods.

### Static Methods
Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the ```@staticmethod``` decorator and do not require an instance of the class to be called. Static methods do not have access to the instance (```self```) or class (```cls```) variables and are used when some functionality is related to the class but does not need to access or modify the class or instance state.

**Example of Static Method**

Here is a simple example of a static method in Python:
```
class Maths:
@staticmethod
def addNum(num1, num2):
return num1 + num2

# Calling the static method without creating an instance of the class
result = Maths.addNum(1, 2)
print("The result is", result)
```

Output:
```
The result is 3
```

In this example, the addNum method is defined as a static method using the ```@staticmethod``` decorator. It can be called directly on the class Maths without creating an instance of the class.

## Syntactic Sugar = Simplified Syntax
Python has several pieces of syntax that are syntactic sugar. This sugar is syntax that isn’t strictly necessary but gives Python some of its flavor as a readable, beginner-friendly, and powerful language

### Magic Methods


### Abstract Classes and Abstract Methods
#### ABC- Abstract Base Class

Certainly! In Python, an abstract class is a class that cannot be instantiated and is typically used to define a common interface for its subclasses. Abstract classes are created using the abc module, which stands for Abstract Base Classes. Here's a concise example to illustrate how you can define and use an abstract class in Python:

```
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Example usage
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
```

#### Key Points:

1. **Importing** ```ABC``` and ```abstractmethod```: These are imported from the ```abc``` module.
2. **Defining an Abstract Class**: The ```Animal``` class inherits from ```ABC```, making it an abstract class.
3. **Abstract** Methods: The ```make_sound``` method is decorated with ```@abstractmethod```, indicating that it must be implemented by any subclass.
4. **Subclasses**: ```Dog``` and ```Cat``` are concrete classes that inherit from ```Animal``` and provide implementations for the ```make_sound``` method.


This structure ensures that any subclass of Animal must implement the make_sound method, providing a consistent interface across different types of animals.