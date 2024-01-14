# Initialization
l = [1, 2, 3] # list
t = (1, 2, 3) # tuple
s = {1, 2, 3} # set
d = {"first": 1, "second":2, "third": 3} # dictionary

print(l)
print(t)
print(s)
print(d)

# Access element
print(l[1])
print(t[1])
print(d["second"])
# no method for set 

# check whether an element exist
print(5 in l)
print(1 in t)
print(1 in s)
print(1 in d) # for dictionary "in" will search for key
print("first" in d)

# length 
print(len(l))
print(len(t))
print(len(s))
print(len(d))

# copy
print(l.copy())
print(d.copy())
print(s.copy())
# print(t.copy()) # because not changeable 

# clear
# l.clear()
# d.clear()
# s.clear()
# t.clear()  # because not changeable 

print(l)
print(t)
print(s)
print(d)

# removing element
l.remove(2)
print(l)
# l.remove(2)
del l[1]
# del l[1]
s.remove(2)
d.pop("first")
# del d['first']

# Adding element
# l.append(50)
l.insert(1, 500)
s.add(50)
# d["fourth"] = 500
d.update({"third": 50000, "fourth": 50})

print(l)
print(s)
print(d)