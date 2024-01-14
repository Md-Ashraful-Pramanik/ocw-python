# relational operator
# conditional statement
mark = 20
if mark >= 33:
    print("Passed")

# mark => Grade (0-32 F), 
#               (33-49 D), 
#               (50-59 C), 
#               (60-69 B), 
#               (70-79 A), 
#               (80-100 A+)

mark = 45
# nested if
if mark > 100:
    print("Input correctly")
else:
    if mark >= 80:
        print("A+")
    else:
        if mark >= 70:
            print("A")
        else:
            if mark >= 60:
                print("B")
            else:
                if mark >= 50:
                    print("C")
                else:
                    if mark >= 33:
                        print("D")
                    else:
                        if mark >= 0:
                            print("F")
                        else:
                            print("Input correctly")

# dependent if .. else .. if
if mark > 100:
    print("Input correctly")
elif mark >= 80:
    print("A+")
elif mark >= 70:
    print("A")
elif mark >= 60:
    print("B")
elif mark >= 50:
    print("C")
elif mark >= 33:
    print("D")
elif mark >= 0:
    print("F")
else:
    print("Input correctly")

# Fully independent
if mark >=0 and mark <=32:
    print("F")
if mark >= 33 and mark <= 49:
    print("D")
if mark >= 50 and mark <= 59:
    print("C")
if mark >= 60 and mark <= 69:
    print("B")
if mark >= 70 and mark <= 79:
    print("A")
if mark >= 80 and mark <= 100:
    print("A+")
if mark < 0 or mark > 100:
    print("Enter correctly")

# short hand if-else
result = "passed" if mark >= 33 else "failed"

print(result)

# pass statement
a = 10
b = 10

if a>b:
    print("a is larger")
elif a<b:
    pass
else:
    print("They are equal")

# Exercise: year input => leap year?
# divisible by 400 => leap year
# divisible by 100 => not leap year
# divisible by 4 => leap year

year = int(input())

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not Leap year")
elif year % 4 == 0: 
    print("Leap year")
else:
    print("Not Leap year")


if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("Leap year")
else:
    print("Not Leap year")