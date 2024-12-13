# %%
test = [
    [8, 9, 0, 1, 0, 1, 2, 3,],
    [7, 8, 1, 2, 1, 8, 7, 4,],
    [8, 7, 4, 3, 0, 9, 6, 5,],
    [9, 6, 5, 4, 9, 8, 7, 4,],
    [4, 5, 6, 7, 8, 9, 0, 3,],
    [3, 2, 0, 1, 9, 0, 1, 2,],
    [0, 1, 3, 2, 9, 8, 0, 1,],
    [1, 0, 4, 5, 6, 7, 3, 2,],
]

data = []
with open(f"../../input_10.txt", "r") as f:
    for line in f:
        row = [int(i) for i in line.strip()]
        data.append(row)


def find_next(y_current, x_current, data):
    total = set()

    current = data[y_current][x_current]
    next = current + 1

    if current == 9:
        loc = (y_current, x_current)
        result = set()
        result.add(loc)
        return result

    if y_current >= 1:
        y_top, x_top = [y_current - 1, x_current]
        top = data[y_top][x_top]
        if top == next:
            total.update(find_next(y_top, x_top, data))

    if y_current <= len(data) - 2:
        y_bot, x_bot = [y_current + 1, x_current]
        bot = data[y_bot][x_bot]
        if bot == next:
            total.update(find_next(y_bot, x_bot, data))

    if x_current >= 1:
        y_left, x_left = [y_current, x_current - 1]
        left = data[y_left][x_left]
        if left == next:
            total.update(find_next(y_left, x_left, data))

    if x_current <= len(data[y_current]) - 2:
        y_right, x_right = [y_current, x_current + 1]
        right = data[y_right][x_right]
        if right == next:
            total.update(find_next(y_right, x_right, data))

    return total


def part_1(data):
    total = []

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == 0:
                total.append(find_next(y, x, data))

    lengths = [len(i) for i in total]
    sums = sum(lengths)
    return sums


tp1 = part_1(test)
print(f"{tp1=}")
assert tp1 == 36

dp1 = part_1(data)
print(f"{dp1=}")


def find_all(y_current, x_current, data):
    total = 0

    current = data[y_current][x_current]
    next = current + 1

    if current == 9:
        return 1

    if y_current >= 1:
        y_top, x_top = [y_current - 1, x_current]
        top = data[y_top][x_top]
        if top == next:
            total += find_all(y_top, x_top, data)

    if y_current <= len(data) - 2:
        y_bot, x_bot = [y_current + 1, x_current]
        bot = data[y_bot][x_bot]
        if bot == next:
            total += find_all(y_bot, x_bot, data)

    if x_current >= 1:
        y_left, x_left = [y_current, x_current - 1]
        left = data[y_left][x_left]
        if left == next:
            total += find_all(y_left, x_left, data)

    if x_current <= len(data[y_current]) - 2:
        y_right, x_right = [y_current, x_current + 1]
        right = data[y_right][x_right]
        if right == next:
            total += find_all(y_right, x_right, data)

    return total


def part_2(data):
    total = []

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == 0:
                total.append(find_all(y, x, data))

    lengths = [i for i in total]
    return sum(lengths)


tp2 = part_2(test)
print(f"{tp2=}")
assert tp2 == 81

dp2 = part_2(data)
print(f"{dp2=}")
