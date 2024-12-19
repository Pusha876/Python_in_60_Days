# default-arguments

## Non-default arguments:
should be listed first (i.e., todos_arg), then the default argument (i.e., filepath).

```
def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


write_todos(todos)
```

### Default arguments: filepath="todos.txt"
are arguments which are given a value in the function definition.

### Default arguments: (todos)
don't have to be included in the function call unless you want to change their default value.

### Doc strings: """ Write the to-do items list in the text file."""
are triple-quote strings defined in the function definition. They are shown as help documentation when help(function) is used.