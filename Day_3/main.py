todo_list = []
while True:
     user_action = input("Type add, show, or exit:")
     user_action = user_action.strip()
     
     match user_action:
          case "add":
              input_todo = input("Enter a todo: ")
              todo_list.append(input_todo)
          case "show" | "display":
               [print(f"Todo_{i}:{todo.title()}") for i,todo in enumerate(todo_list,1)]
          case "exit":
               break
          case _:
              print("Invalid action") 
              
print("Done")