def ReadFile():
    with open(r"C:\Users\BS-865\Documents\bs23-python\files\todos.txt", "r") as file:
        todos = file.readlines()
        file.close()
        return todos


def WriteFile(todos):
    with open(r"C:\Users\BS-865\Documents\bs23-python\files\todos.txt","w") as file:
        file.writelines(todos)
        file.close()