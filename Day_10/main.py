import sys
sys.path.insert(1, "C:/Users/BS-865/Documents/bs23-python/Day_9")

from File import ReadFile, WriteFile
while True:
     user_action = input("Type add, show,edit,complete or exit:")
     user_action = user_action.strip()
     
     if user_action.startswith("add"):
        try:
            input_todo = user_action[4:] + "\n"
            todo_list = ReadFile()
            todo_list.append(input_todo)
            WriteFile(todo_list) 
        except ValueError:
            print("Your Command is not  valid")           
              
     elif  user_action.startswith("show"):
         todo_list = ReadFile()
         [print(f"Todo_{i}:{todo.rstrip()}") for i,todo in enumerate(todo_list,1)]
         
     elif  user_action.startswith("edit"):
         try:
            todo_list = ReadFile()
            input_number = int(user_action[5:])
            input_number = input_number-1
            new_todo = input("Enter new todo: ") + "\n"
            todo_list.__setitem__(input_number,new_todo) 
            WriteFile(todo_list)
         except ValueError:
            print("Your Command is not  valid")
    
     elif user_action.startswith("complete"):
         try:
            todo_list = ReadFile()
            input_number = int(user_action[9:])
            try:
                todo_list.pop(input_number-1)
                WriteFile(todo_list)
            except IndexError:
                print("Invalid index")
         except ValueError:
            print("Your Command is not  valid")

     elif user_action.startswith("exit"):
        break
    
     else:
        print("Invalid action")           
print("Done")