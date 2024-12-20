def get_todos(filepath="todos.txt"):
    """ Read the todos from the file and return them as a list. """
    with open(filepath, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the todos to the file. """
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("This is the functions module.")
    print("It is only intended to be used as a helper module.")
    print("To use the app, run main.py")
