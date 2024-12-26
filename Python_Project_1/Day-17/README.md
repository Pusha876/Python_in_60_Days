# desktop-gui

## Further exploring desktop GUIs, making the Todo List App interactive and visually engaging.

```
while True:
    event values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todos'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos"].update(value=todos)
```

### while True::
The while loop serves as a listener. It helps you listen for events happening in the program and watch the values of the widgets as they change.

### event:
The **event** variable holds the name or the key of the widget that was just clicked. The widget can be a button or some other clickable element.

### values:
The **values** variable holds a dictionary. The dictionary contains the current values entered or selected by the user in the widgets.

 ###     match event:
###        case "Add":
We can try to match the value of the **event** variable and perform different actions depending on what the current value of that variable is.

### window['todos"].update(value=todos):
Widgets can be accessed with **window['widget_key'] and their values can be updates using the **update()** method.