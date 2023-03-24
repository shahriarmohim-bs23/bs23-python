from File import ReadFile,WriteFile
while True:
     user_action = input("Type add, show,edit,complete or exit:")
     user_action = user_action.strip()
     
     if 'add' in user_action or "new" in user_action:
         input_todo = user_action[4:] + "\n"
         todo_list = ReadFile()
         todo_list.append(input_todo)
         WriteFile(todo_list)            
              
     elif "show"  in user_action:
         todo_list = ReadFile()
         [print(f"Todo_{i}:{todo.rstrip()}") for i,todo in enumerate(todo_list,1)]
         
     elif "edit" in user_action:
         todo_list = ReadFile()
         input_number = int(user_action[5:])
         input_number = input_number-1
         new_todo = input("Enter new todo: ") + "\n"
         todo_list.__setitem__(input_number,new_todo) 
         WriteFile(todo_list)
    
     elif "complete" in user_action:
         todo_list = ReadFile()
         input_number = int(user_action[9:])
         try:
          todo_list.pop(input_number-1)
          WriteFile(todo_list)
         except IndexError:
          print("Invalid index")
        
     elif "exit" in user_action:
        break
    
     else:
        print("Invalid action")           
print("Done")