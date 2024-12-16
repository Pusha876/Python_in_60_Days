# if, elif, else, dictionaries

### if-elif-else can be used to check multiple conditions. Conditions are expressions that evaluate to either True or False.
```
if 'add' in user_action:
    todo = user_action[4:]

elif 'show' in user_action:
    with open('todos-delete.txt', 'r') as file:
        todos = file.readlines()

else:
    print("Command is not valid.")
```
**'add' in user_action** - The interpreter always checks the conditions of the if-line first.

**'show' in user_action:** - If the condition of the if-line **does not** evaluate to True. The interpreter goes to check the condition of the elif-line.

**print("Command is not valid.")** - If all conditions under the if-lines and the elif-lines are False. The interpreter executes the code indented under the else-line.