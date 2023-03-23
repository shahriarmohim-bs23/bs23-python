
todo_list = []
while True:
     user_action = input("Type add, show,edit,complete or exit:")
     user_action = user_action.strip()
     
     match user_action:
          case "add":
              input_todo = input("Enter a todo: ")
              todo_list.append(input_todo)
          case "show" | "display":
               [print(f"Todo_{i}:{todo.title()}") for i,todo in enumerate(todo_list,1)]
          case "edit":
              input_number = int(input("Number of todo to update: "))
              input_number = input_number-1
              new_todo = input("Enter new todo: ")
              todo_list.__setitem__(input_number,new_todo) 
          case "complete":
               input_number = int(input("Number of todo to complete: "))
               todo_list.pop(input_number-1)
          case "exit":
               break
          case _:
              print("Invalid action")           
print("Done")