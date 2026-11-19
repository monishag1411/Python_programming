

username = input("Enter your username: ").strip()

if username == "":
    print("Invalid Username")
    print("Reason: Username cannot contain only spaces.")

elif len(username) < 5:
    print("Invalid Username")
    print("Reason: Username must contain at least 5 characters.")

elif username.lower() == "admin":
    print("Invalid Username")
    print("Reason: Username cannot be admin.")

else:
    print("Valid Username")
