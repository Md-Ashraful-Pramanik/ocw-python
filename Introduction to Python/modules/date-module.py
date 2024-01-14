import datetime

# Seeing today's date and time
today = datetime.datetime.now()
print(today.strftime("%d %B %y, %I:%M:%S %p"))

# Building a date object
my_birth_date = datetime.datetime(2010, 9, 26)
print(my_birth_date.strftime("%d %B %y, %I:%M:%S %p"))

# Finding the difference between two dates
print((today-my_birth_date).days/365)
