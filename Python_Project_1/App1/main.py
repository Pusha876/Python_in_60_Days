# This is a simple todo app that allows you to add, show and edit todos.

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

        case 'show':

            with open("todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item.title()}"
                print(row)
        case 'edit':
            number = int(input("Enter number of todo to edit: "))
            number = number - 1

            with open("todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter number of todo that was completed: "))

            with open("todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)

            message = f"The todo {todo_to_remove} was completed."
            print(message)

        case 'exit':
            break

print("Bye!")
