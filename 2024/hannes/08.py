# %%
from collections import defaultdict
from copy import copy

test = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............",
]

with open(f"../../input_08.txt", "r") as f:
    data = [i.strip() for i in f]


def prep_data(data):
    locations = defaultdict(list)

    for y in range(len(data)):
        for x in range(len(data[y])):
            symbol = data[y][x]
            if symbol == ".":
                continue

            locations[symbol].append([y, x])

    return locations


def part_1(data):
    unique = set()

    locations = prep_data(data)
    for locs in locations.values():
        for i in range(len(locs)):
            compare: list = copy(locs)
            start = compare.pop(i)

            for val in compare:
                distance = [start[0] - val[0], start[1] - val[1]]
                opposite = [start[0] + distance[0], start[1] + distance[1]]

                if opposite[0] < 0 or opposite[0] >= len(data):
                    continue

                if opposite[1] < 0 or opposite[1] >= len(data[0]):
                    continue

                unique.add(tuple(opposite))

    return len(unique)


tp1 = part_1(test)
print(f"{tp1=}")
assert tp1 == 14

dp1 = part_1(data)
print(f"{dp1=}")
# assert dp1 == 332


def part_2(data):
    unique = set()

    locations = prep_data(data)
    for locs in locations.values():
        for i in range(len(locs)):
            compare: list = copy(locs)
            start = compare.pop(i)

            for val in compare:
                unique.add(tuple(val))

                distance = [start[0] - val[0], start[1] - val[1]]

                next = [start[0] + distance[0], start[1] + distance[1]]
                while True:
                    if next[0] < 0 or next[0] >= len(data):
                        break

                    if next[1] < 0 or next[1] >= len(data[0]):
                        break

                    unique.add(tuple(next))
                    next = [next[0] + distance[0], next[1] + distance[1]]

    return len(unique)


tp2 = part_2(test)
print(f"{tp2=}")
assert tp2 == 34

dp2 = part_2(data)
print(f"{dp2=}")
