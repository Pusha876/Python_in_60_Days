# customer-functions

## Custom functions:
are instructions we write to perform a certain process.
```
def get_todos():
    with open('todos-delete.txt', 'r') as file_local
        todos_local = file_local.readlines()
    return todos_local
```

### with open:  return:
The instructions describe the process are written in the **function definition**. In this specific example, the instructions are:
1. Open the "todos-delete.txt" file.
1. Extract text from the text file and store the text in a list.
1. Return the list as the output of the function.

### = get_todos():
The instructions are executed by calling the function.

### todos:
The value returned by executing the instructions can be stored inn a variable.