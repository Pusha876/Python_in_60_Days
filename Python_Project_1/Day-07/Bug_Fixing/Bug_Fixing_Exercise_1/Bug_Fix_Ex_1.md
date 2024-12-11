### Bug-Fixing Exercise 1
The code below tries to write the items of temperatures each in one line in the file.txt list. However, the code has an error. Try to fix the error.
```
temperatures = [10, 12, 14]
 
file = open("file.txt", 'w')
```
file.writelines(temperatures)