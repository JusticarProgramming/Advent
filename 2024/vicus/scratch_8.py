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

with open(f"scratch_4.txt", "r") as f:
    data = [line.strip() for line in f]

def looper_1(map_data):
    time_travelers = []

    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    joe = [[y, row.index("^")] for y, row in enumerate(map_data) if "^" in row][0]
    young_joe, old_joe = joe
    time_travelers.append((young_joe, old_joe))

    rotation = 0
    while True:
        y_dir, x_dir = directions[rotation]

        y_target = young_joe + y_dir
        x_target = old_joe + x_dir

        if y_target < 0 or y_target >= len(map_data):
            break

        if x_target < 0 or x_target >= len(map_data[y_target]):
            break

        target = map_data[y_target][x_target]

        if target == "#":
            if rotation == 3:
                rotation = 0
            else:
                rotation += 1
            continue

        young_joe = y_target
        old_joe = x_target

        time_travelers.append((y_target, x_target))

    time_travelers = set(time_travelers)
    return len(time_travelers), time_travelers, joe

def is_loop(map_data):
    obstacles = set()

    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    young_joe, old_joe = [[y, row.index("^")] for y, row in enumerate(map_data) if "^" in row][0]

    rotation = 0
    while True:
        y_dir, x_dir = directions[rotation]

        y_target = young_joe + y_dir
        x_target = old_joe + x_dir

        if y_target < 0 or y_target >= len(map_data):
            break

        if x_target < 0 or x_target >= len(map_data[y_target]):
            break

        target = map_data[y_target][x_target]

        if target == "#":
            obstacle = (y_target, x_target, rotation)
            if obstacle in obstacles:
                return True

            obstacles.add(obstacle)

            if rotation == 3:
                rotation = 0
            else:
                rotation += 1
            continue

        young_joe = y_target
        old_joe = x_target

    return False

def looper_2_the_prequel(map_data):
    total_loops = 0

    _, time_travelers, joe = looper_1(map_data)

    for y, x in time_travelers:
        if y == joe[0] and x == joe[1]:
            continue

        new_map = copy(map_data)

        row = list(new_map[y])
        row[x] = "#"
        row = "".join(row)

        new_map[y] = row
        if is_loop(new_map):
            total_loops += 1

    return total_loops

def print_map(map_data):
    for row in map_data:
        print(' '.join(row))
    print("#" * 40)

print_map(data)