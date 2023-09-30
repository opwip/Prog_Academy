# Task 1
lucky_or_not = list(map(int, input('ticket=')))
if len(lucky_or_not) == 4:
    if lucky_or_not[0] + lucky_or_not[1] == lucky_or_not[2] + lucky_or_not[3]:
        print("Lucky")
    else:
        print("Unlucky")
else:
    print("Error, enter a valid ticket")

# Task 2
pldrom_or_not = list(map(int, input('6 digit number>>>')))
if len(pldrom_or_not) == 6:
    if pldrom_or_not == pldrom_or_not[::-1]:
        print("Polidrom")
else:
    print("Error, enter a 6 digit number")

# Task 3
r = 4
circle_center = [0, 0]
if (int(input("input x>>>")) - circle_center[0])**2 + (int(input("input y>>>")) - circle_center[1])**2 < r**2:
    print("belongs to the area of circle(inside the circle)")
elif (int(input("input x>>>")) - circle_center[0])**2 + (int(input("input y>>>")) - circle_center[1])**2 == r**2:
    print("belongs to the circle(on the circle)")
else:
    print("does not belong to the area of circle(outside the circle")
