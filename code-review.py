name = input("Enter your name: ")

print("Hello", name)

password = input("Enter password: ")

if password == "1234":
    print("Login successful")
else:
    print("Wrong password")
    
    correct_password = input("Set password: ")

if password == correct_password: