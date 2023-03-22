todo_list = []
for i in range(3):
    user_input = input("Enter a todo:")
    todo_list.append(user_input)

i = 1
for todo in todo_list:
    print(f"Todo_{i}:",todo)
    i+=1


