import math
import random

# Task 1

# print(int(i) for i in range(7,100,7))
# не працює :(

print(*(list(range(7, 101, 7))), sep="; ")
print("     Next task")

# Task 2
summa = []
for count in range(1, 100):
    if count % 2:
        summa.append(count)
print(sum(summa))
print("     Next task")

# Task 3
printer = []
number_while = 0
while number_while < 200:
    number_while += 1
    printer.append(number_while)
    if number_while % 5 == 0:
        print(*printer)
        printer = []
print("     Next task")

# Task 4
n = int(input("input >>>"))
print(math.factorial(n))
print("     Next task")

# Task 5
n = 5
for i in range(11):
    print(f"{i} x {n} = {i * n}")
print("     Next task")

# Task 6
x = int(input("input x>>>"))
y = int(input("input y>>>"))
for i in range(1, y + 1):
    if i == 1 or i == y:
        print("*" * x)
    else:
        print("*" + " " * (x - 2) + "*")
print("     Next task")

# Task 7 ЦИФР!!!!!!!
odd = "13579"
count = 0
for i in [0, 5, 2, 4, 7, 1, 3, 19]:
    for digit in str(i):
        if digit in odd:
            count += 1
print(count)
print("     Next task")

# Task 8
was = [random.randint(1, 100) for item in range(10)]
now = was[:]
for item in was:
    now.append(item * 2)
print("old -->", was)
print("new -->", now)
print("     Next task")

# Task 9
payout = [random.randint(1000, 1500) for i in range(13)]
print(payout)
print(f"Середня зарплата == {int(sum(payout) / len(payout))}")
print("     Next task")

# Task 10
k = 0
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in matrix:
    print("|", *i, "|", sep=" ")
    k += sum(i)
print("sum ==", k)
print("     Next task")

# Task 11
task_11_list = [7, 2, 9, 4]
print(task_11_list, "-->", task_11_list[::-1])
print("     Next task")

# Task 12
prime_numbers = [1]
for i in range(2, 101):
    m = 2
    while m < i:
        if i % m == 0:
            break
        m += 1
    else:
        prime_numbers.append(i)
print(*prime_numbers)
print("     Next task")

# Task 13
sand_width = int(input("input sand clock width>>>"))
width = [sand_width]
while True:
    if sand_width % 2 == 0:
        sand_width -= 2
        width.append(sand_width)
    if sand_width % 2 != 0:
        sand_width -= 2
        width.append(sand_width)
    if sand_width == 1 or sand_width == 2:
        break
new_layer = 2
spaces = -1
while new_layer != 0:
    for i in width:
        if new_layer != 1:
            spaces += 1
        else:
            spaces -= 1
        print(" " * spaces + "*" * i + " " * spaces)
    new_layer -= 1
    width = width[:-1]
    width = width[::-1]
