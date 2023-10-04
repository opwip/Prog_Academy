def category_money(family_data: dict) -> dict:
    """
    Returns dict with key = category, value = money spent on category

    :param family_data: data extracted from .txt
    :return: dict{key = category : value = money spent on that category}
    """
    categories_money_dict = {}
    # Find all the categories
    for values in family_data.values():
        if values[-1] not in categories_money_dict:
            categories_money_dict[values[-1]] = 0
    # Find sum of spent money for all the categories
    for key in categories_money_dict:
        for values in family_data.values():
            if values[-1] == key:
                minus_dollar = values[-2]
                minus_dollar = minus_dollar.strip('$')
                categories_money_dict[key] += float(minus_dollar)
        categories_money_dict[key] = f"{categories_money_dict[key]:.2f}$"
    return categories_money_dict


with open("hw_10_test.txt", "r", encoding="utf-8") as file:
    data = {}
    for item in file:
        line = item.split()
        transaction_id, *name, money, category = line
        data[transaction_id] = (' '.join(name)), money, category
    print(category_money(data))
