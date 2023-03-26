def ReadFile():
    with open(r"C:\Users\BS-865\Documents\bs23-python\files\todos.txt", "r") as file:
        todos = file.readlines()
        file.close()
    """_This is a function for reading the file and the file path to an absolute path that points directly to the file location.and return a list which contains file's contents_

    Returns:
        _type_: _list_
    """
        return todos


def WriteFile(todos):
    with open(r"C:\Users\BS-865\Documents\bs23-python\files\todos.txt","w") as file:
        file.writelines(todos)
        file.close()


print("Hello from function")