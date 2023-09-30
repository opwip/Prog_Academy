# Task 1
number = int(input(">>>"))
floors = 9
entrances = 4
apartments = 4
max_number = entrances * floors * apartments
ent = ((number - 1) // (floors * apartments)) + 1
floor = (number - (floors * apartments * (ent - 1)) - 1) // apartments + 1
number_on_floor = ((number - 1) - (floors * apartments * (ent - 1))) % apartments + 1
(0 < number <= max_number) and (print(
    f"{ent} entrance, {floor} floor, {number_on_floor} number. Just ignore the second message ") or True) or print(
    "There is no apartment under this number in this building")

# Task 2

year = int(input("year>>>"))

if not year % 4 and not year % 100 and year % 400:
    print("365")
elif not year % 400:
    print("366")
elif year % 4 == 0 and year % 100:
    print("366")
else:
    print("365")

# Task 3
a, b, c = int(input("a >>>")), int(input("b >>>")), int(input("c >>>"))
if a + b + c > 2 * max(a, b, c):
    print("Exists")
else:
    print("Doesnt exist")

# Task 1(additional)
password = str(input("Enter your password>>>"))
old_pass = "Claus123"
if password == old_pass:
    print("Доступ дозволено")
else:
    print("Доступ заборонено")

# Task 2(additional)
sum_of_buy = int(input("Sum of buy>>>"))
if sum_of_buy > 1000:
    total_sum = sum_of_buy - sum_of_buy * 0.1
    print(f"До сплати {total_sum}")
else:
    print(f"До сплати {sum_of_buy}")

# Task 3(additional)
months = [31, "28 or 29", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_number = int(input("Input month number in range from 1 to 12>>>"))
print(months[month_number - 1])

# Task 4(additional)
user_rating = int(input("Оцініть нас (від 1 до 5)>>>"))
if user_rating == 1:
    print("Жахливо")
elif user_rating == 2:
    print("Погано")
elif user_rating == 3:
    print("Задовільно")
elif user_rating == 4:
    print("Добре")
elif user_rating == 5:
    print("Відмінно")

# Task 5(additional)
mass, height = float(input("Input your weight(kg)>>>")), float(input("Input your height(m)>>>"))
VMI = mass / height ** 2
if VMI <= 18.5:
    print("Недостатньо ваги")
elif VMI <= 25:
    print("Нормальна вага")
elif VMI <= 30:
    print("Надлишкова вага")
elif VMI > 30:
    print("Ожиріння")
