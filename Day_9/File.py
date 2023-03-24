def ReadFile():
    with open("../files/todos.txt","r") as file:#context manager
        todos = file.readlines()
        file.close()
        return todos

def WriteFile(todos):
    with open("../files/todos.txt","w") as file:
        file.writelines(todos)
        file.close()