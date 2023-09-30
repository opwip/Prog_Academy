# Execute the whole .py file to test all the codes at once. You will get number of next task after testing previous
task = 0
# Task 1
task += 1
print(f"Task {task}")
# Execute task partially in console from the next line
name = input("Input your name>>> ")
print("Hello,", name)

# Task 2
task += 1
print(f"Task {task}")
# Execute task partially in console from the next line
a1 = int(input("a1 = "))
a2 = int(input("a2 = "))
a3 = int(input("a3 = "))
a4 = int(input("a4 = "))
a5 = int(input("a5 = "))
print("max =", max(a1, a2, a3, a4, a5))
print("min =", min(a1, a2, a3, a4, a5))
print("arithmetic mean = ", (a1 + a2 + a3 + a4 + a5) / 5)

# Task 3
task += 1
print(f"Task {task}")
# Execute task partially in console from the next line
x = int(input("x = "))
y = int(input("y = "))
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)

# Task 4
task += 1
print(f"Task {task}")
# Execute task partially in console from the next line
radius = int(input("Circle radius>>> "))
print("Circle diameter =", radius * 2)
print("Circle length =", 2 * 3.14 * radius, "or", str(radius * 2) + "*pi")
print("Circle area =", 3.14 * radius ** 2, "or", str(radius ** 2) + "*pi")

# Task 5
task += 1
print(f"Task {task}")
# Execute task partially in console from the next line
p = 1000
r = 0.10
years = [10, 20, 30]
for n in years:
    a = p * ((1 + r) ** n)
    print(f"Your money after {n} years=", round(a))
# If p is an input
print("Input your own start money(If you dont want to input your own money on start, input 0)>>> ")
p_input = int(input())
if p_input != 0:
    for n in years:
        a = p_input * ((1 + r) ** n)
        print(f"Your money after {n} years=", round(a))
elif p_input == 0:
    print("Ok, skipping that one")

# Task 6
task += 1
print(f"Task {task}")
# Execute task partially in console from the next line
convert_mult_2004 = 5
dollars = float(input("dollars without '$' >>>"))
print(f"{dollars} dollars in hrywnas =", dollars * convert_mult_2004)

# Task 7
task += 1
print(f"Task {task}")
# Execute task partially in console from the next line
break_that_int = int(input())
break_that_int_str = str(break_that_int)
for i in break_that_int_str:
    print(i, sep="\n")

print("Code written by Kolesnik Yarolav date and time 22:29 6.09.2023")
