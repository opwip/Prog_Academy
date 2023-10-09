# Task 1
def category_money(data) -> dict:
    total_cost = {}
    with open(data, "r", encoding="utf-8") as file:
        for line in file:
            transaction_id, *name, money, category = line.split()
            if category in total_cost:
                total_cost[category] += float(money.strip("$"))
            else:
                total_cost[category] = float(money.strip("$"))
    for key, value in total_cost.items():
        total_cost[key] = f"{value:.2f}$"
    return total_cost


# Task 2
def name_money(data) -> dict:
    total_cost = {}
    with open(data, "r", encoding="utf-8") as file:
        for line in file:
            transaction_id, *name, money, category = line.split()
            if category in total_cost:
                total_cost[(' '.join(name))] += float(money.strip("$"))
            else:
                total_cost[(' '.join(name))] = float(money.strip("$"))
    for key, value in total_cost.items():
        total_cost[key] = f"{value:.2f}$"
    return total_cost


def count_total(data: str, name_req: str) -> int:
    count = 0
    with open(data, "r", encoding="utf-8") as file:
        for line in file:
            transaction_id, *name, money, category = line.split()
            if name_req == (' '.join(name)):
                count += 1
    return count


print(category_money("hw_10_test.txt"))
print(name_money("hw_10_test.txt"))
print(count_total("hw_10_test.txt", input("name>>>")))
