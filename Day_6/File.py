def ReadFile():
    file = open("todos.txt","r")
    todos = file.readlines()
    file.close()
    return todos

def WriteFile(todos):
    file = open("todos.txt","w")
    file.writelines(todos)
    file.close()