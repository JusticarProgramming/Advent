# %%
from math import floor

test_rules = [
    [47, 53],
    [97, 13],
    [97, 61],
    [97, 47],
    [75, 29],
    [61, 13],
    [75, 53],
    [29, 13],
    [97, 29],
    [53, 29],
    [61, 53],
    [97, 53],
    [61, 29],
    [47, 13],
    [75, 47],
    [97, 75],
    [47, 61],
    [75, 61],
    [47, 29],
    [75, 13],
    [53, 13],
]

test_manuals = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]

data_rules = []
data_manuals = []

with open(f"../../scratch_4.txt", "r") as f:
    for l in f:
        if "|" in l:
            data_rules.append([int(i) for i in l.strip().split("|")])
        if "," in l:
            data_manuals.append([int(i) for i in l.strip().split(",")])


def part_1(rules, manuals):
    middel = []

    for manual in manuals:
        for before, after in rules:
            if not (before in manual and after in manual):
                continue

            i_before = manual.index(before)
            i_after = manual.index(after)

            if i_before > i_after:
                break
        else:
            number = manual[floor(len(manual) / 2)]
            middel.append(number)

    return sum(middel)


result = part_1(test_rules, test_manuals)
print(f"{result=}")
assert result == 143

result = part_1(data_rules, data_manuals)
print(f"{result=}")


def part_2(rules, manuals):
    middel = []

    for manual in manuals:
        for before, after in rules:
            if not (before in manual and after in manual):
                continue

            i_before = manual.index(before)
            i_after = manual.index(after)

            if i_before > i_after:
                break
        else:
            continue

        wrong = True
        while wrong:
            for before, after in rules:
                if not (before in manual and after in manual):
                    continue

                i_before = manual.index(before)
                i_after = manual.index(after)

                if i_before > i_after:
                    del manual[i_after]
                    manual.append(after)
                    break
            else:
                wrong = False

        number = manual[floor(len(manual) / 2)]
        middel.append(number)

    return sum(middel)


result = part_2(test_rules, test_manuals)
print(f"{result=}")
assert result == 123

result = part_2(data_rules, data_manuals)
print(f"{result=}")
