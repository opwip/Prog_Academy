# Task 1
def category_money(data) -> dict:
    family_data = {}
    with open(data, "r", encoding="utf-8") as file:
        for item in file:
            line = item.split()
            transaction_id, *name, money, category = line
            family_data[transaction_id] = (' '.join(name)), money, category
    categories_money_dict = {}
    for values in family_data.values():
        if values[-1] not in categories_money_dict:
            categories_money_dict[values[-1]] = 0
    for key in categories_money_dict:
        for values in family_data.values():
            if values[-1] == key:
                minus_dollar = values[-2]
                minus_dollar = minus_dollar.strip('$')
                categories_money_dict[key] += float(minus_dollar)
        categories_money_dict[key] = f"{categories_money_dict[key]:.2f}$"
    return categories_money_dict


# Task 2
def name_money(data) -> dict:
    with open(data, "r", encoding="utf-8") as file:
        family_data = {}
        for item in file:
            line = item.split()
            transaction_id, *name, money, category = line
            family_data[transaction_id] = (' '.join(name)), money, category
    name_money_dict = {}
    for values in family_data.values():
        if values[-3] not in name_money_dict:
            name_money_dict[values[-3]] = 0
    for key in name_money_dict:
        for values in family_data.values():
            if values[-3] == key:
                minus_dollar = values[-2]
                minus_dollar = minus_dollar.strip('$')
                name_money_dict[key] += float(minus_dollar)
        name_money_dict[key] = f"{name_money_dict[key]:.2f}$"
    return name_money_dict


def count_total(data: str, name_req: str) -> str:
    with open(data, "r", encoding="utf-8") as file:
        family_data = {}
        for item in file:
            line = item.split()
            transaction_id, *name, money, category = line
            family_data[transaction_id] = (' '.join(name)), money, category
    name_count_dict = {}
    for values in family_data.values():
        if values[-3] not in name_count_dict:
            name_count_dict[values[-3]] = 0
    for key in name_count_dict:
        count = 0
        for values in family_data.values():
            if values[-3] == key:
                count += 1
        name_count_dict[key] = count
    return f"{name_req} -> {name_count_dict[name_req]}" if name_req in name_count_dict.keys() else "Error"


print(category_money("hw_10_test.txt"))
print(name_money("hw_10_test.txt"))
print(count_total("hw_10_test.txt", input("name>>>")))
