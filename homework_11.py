def parser(numbers: str) -> list:
    return list(map(int, numbers.split(",")))


def is_arithmetic_sequence(numbers: list) -> bool:
    d = numbers[1] - numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != d:
            return False
    return True


def is_geometric_sequence(numbers: list) -> bool:
    if 0 in numbers:
        return False
    q = numbers[1] / numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i + 1] / numbers[i] != q:
            return False
    return True


def next_arithmetic_item(numbers: list) -> int:
    # d2 = (((sum(numbers) * 2) / len(numbers)) - 2 * numbers[0]) / (len(numbers) - 1)
    d = numbers[1] - numbers[0]
    return numbers[-1] + d


def next_geometric_item(numbers: list) -> int:
    q = numbers[1] / numbers[0]
    return numbers[-1] * q


def get_next_item(numbers: list):
    if len(numbers) >= 2:
        if is_arithmetic_sequence(numbers):
            return next_arithmetic_item(numbers)

        if is_geometric_sequence(numbers):
            return next_geometric_item(numbers)

        next_diff = get_next_item([numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)])
        if next_diff is not None:
            return numbers[-1] + next_diff
        if 0 in numbers:
            return None
        next_div = get_next_item([numbers[i + 1] / numbers[i] for i in range(len(numbers) - 1)])
        if next_div is not None:
            return numbers[-1] * next_div

    return None


if __name__ == '__main__':
    numbers = input('numbers>>>')
    print(parser(numbers))
    numbers = parser(numbers)
    print(get_next_item(numbers))
