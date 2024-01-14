from pydantic import BaseModel, EmailStr, PositiveInt, field_validator

# IDE support
# Data validation, custom validation
# JSON serialization

class Person(BaseModel):
    name: str 
    email: EmailStr
    phone_number: str
    password: str
    salary: PositiveInt 

    @field_validator("password")
    def validate_password_2(cls, value):
        if len(value) >= 6:
            return value
        else:
            raise ValueError("Password should be 6 char long.")
        # assert len(value) >=6, "Password should be 6 char long."
        # return value

p = Person(
    name="Mr. X",
    email="abc@gmail.com",
    phone_number="01.....",
    password="abc16h",
    salary="30000"
)
print(p)

print(p.model_dump())
print(p.model_dump_json())

# JSON => JavaScript Object Notation

# Python, Javascript, Java, C, C#

# Python => JSON
# JS => 
# Java => JSON
# C => JSON
