# Task 1
if int(input(">>>")) < 20:
    print(True)
    print("x is < 20")
else:
    print(False)
    print("x is not < 20")

# Task 2
if int(input(">>>")) == 0:
    print(True)
    print("x is 0")
else:
    print(False)
    print("x is not 0")

# Task 3
if int(input(">>>")) % 2 == 0:
    print(True)
    print("x is even")
else:
    print(False)
    print("x is odd")

# Task 4
x, y, z = float(input(">>>")), float(input(">>>")), float(input(">>>"))
print("max is", max(x, y, z))
# Task 5
three_or_five = int(input(">>>"))
if three_or_five % 3 == 0 and not three_or_five % 5 == 0:
    print("Число підходить")
else:
    print("Число не підходить")
