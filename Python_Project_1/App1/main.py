# This is a simple todo app that allows you to add, show and edit todos.

def get_todos(filepath="todos.txt"):
    """ Read the todos from the file and return them as a list. """
    with open(filepath, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the todos to the file. """
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)


text = """
Welcome to the todo app.
Type add to add a new todo.
Type show to show all todos.
Type edit to edit a todo.
Type complete to complete a todo.
Type exit to exit the app.
"""

print(text)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            message = f"The todo {todo_to_remove} was completed."
            print(message)
        except IndexError:
            print("The todo you are trying to complete does not exist.")
            continue
        except ValueError:
            print("Your command is not valid.")

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not recognized")

print("Bye!")
