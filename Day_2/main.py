user_prompt = "Enter a todo:"
todo_list = []

while True:
    try:
        input_todo = input(user_prompt)
        print(input_todo.capitalize())
        print(input_todo.title())
        todo_list.append(input_todo)
    except KeyboardInterrupt:
        break
    
     
    

