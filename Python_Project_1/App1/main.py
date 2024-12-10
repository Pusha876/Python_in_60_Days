# This is a simple todo app that allows you to add, show and edit todos.

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r", encoding="utf-8")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w", encoding="utf-8")
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt", "r", encoding="utf-8")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.title()}"
                print(row)
        case 'edit':
            number = int(input("Enter number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter number of todo that was completed: "))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")
