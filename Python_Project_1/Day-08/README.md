# with-context-manager

## The with-context manager is a helper to better handle file reading and writing.

### todos = file.readlines():
The file will be closed implicitly once all the indented lines have been executed.

### file:
This is the variable that will hold the file object. It is the equivalent of **file = open("todos-delete.txt", "w")**

```
with open("todos-delete.txt", "r") as file:
    todos = file.readlines()

with open("todos-delete.txt", "w") as file:
    todos = file.readlines()
```