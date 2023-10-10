def parser(numbers: str) -> list:
    return list(map(int, numbers.split(",")))


def is_arithmetic_sequence(numbers: list) -> bool:
    # d2 = (((sum(numbers) * 2) / len(numbers)) - 2 * numbers[0]) / (len(numbers) - 1)
    d = numbers[2] - numbers[1]
    if numbers[0] + d == numbers[1] and numbers[0] + d*2 == numbers[2]:
        return True
    return False


def is_geometric_sequence(numbers: list) -> bool:
    q = numbers[2] / numbers[1]
    if numbers[0] * q == numbers[1] and numbers[0] * q**2 == numbers[2]:
        return True
    return False


def next_arithmetic_item(numbers: list) -> int:
    # d2 = (((sum(numbers) * 2) / len(numbers)) - 2 * numbers[0]) / (len(numbers) - 1)
    d = numbers[2] - numbers[1]
    return numbers[-1] + d


def next_geometric_item(numbers: list) -> int:
    q = (numbers[2] / numbers[1])
    return numbers[-1] * q


def get_next_item(numbers: list):
    if len(numbers) > 2:
        if is_arithmetic_sequence(numbers):
            print("Arithmetic")
            return next_arithmetic_item(numbers)

        if is_geometric_sequence(numbers):
            print("Geometric")
            return next_geometric_item(numbers)

    return None


if __name__ == '__main__':
    numbers = input('numbers>>>')
    print(parser(numbers))
    numbers = parser(numbers)
    print(get_next_item(numbers))
