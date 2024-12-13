# %%
from collections import defaultdict
from dataclasses import dataclass
from copy import copy


@dataclass
class Plot():
    letter: str
    members: int
    fences: int

    def cost(self):
        return self.members * self.fences


test_1 = [
    "AAAA",
    "BBCD",
    "BBCC",
    "EEEC",
]

test_2 = [
    "OOOOO",
    "OXOXO",
    "OOOOO",
    "OXOXO",
    "OOOOO",
]

test_3 = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",
]

with open(f"../vicus/input_12.txt", "r") as f:
    data = f.readlines()


def prep_data(data: list[str]):
    locations = defaultdict(lambda: None)
    for y, row in enumerate(data):
        row: str = row.strip()
        for x, col in enumerate(row):
            locations[(y, x)] = col

    return locations


def assign_letter(
    data: defaultdict,
    letter: str,
    loc: tuple,
    assigned: set,
    unique_plots: list,
    plot: Plot = None,
):
    assigned.add(loc)
    y, x = loc

    neighbours = []
    neighbours_locations = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for (y_mod, x_mod) in neighbours_locations:
        n_y, n_x = (y + y_mod, x + x_mod)
        n_letter = data[(n_y, n_x)]

        if n_letter == letter:
            neighbours.append((n_y, n_x))

    if plot:
        plot.members += 1
        plot.fences += 4 - len(neighbours)
    else:
        plot = Plot(letter=letter, members=1, fences=(4 - len(neighbours)))
        unique_plots.append(plot)

    for neighbour in neighbours:
        if neighbour in assigned:
            continue

        assign_letter(data, letter, neighbour, assigned, unique_plots, plot)


def part_1(data: defaultdict):
    assigned = set()
    unique_plots: list[Plot] = []

    itterator = data.copy()
    for loc, letter in itterator.items():

        if loc in assigned:
            continue

        assign_letter(data, letter, loc, assigned, unique_plots)

    total = 0
    for plot in unique_plots:
        total += plot.cost()

    return total


result_1 = prep_data(test_1)
result_2 = prep_data(test_2)
result_3 = prep_data(test_3)

tp1_1 = part_1(result_1)
print(f"{tp1_1=}")
assert tp1_1 == 140

tp1_2 = part_1(result_2)
print(f"{tp1_2=}")
assert tp1_2 == 772

tp1_3 = part_1(result_3)
print(f"{tp1_3=}")
assert tp1_3 == 1930

result_data = prep_data(data)

dp1 = part_1(result_data)
print(f"{dp1=}")
# assert dp1 == 1546338


def assign_corner(
    data: defaultdict,
    letter: str,
    loc: tuple,
    assigned: set,
    unique_plots: list,
    plot: Plot = None,
):
    assigned.add(loc)
    y, x = loc

    vertical_neighbors = 0
    horizontal_neighbors = 0
    diagonal_neighbors = 0

    neighbours_locations = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for (y_mod, x_mod) in neighbours_locations:
        n_y, n_x = (y + y_mod, x + x_mod)
        n_letter = data[(n_y, n_x)]

        if n_letter == letter:
            if y_mod == 0:
                horizontal_neighbors += 1
            else:
                vertical_neighbors += 1

    diagonal_locations = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    for (y_mod, x_mod) in diagonal_locations:
        n_y, n_x = (y + y_mod, x + x_mod)
        n_letter = data[(n_y, n_x)]

        if n_letter == letter:
            diagonal_neighbors += 1

    corners = 4 - (vertical_neighbors * 2) - (horizontal_neighbors * 2) + diagonal_neighbors

    if plot:
        plot.members += 1
        plot.fences += corners
    else:
        plot = Plot(letter, 1, corners)
        unique_plots.append(plot)

    for (y_mod, x_mod) in neighbours_locations:
        n_y, n_x = (y + y_mod, x + x_mod)
        if (n_y, n_x) not in assigned and data[(n_y, n_x)] == letter:
            assign_corner(data, letter, (n_y, n_x), assigned, unique_plots, plot)


def part_2(data: defaultdict):
    assigned = set()
    unique_plots: list[Plot] = []

    itterator = copy(data)
    for loc, letter in itterator.items():

        if loc in assigned:
            continue

        assign_corner(data, letter, loc, assigned, unique_plots)

    total = 0
    for plot in unique_plots:
        total += plot.cost()

    return total


result_1 = prep_data(test_1)
result_2 = prep_data(test_2)

tp2_1 = part_2(result_1)
print(f"{tp2_1=}")
assert tp2_1 == 80

tp2_2 = part_2(result_2)
print(f"{tp2_2=}")
assert tp2_2 == 436

test_3 = [
    "EEEEE",
    "EXXXX",
    "EEEEE",
    "EXXXX",
    "EEEEE",
]

result_3 = prep_data(test_3)

tp2_3 = part_2(result_3)
print(f"{tp2_3=}")
assert tp2_3 == 236

test_4 = [
    "AAAAAA",
    "AAABBA",
    "AAABBA",
    "ABBAAA",
    "ABBAAA",
    "AAAAAA",
]

result_4 = prep_data(test_4)

tp2_4 = part_2(result_4)
print(f"{tp2_4=}")
# assert tp2_4 == 368


test_5 = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",
]

result_5 = prep_data(test_5)

tp2_5 = part_2(result_5)
print(f"{tp2_5=}")
assert tp2_5 == 1206

result_data = prep_data(data)

dp2 = part_2(result_data)
print(f"{dp2=}")
