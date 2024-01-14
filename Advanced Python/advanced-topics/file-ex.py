# create => write
# append => write
# read

# file path
# file absolute path
# file relative path

# w => if exist => replace, not exist => create
with open(file="test.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello")
    file.write("world3")


# a => if exist => append, not exist => create
with open(file="test.txt", mode="a", encoding="utf-8") as file:
    file.write("Hello")
    file.write("world4")

# read
with open(file="test.txt", mode="r", encoding="utf-8") as file:
    print(file.readlines())
