import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo here")
add_button = sg.Button("add")

window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
