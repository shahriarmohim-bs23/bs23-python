try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))
    if width ==length:
       exit("That looks like a square")
    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")

multi_line_string = """
My Name is Mohim.
I am currently working as a Software Engineer Trainee in Brain Station-23.
"""
print(multi_line_string)