# Third-Party-Models

## libraries such as PySimpleGUI
are collections of Python **functions** and **types** which are can call and instantiate in our programs. To be able to use such objects, we need to install the library with "pip install library" and then import it.

```
import PySimpleGUI as sg

label = sg.text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()
```

### sg.text:
Once the library is imported, you need to refer to the library name or its variable representation (i.e., sg) to be able to use the library functions or types.

### window.read(), window.close():
Once an object instance is stored in a variable, the methods of that type of instance can be accessed (e.g., read() and close())

### = sg.text("Type in a to-do"), = sg.InputText(tooltip="Enter todo"), = sg.Button("Add"), = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
Libraries can offer many types. For example, the PySimpleGUI libray offers a window type, Text type, InputText type, Button type, etc. We use such types to create Windows, Text, InputText, Buttons and other instances. You can create as many instances as you want.