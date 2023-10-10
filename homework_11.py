def parser(numbers: str) -> list:
    return list(map(int, numbers.split(",")))


def is_arithmetic_sequence(numbers: list) -> bool:
    # d2 = (((sum(numbers) * 2) / len(numbers)) - 2 * numbers[0]) / (len(numbers) - 1)
    d2 = numbers[2] - numbers[1]
    d1 = numbers[1] - numbers[0]
    if numbers[0] + (d1 + (d2 - d1) * 0) == numbers[1] and numbers[1] + (d1 + (d2 - d1) * 1) == numbers[2]:
        return True
    return False


def is_geometric_sequence(numbers: list) -> bool:
    q1 = numbers[1] / numbers[0]
    q2 = numbers[2] / numbers[1]
    q_next_g = q2 / q1
    print(q1)
    print(numbers[0] * (q1 * (q_next_g * 0)))
    print(numbers[1] * (q2 + (q_next_g * 1)))
    if numbers[0] * (q1 * (q_next_g ** 0)) == numbers[1] and numbers[1] * (q2 * (q_next_g ** 1)) == numbers[2]:
        return True
    return False


def next_arithmetic_item(numbers: list) -> int:
    # d2 = (((sum(numbers) * 2) / len(numbers)) - 2 * numbers[0]) / (len(numbers) - 1)
    d2 = numbers[2] - numbers[1]
    return numbers[-1] + (numbers[1] - numbers[0] + (d2 - (numbers[1] - numbers[0])) * (len(numbers) - 1))


def next_geometric_item(numbers: list) -> int:
    q2 = (numbers[2] / numbers[1])
    q1 = (numbers[1] / numbers[0])
    return numbers[-1] * (q1 * (q2 / q1)) ** (len(numbers) - 1)


def get_next_item(numbers: list):
    if len(numbers) > 2:
        if is_arithmetic_sequence(numbers):
            print("ok")
            return next_arithmetic_item(numbers)

        if is_geometric_sequence(numbers):
            print("nice")
            return next_geometric_item(numbers)

    return None


if __name__ == '__main__':
    numbers = input('numbers>>>')
    print(parser(numbers))
    numbers = parser(numbers)
    print(get_next_item(numbers))
    print(is_geometric_sequence([1, 3, 9, 27]))
