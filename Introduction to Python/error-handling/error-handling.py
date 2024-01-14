# Example-1: Error handling with try except
try:
    x = int(input("Enter an integer number: "))
    print(x ** 2)
except:
    print("Invalid entry. Please enter an integer.")

# Example-2: Error handling with try except else
try:
    x = int(input("Enter an integer number: "))
except:
    print("Invalid entry. Please enter an integer.")
else: 
    print(x ** 2)

# Example-3: Error handling with try except finally
try:
    x = float(input("Enter a number: "))
    print(100 / x)
except ValueError:
    print("Invalid entry. Please enter a number.")
except ZeroDivisionError:
    print("You can not enter 0 for division.")
except:
    print("There is an error. Enter correctly.")
finally: # always execute (normal or error in both case)
    print("In finally")

# Note
# finally: always execute (normal or error in both case)
# else: if there is no error
# except: if there is an error
# except ErrorName: if that particular error occurred

# Raising custom error
def get_full_name(first_name, last_name):
    if len(first_name) == 0:
        raise Exception("First name is empty")
    if len(last_name) == 0:
        raise Exception("Last name is empty")
    
    return f'{first_name} {last_name}'

print(get_full_name('Md.', 'Ashraful'))
print(get_full_name('', 'Ashraful'))
print(get_full_name('Md.', ''))

