file_path = "todos.txt"

def get_todos(file_path=file_path):

    with open(file_path, 'r') as file:
        todos = file.readlines()
        return todos

def write_todos(todos_arg, file_path=file_path):

    with open(file_path, 'w') as file:
        file.writelines(todos_arg)