from File import ReadFile,WriteFile
while True:
     user_action = input("Type add, show,edit,complete or exit:")
     user_action = user_action.strip()
     
     match user_action:
          case "add":
              input_todo = input("Enter a todo: ") + "\n"
              print(input_todo)
              todo_list = ReadFile()
              todo_list.append(input_todo)
              print(todo_list)
              WriteFile(todo_list)
              
          case "show" | "display":
               todo_list = ReadFile()
               [print(f"Todo_{i}:{todo.rstrip()}") for i,todo in enumerate(todo_list,1)]
          case "edit":
              todo_list = ReadFile()
              input_number = int(input("Number of todo to update: "))
              input_number = input_number-1
              new_todo = input("Enter new todo: ")
              print(todo_list)
              todo_list.__setitem__(input_number,new_todo) 
              WriteFile(todo_list)
          case "complete":
               todo_list = ReadFile()
               input_number = int(input("Number of todo to complete: "))
               todo_list.pop(input_number-1)
               WriteFile(todo_list)
          case "exit":
               break
          case _:
              print("Invalid action")           
print("Done")