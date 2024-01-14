# Website user management
# User => username, fathername, mothername, email, password (Sign up)
#      => email, password (Sign in)
from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    father_name: str 
    mother_name: str 
    email: EmailStr
    password: str 

    @field_validator("password")
    def validate_password_2(cls, value):
        if len(value) >= 6:
            return value
        else:
            raise ValueError("Password should be 6 char long.")

    def __str__(self):
        return f"Name: {self.name}, Father Name: {self.father_name}, Mother Name: {self.mother_name}, Email: {self.email}"


class UserController:
    def __init__(self):
        self.users = []
    
    # whether this email is in users list
    def find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    # Handle sign up
    def sign_up_user(self):
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
        while self.find_user_by_email(email) is not None:
            print("This email already exist. Try with another one.")
            email = input("Enter email: ")
        
        # Adding user into our user list
        self.users.append(User(
            name=user_name,
            father_name=father_name,
            mother_name=mother_name,
            email=email,
            password=password
        ))

        print("User added successfully.")

    # Handle sign in
    def sign_in_user(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        user = self.find_user_by_email(email=email)

        if user is None:
            print("Can not find your Email")
        elif user.password != password:
            print("Password mismatch")
        else:
            print(user)
    
# main program
def main():
    controller = UserController()
    while True:
        choice = input("For sign up press 1\nFor sign in press 2\nFor exit press 0\nEnter your choice: ")
        if choice == '1':
            controller.sign_up_user()
        elif choice == '2':
            controller.sign_in_user()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again.")


main()
