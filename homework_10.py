# def func(item):
#     return f"{item}\n"
#
#
# with open("text.txt", "r", encoding="utf-8") as f:
#
#     "w"
#     x = ['1', '2', '3', '4']
#     x = [f'{item}\n' for item in x]
#     x = map(func, x)
#     f.write('Hello\n')
#     f.write('Python\n')
#     f.write('Python Pro\n')
#     f.writelines(x)
#
#     "r"
#     while data := f.read(1):
#         print(data)
#     data = f.readlines()
#     print(*data, sep="")
#     for line in f:
#         print(line.strip())
#     import timeit
#
#     stmp_1 = """
#     with open('test.txt', 'r', encoding='utf-8') as f:
#         data = f.readlines()
#         s = 0
#         for item in data:
#             s += int(item.strip())
#     """
#
#     stmp_2 = """
#     with open('test.txt', 'r', encoding='utf-8') as f:
#         s = 0
#         for item in f:
#             s += int(item.strip())
#     """
#
#     print(timeit.timeit(stmp_1, number=5))
#     print(timeit.timeit(stmp_2, number=5))