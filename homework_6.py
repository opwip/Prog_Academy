import math

# Task 1
text = input(">>>")
print(text.count("b"))
print("     Next Task")

# Task 2
not_valid = "1234567890-+=@*&?/.,$#()%^:;{}[]<>,|"
name = input("Input a valid name>>>")
index = 0
p = 0
for item in name:
    if item in not_valid:
        break
    elif name[0].islower():
        break
    if index > 0 and str(item).isupper():
        break
    index += 1
else:
    print("Valid name")
print("     Next Task")

# Task 3
row = input(">>>")
i = 0
for item in row:
    i += ord(item)
print(i)
print("     Next Task")

# Task 4
for digits in range(2, 13):
    print(f"The value of pi is approximately {math.pi:.{digits}f}")
print("     Next Task")

# Task 5
text = input(">>>")
words = text.split(" ")
max_length = max(len(word) for word in words)
for word in words:
    if len(word) == max_length:
        print(word)
print("     Next Task")

# Task 6
text = input(">>>")
for length in range(1, len(text) + 1):
    if len(text) % length == 0 and text[:length] * (len(text) // length) == text:
        print(text[:length])
        break

# Task 7
HTML = input(">>>")
inside_tag = False
HTML_formatted = ""
for item in HTML:
    if item == "<" and not inside_tag:
        inside_tag = True
    elif item == ">" and inside_tag:
        inside_tag = False
    elif not inside_tag:
        HTML_formatted += item
print(HTML_formatted)
