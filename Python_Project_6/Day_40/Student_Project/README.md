# Student Project

### Learn the syntax of Classes

**Task 1**: Create a class named User. The class should:

1. have two methods, ```get_name``` and ```age```.

1. The two methods should contain only a ```pass``` statement inside them.

3. The ```get_name``` method should contain a ```self``` parameter.

4. The ```age``` method should contain a ```self``` and a ```current_year``` parameter.


```
class User:
    def get_name(self):
        pass
    
    def age(self, current_year):
        pass
```

**Task 2**: Add an ```__init__``` method to the ```User``` class. The method should have:

1. three parameters, ```self```, ```name```, and ```birthyear```.

2. ```name``` and ```birthyear``` should also be instance variables.

```
class User:
    
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def get_name(self):
        pass
    
    def age(self, current_year):
        pass
```

**Task 3**: Implement/code the ```User.age``` method so the method returns the age of the user given the ```self.birthyear``` instance variable and the ```current_year``` parameters.

```
class User:
    
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def get_name(self):
        pass
    
    def age(self, current_year):
        age = current_year - self.birthyear
        return age
```

**Task 4**: Let us suppose the current year is 2023.

1. Create a ```User``` instance for John, whose birth year is 1999.

2. Call the ```age``` method for that instance and print out the output.

You should get 24 as output.

```
class User:
    
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def get_name(self):
        pass
    
    def age(self, current_year):
        age = current_year - self.birthyear
        return age



user = User("john", 1999)
print(user.age(2023))
```

**Task 5**: Implement/code the ```User.get_name``` method, so the method returns the capitalized version of the user's name (e.g., JOHN). Note that the name is stored in the instance variable. Also, call the method for the instance you created in Task 4.

```
class User:
    
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear
        
    def get_name(self):
        return self.name.upper()
    
    def age(self, current_year):
        age = current_year - self.birthyear
        return age



user = User("john", 1999)
print(user.age(2023))
print(user.get_name())

```