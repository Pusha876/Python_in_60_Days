# gui-configuration

```
while True:
    event, values = window.read(timeout=200)
    window["clock"].update9(value=time.strftime(%b %d, %Y %H:%M:%S"))



    except IndexError:
        sg.popup("Please select an item first.", font=("Helvetica", 20))


    case "Exit":
        break
    case 'todos':
        window['todo'].update(value=values['todos'][0])
    case sg.WIN_CLOSED:
        break
```
### (timeout=200)
The while loop run whenever an event happens unless you supply a timeout value. In that case the loop will run continuously every X (i.e., 200) milliseconds.

---
### .update9(value=time.strftime(%b %d, %Y %H:%M:%S"))
Whenever you want to update the value of a widget constantly, you can use the **update()** method in conjunction with the **timeout** argument explained in step 1.

---
###  except IndexError:
###      sg.popup("Please select an item first.", font=("Helvetica", 20))
If you expect an error, you should handle it with a try-except block and display a message to the user using a popup window.

---
###  case "Exit"
###     break
###  case sg.WIN_CLOSED:
###     break
The close-program functionality can be implemented both by handling the behavior of the X button and also by adding an *EXIT* button.

When the user presses one of those buttons we can break the while-loop with a **break** statement. Breaking the while-loop also breaks the program.