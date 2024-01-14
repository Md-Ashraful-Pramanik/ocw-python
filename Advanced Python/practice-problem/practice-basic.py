# Website user management
# User => username, fathername, mothername, email, password (Sign up)
#      => email, password (Sign in)

users = []

# whether this email is in users list
def find_email(email):
    for user in users:
        if user['email'] == email:
            return True
    
    return False

# Handle sign up
def sign_up_user():
    user_name = input("Enter your name: ")
    father_name = input("Enter your father's name: ")
    mother_name = input("Enter your mother's name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    confim_password = input("Enter password again: ")

    # whether password is correct or not
    while password != confim_password:
        print("Password mismatch. Try again.")
        password = input("Enter password: ")
        confim_password = input("Enter password again: ")
    
    # whether email already in use
    while find_email(email):
        print("This email already exist. Try with another one.")
        email = input("Enter email: ")
    
    # Adding user into our user list
    users.append({
        "name": user_name,
        "father_name": father_name,
        "mother_name": mother_name,
        "email": email,
        "password": password,
    })
    # users.append([
    #     user_name, 
    #     father_name, 
    #     mother_name, 
    #     email, 
    #     password
    # ])

    print("User added successfully.")

# Handle sign in
def sign_in_user():
    email = input("Enter email: ")
    password = input("Enter password: ")

    found = False
    for user in users:
        if user['email'] == email and user['password'] == password:
            print(f"Name: {user['name']}, Father Name: {user['father_name']}, Mother Name: {user['mother_name']}")
            found = True
            break
    
    if not found:
        print("Email or password is wrong.")
    
# main program
def main():
    while True:
        choice = input("For sign up press 1\nFor sign in press 2\nFor exit press 0\nEnter your choice: ")
        if choice == '1':
            sign_up_user()
        elif choice == '2':
            sign_in_user()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again.")


main()
