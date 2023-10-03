# Task 1.1
text_1 = input(">>>")
text_unique_1 = set(text_1)
if len(text_unique_1) == len(text_1):
    print("It is unique")
else:
    print("It is not unique")
print("     Next Task")

# Task 1.2
text_2 = input(">>>")
text_unique_2 = set(text_2)
unique = 0
for item in text_unique_2:
    if text_2.count(item) == 1:
        unique += 1
print(unique)
print("     Next Task")

# Task 1.3
text_3 = {
    "key": "lama",
    "key2": "lamaa",
}
count = 0
text_unique_3 = set(text_3.values())
if len(text_unique_3) == len(text_3.values()):
    print("All of the values are unique")
else:
    print("Some or none of the values are unique")
print("     Next Task")

# Task 1.4
friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}
user_name1, user_name2 = input(">>>"), input(">>>")
if user_name1 not in friendships or user_name2 not in friendships:
    print("There is no such users")
elif friendships[user_name1] & friendships[user_name2]:
    print(friendships[user_name1] & friendships[user_name2], "- спільні друзі")
else:
    print("Немає спільних друзів")

# Task 1.5
row1, row2 = input(">>>"), input(">>>")
both_have = set(row1.split()).intersection(set(row2.split()))
print(max(both_have, key=len))


