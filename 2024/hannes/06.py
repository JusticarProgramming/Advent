from copy import copy

test = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]


with open(f"../../scratch_4.txt", "r") as f:
    data = [l.strip() for l in f]


def part_1(map):
    visited = []

    modifiers = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    loc_guard = [[y, row.index("^")] for y, row in enumerate(map) if "^" in row][0]
    y_guard, x_guard = loc_guard
    visited.append((y_guard, x_guard))

    rotation = 0
    while True:
        y_mod, x_mod = modifiers[rotation]

        y_target = y_guard + y_mod
        x_target = x_guard + x_mod

        if y_target < 0 or y_target >= len(map):
            break

        if x_target < 0 or x_target >= len(map[y_target]):
            break

        target = map[y_target][x_target]

        if target == "#":
            if rotation == 3:
                rotation = 0
            else:
                rotation += 1
            continue

        y_guard = y_target
        x_guard = x_target

        visited.append((y_target, x_target))

    visited = set(visited)
    return len(visited), visited, loc_guard


tp1 = part_1(test)
print(f"{tp1=}")
assert tp1[0] == 41

dp1 = part_1(data)
print(f"{dp1=}")


def is_loop(map):
    obstacles = set()

    modifiers = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    y_guard, x_guard = [[y, row.index("^")] for y, row in enumerate(map) if "^" in row][0]

    rotation = 0
    while True:
        y_mod, x_mod = modifiers[rotation]

        y_target = y_guard + y_mod
        x_target = x_guard + x_mod

        if y_target < 0 or y_target >= len(map):
            break

        if x_target < 0 or x_target >= len(map[y_target]):
            break

        target = map[y_target][x_target]

        if target == "#":
            obj = (y_target, x_target, rotation)
            if obj in obstacles:
                return True

            obstacles.add(obj)

            if rotation == 3:
                rotation = 0
            else:
                rotation += 1
            continue

        y_guard = y_target
        x_guard = x_target

    return False


def part_2(map):
    total = 0

    _, visited, guard = part_1(map)

    for y, x in visited:
        if y == guard[0] and x == guard[1]:
            continue

        new_map = copy(map)

        row = list(new_map[y])
        row[x] = "#"
        row = "".join(row)

        new_map[y] = row
        if is_loop(new_map):
            total += 1

    return total


tp2 = part_2(test)
print(f"{tp2=}")
assert tp2 == 6

dp2 = part_2(data)
print(f"{dp2=}")
