# %%
from copy import copy

test_data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

data = []

with open(f"scratch_4.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        line = [int(i) for i in line]
        data.append(line)


def is_report_safe(report):
    direction = report[0] - report[1]

    for b, f in zip(report[1:], report[0:-1]):
        diff = f - b
        if abs(diff) > 3 or diff == 0:
            break

        if direction > 0 and diff < 0:
            break

        if direction < 0 and diff > 0:
            break
    else:
        return True

    return False


def part_1(reports):
    safe = 0

    for report in reports:
        if is_report_safe(report):
            safe += 1

    return safe


tp1 = part_1(test_data)
print(f"{tp1=}")
assert tp1 == 2

dp1 = part_1(data)
print(f"{dp1=}")


def part_2(reports):
    safe = 0

    for report in reports:
        if is_report_safe(report):
            safe += 1
            continue

        for i in range(len(report)):
            dup = copy(report)
            del dup[i]

            if is_report_safe(dup):
                safe += 1
                break

    return safe


tp2 = part_2(test_data)
print(f"{tp2=}")
assert tp2 == 4

dp2 = part_2(data)
print(f"{dp2=}")
