# Task 1
text = input('text=')
text = text.split()
res = {}

for item in text:
    if item not in res:
        res[item] = text.count(item)
print(res)
print("     Next Task")

# Task 2
translations = {
    'hello': 'привіт',
    'goodbye': 'до побачення',
    'cat': 'кіт',
    'dog': 'собака'
}
word = input(">>>")
if word in translations:
    print(word + " --> " + translations[word])
else:
    translations[word] = input("Слова немає в словнику введіть переклад")
    print(word + " --> " + translations[word])
print("     Next Task")

# Task 3
contacts = {}
i = "working"
while True:
    contact = input("contact name(to quit input stop )>>>")
    if contact == "stop":
        break
    if contact in contacts:
        print(contacts[contact])
    else:
        contacts[contact] = (input("Input phone number>>>"))
print(contacts)
print("     Next Task")

# Task 4
# Курси обміну уявні
converter = {
    "to USD": 0.2,
    "to Euro": 0.3,
    "to Pounds": 0.5
}
grywnas = int(input("Input value in grywnas>>>"))
for value in converter:
    print(f"Grywnas {value} == {grywnas*converter[value]}")

