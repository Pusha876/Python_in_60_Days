# List Comprehensions and Comments

## List comprehensions can create a new list by modifying an existing list.

```
new_todos = [item.strip('\n) for item in todos]
```

### item.strip('\n):
The first half of the comprehension contains the expression that creates the new items.

### for item in todos:
The second half contains the for-syntax.

### new_todos:
The new list will be stored in this variable.

### item  item:
This variable represents each item of the existing list.

### todos:
This variable holds the existing list whose items are used to create new items for the new list.