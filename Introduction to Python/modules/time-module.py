import time
import random

# Calculating elapsed time for generating 8000 random passwords
start_time = time.time()

char_list = char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#%&'

for i in range(100):
    random_password = ''
    for i in range(8000):
        random_password = random_password + random.choice(char_list)

end_time = time.time()
print(f'Elapsed Time in average: {((end_time-start_time)*1000) / 100:.2f} ms')


# Experiment on time taken by for loop and map
# The following code snippet generates 1000000 random names and 
# calculates the length of each name using for loop and map. 
# The time taken by both the methods are compared.

## random name generator
def get_random_name():
    char_list = char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    random_name = ''
    for i in range(random.randint(5, 20)):
        random_name = random_name + random.choice(char_list)
    return random_name

## generating random name
names = []
for i in range(1000000):
    names.append(get_random_name())

## for loop to calculate length of each name
start_time = time.time()
name_lengths = []
for name in names:
    name_lengths.append(len(name))
end_time = time.time()
print(f'Elapsed Time (for): {((end_time-start_time)*1000):.2f} ms')

## map to calculate length of each name
start_time = time.time()
name_lengths = list(map(len, names))
end_time = time.time()
print(f'Elapsed Time (map): {((end_time-start_time)*1000):.2f} ms')

