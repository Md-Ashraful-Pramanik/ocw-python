import random

# Using random seed we can control random generation
random.seed(4)

# Random number generation between 0 and 1 (not including 1) 
print(random.random())

# Random number generation between 1 and 6 (including 1 and 6)
print(random.randint(1, 6))

# Shuffle a list randomly => changing order
a = [5, 6, 7, 9, 3]
random.shuffle(a)
print(a)

# Taking one element from a list randomly
print(random.choice(a))

# Making random password
char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#%&'

random_password = ''
for i in range(8):
    random_password = random_password + random.choice(char_list)

print(random_password)