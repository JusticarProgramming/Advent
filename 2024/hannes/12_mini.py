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


@dataclass
class Vector():
    y: int
    x: int

    def is_diagonal(self, other: "Vector"):
        result = Vector(y=self.y - other.y, x=self.x - other.x)
        orientation = result.x * result.y

        if orientation == 0:
            return False

        return True

    @property
    def loc(self):
        return (self.y, self.x)

    def __eq__(self, other: "Vector") -> bool:
        if self.y == other.y and self.x == other.x:
            return True

        return False


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

with open(f"data/12.txt", "r") as f:
    data = f.readlines()


def prep_data(data: list[str]):
    locations = defaultdict(lambda: None)
    for y, row in enumerate(data):
        row: str = row.strip()
        for x, col in enumerate(row):
            locations[(y, x)] = col

    return locations


def get_neighbours(data: dict, letter: str, vector: Vector) -> list[Vector]:
    result = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for (y_mod, x_mod) in directions:
        neighbour = Vector(y=vector.y + y_mod, x=vector.x + x_mod)
        n_letter = data[(neighbour.loc)]

        if n_letter == letter:
            result.append((neighbour))

    return result


def get_diagonals(data: dict, letter: str, vector: Vector) -> list[Vector]:
    result = []

    directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
    for (y_mod, x_mod) in directions:
        neighbour = Vector(y=vector.y + y_mod, x=vector.x + x_mod)
        n_letter = data[(neighbour.loc)]

        if n_letter == letter:
            result.append((neighbour))

    return result


def shares_neighbours(data: dict, letter: str, vector_a: Vector, vector_b: Vector) -> bool:
    neighbours_a = get_neighbours(data, letter, vector_a)
    neighbours_b = get_neighbours(data, letter, vector_b)

    shared = [True for i in neighbours_a if i in neighbours_b]
    return len(shared)


def assign_corner(
        data: defaultdict,
        letter: str,
        current: Vector,
        assigned: set,
        unique_plots: list,
        plot: Plot = None,
):
    assigned.add(current.loc)

    corners = 4

    state: list[Vector] = []
    neighbours = get_neighbours(data, letter, current)
    for neighbour in neighbours:
        corners -= 2
        for item in state:
            if neighbour.is_diagonal(item):
                corners += 2

        state.append(neighbour)

    diagonals = get_diagonals(data, letter, current)
    for diagonal in diagonals:
        if shares_neighbours(data, letter, current, diagonal) >= 2:
            corners -= 1

    if plot:
        plot.members += 1
        plot.fences += corners
    else:
        plot = Plot(letter=letter, members=1, fences=corners)
        unique_plots.append(plot)

    for neighbour in neighbours:
        if neighbour.loc in assigned:
            continue

        assign_corner(data, letter, neighbour, assigned, unique_plots, plot)


def part_2(data: defaultdict):
    assigned = set()
    unique_plots: list[Plot] = []

    itterator = copy(data)
    for loc, letter in itterator.items():
        if loc in assigned:
            continue

        current = Vector(y=loc[0], x=loc[1])
        assign_corner(data, letter, current, assigned, unique_plots)

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
assert tp2_4 == 368


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
