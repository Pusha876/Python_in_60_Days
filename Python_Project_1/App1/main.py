# This is a simple todo app that allows you to add, show and edit todos.

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if 'add' in user_action or 'ADD' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open("todos.txt", "r", encoding="utf-8") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open("todos.txt", "r", encoding="utf-8") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item.title()}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)

        number = number - 1

        with open("todos.txt", "r", encoding="utf-8") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open("todos.txt", "r", encoding="utf-8") as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)

        message = f"The todo {todo_to_remove} was completed."
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Command not recognized")

print("Bye!")
