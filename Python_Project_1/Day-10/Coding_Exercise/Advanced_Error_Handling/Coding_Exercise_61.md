### Advanced Error Handling
As you might know, it is not mathematically possible to divide a number by zero. Consequently, this is also not possible in Python either -you will get a ```ZeroDivisionError``` if you try:
```
>>> 20 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

With that in mind, your task for this exercise is to extend the program you created in Exercise 1 by displaying a message to the user when they enter 0 for the "total value".
```
Enter total value: 0
Enter value: 20
Your total value cannot be zero.