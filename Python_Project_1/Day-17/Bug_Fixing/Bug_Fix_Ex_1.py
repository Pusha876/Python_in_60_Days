import FreeSimpleGUI as sg


def km_to_miles(kms):
    return kms / 1.60934


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")


window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            kilometers = float(values["kms"])
            result = km_to_miles(kilometers)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()
