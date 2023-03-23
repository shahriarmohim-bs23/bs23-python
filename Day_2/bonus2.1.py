import os 
user_email = os.environ.get('email')
user_password = os.environ.get('password')
print(user_email, user_password)
while True:
    input_email = input("Enter email: ")
    input_password = input("Enter password: ")
    if input_email == user_email and input_password == user_password:
       print("Email and password are correct")
       break
    else:
        print("Email and password are incorrect")