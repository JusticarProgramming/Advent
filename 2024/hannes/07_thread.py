# %%
from copy import copy
from multiprocessing import Pool


def parse_data(line):
    answer, values = line.strip().split(":")
    answer = int(answer)
    values = values.strip().split(" ")
    return [["+", "*", ""], answer, int(values[0]), values[1:]]


with open(f"data/07.txt", "r") as f:
    data = [parse_data(i) for i in f]


def is_valid(operators, answer, total, values):
    copied = copy(values)
    number = copied[0]
    del copied[0]

    for op in operators:
        if op == "+":
            new_total = total + int(number)

        if op == "*":
            new_total = total * int(number)

        if op == "":
            new_total = int(f"{total}{number}")

        # new_total = eval(f"{total}{op}{number}")
        if new_total > answer:
            continue

        if not copied:
            if new_total == answer:
                return True
            continue

        check = is_valid(operators, answer, new_total, copied)
        if check:
            return True

    return False


def solution(data):
    with Pool(processes=16) as pool:
        total = pool.starmap(is_valid, data)
        total = [data[i][1] for i, val in enumerate(total) if val]
        total = sum(total)
        return total


if __name__ == "__main__":
    dp2 = solution(data)
    print(f"{dp2=}")
    assert dp2 == 162987117690649
