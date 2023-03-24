password   = input("Enter  new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

result['digit'] = False

for i in password:
    if i.isdigit():
       result['digit'] = True
      

result['uppercase'] = False
for i in password:
    if i.isupper():
      result['uppercase'] = True
      break

if all(result.values()):
    print("Password is Strong")
else:
    print("Password is weak")