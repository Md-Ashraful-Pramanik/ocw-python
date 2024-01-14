a = 'he\nllo'  # \  => back slash (escape), / forward slash
print(a)

a = "he\nllo"
print(a)

a = """he
llo"""
print(a)

a = '''hel\tlo'''
print(a)


a = 'let\'s go'
print(a)

a = 'let\"s go \\'
print(a)

# concatenation
a = 'hello'
c=' '
b = 'world'

print(a+c+b)

# formated string
print(f'{a} {b}')


name = "Md. Ashraful Islam"

print(f"Welcome! {name}")


welcomeText = "Welcome! {n}"

print(welcomeText.format(n=name))


a = "50"
print(a)
print(type(a))

b  =int(a)
print(b)
print(type(b))


a, b = "50", "6"

print(int(a)+int(b))

# Taking input as integer
# a = int(input())
# print(type(a))


print(float("5.46"))


# Searching in string
print("AshRaful" in name)
print("ashRaful".casefold() in name.casefold())

# Case changing
print("aBcD".lower())
print("aBcD".upper())
print("abcd".capitalize())
print("aBcD".swapcase())
print("aBcD".casefold())

# Length of a string
print(len(name))

# whitespace removal (newline, tab, space)
print("   \t\n abcd".lstrip())
print("abcd\n  \t".rstrip())
print("   \t\n abcd\n\t    ".strip())

# splitting text
print("aw br ct d faskdjksjag".split('a'))
print("""First
Second
3rd
4th""".splitlines())

# formatted string
x = 50
s = "first: {:.2f}, Secord: {:.0f}"

print(s.format(50.465465, 500))

s = "first: {1:.2f}, Secord: {0:.4f} {1}"
print(s.format(50.46546, 56, 465))

s = "His name is {0}. {0} is a Lecturer."
print(s.format("Md. Ashraful Islam"))