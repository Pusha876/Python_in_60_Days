# function-arguments

```
def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath), todos_arg:
    with open(filepath, 'w') as file_local:
        file.writelines(todos_arg)

todos = get_todos("todos.txt")

```

### "todos.txt"
Argument value are assigned to arguments when the functions is called.

### (filepath):, (filepath, todos_arg):
Arguments are also known as parameters. They are local variables that get a value dynamically when the function is called.