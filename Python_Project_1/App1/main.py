# This is a simple todo app that allows you to add, show and edit todos.

def get_todos():
    with open("todos.txt", "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + "\n")

        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)

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

            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)
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

            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

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
