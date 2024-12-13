# %%
test = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]

with open(f"data/04.txt", "r") as f:
    data = [l.strip() for l in f]

match = "XMAS"


def part_1(data):
    total = 0

    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if not c == match[0]:
                continue

            for y_mod in [-1, 0, 1]:
                for x_mod in [-1, 0, 1]:
                    y_loc = y + y_mod
                    x_loc = x + x_mod

                    if y_loc < 0 or y_loc >= len(data):
                        continue

                    if x_loc < 0 or x_loc >= len(row):
                        continue

                    comp = data[y_loc][x_loc]

                    if not comp == match[1]:
                        continue

                    direction = (y_mod, x_mod)

                    step = 2
                    y_dir, x_dir = direction

                    while step < len(match):
                        lookup = match[step]

                        y_loc = y + (y_dir * step)
                        x_loc = x + (x_dir * step)

                        if y_loc < 0 or y_loc >= len(data):
                            break

                        if x_loc < 0 or x_loc >= len(row):
                            break

                        character = data[y_loc][x_loc]

                        if lookup == character:
                            step += 1
                            if step == len(match):
                                total += 1
                        else:
                            break

    return total


result = part_1(test)
print(f"{result=}")
assert result == 18

result = part_1(data)
print(f"{result=}")


def part_2(data):
    total = 0

    for y, row in enumerate(data[1:-1]):
        for x, c in enumerate(row[1:-1]):
            if not c == "A":
                continue

            neighbours = f"{data[y][x]}{data[y][x + 2]}{data[y + 2][x]}{data[y + 2][x + 2]}"

            if neighbours in [
                "MMSS", "MSMS", "SSMM", "SMSM"
            ]:
                total += 1

    return total


result = part_2(test)
print(f"{result=}")
assert result == 9

result = part_2(data)
print(f"{result=}")
