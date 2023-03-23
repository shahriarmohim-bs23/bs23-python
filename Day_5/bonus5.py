waiting_list = ["sen","ben","john"]
# waiting_list.sort()
# print(waiting_list)
waiting_list.sort(reverse=True)
print(waiting_list)

for index,item in enumerate(waiting_list):
    row =  f"{index + 1}.{item.capitalize()}"
    print(row)

