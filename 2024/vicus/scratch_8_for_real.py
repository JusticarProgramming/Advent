from collections import defaultdict


def is_antenna(char):
    return char.isalnum()


def find_matching_antennas(data):
    antennas = defaultdict(list)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if is_antenna(data[i][j]):
                antennas[data[i][j]].append((i, j))
    return antennas


def calculate_expected_antinodes(antennas, data):
    antinodes = []
    valid_positions = []
    antenna_positions = {pos for loc in antennas.values() for pos in loc}

    for loc in antennas.values():
        for i, a in enumerate(loc):
            valid_antinode_found = False
            for b in loc[:i] + loc[i + 1:]:
                antinode = (a[0] + (a[0] - b[0]), a[1] + (a[1] - b[1]))
                if (0 <= antinode[0] < len(data) and 0 <= antinode[1] < len(data[0]) and
                        data[antinode[0]][antinode[1]] == '.' and antinode not in antenna_positions):
                    antinodes.append(antinode)
                    valid_antinode_found = True
            if valid_antinode_found and a not in antenna_positions:
                valid_positions.append(a)

    # Combine valid antinodes and valid antenna positions
    antinodes.extend(valid_positions)

    return antinodes


def calculate_expected_antinodes_2(antennas, data):
    antinodes = set()
    antenna_positions = {pos for loc in antennas.values() for pos in loc}

    for loc in antennas.values():
        if len(loc) < 2:
            continue
        for i, a in enumerate(loc):
            for b in loc[:i] + loc[i + 1:]:
                distance = (a[0] - b[0], a[1] - b[1])
                next_pos = (a[0] + distance[0], a[1] + distance[1])
                while 0 <= next_pos[0] < len(data) and 0 <= next_pos[1] < len(data[0]):
                    if data[next_pos[0]][next_pos[1]] == '.':
                        antinodes.add(next_pos)
                    next_pos = (next_pos[0] + distance[0], next_pos[1] + distance[1])
            antinodes.add(a)

    return list(antinodes)


def draw_antinodes_map(data, antinodes):
    map_with_antinodes = [row[:] for row in data]  # Create a copy of the data map
    for i, j in antinodes:
        map_with_antinodes[i][j] = '#'
    return map_with_antinodes


def print_map(data):
    for row in data:
        print(''.join(row))


# Test data
test_data = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

test_data_map_correct = [['.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
                         ['.', '.', '.', '#', '.', '.', '.', '.', '0', '.', '.', '.'],
                         ['.', '.', '.', '.', '#', '0', '.', '.', '.', '.', '#', '.'],
                         ['.', '.', '#', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
                         ['.', '.', '.', '.', '0', '.', '.', '.', '.', '#', '.', '.'],
                         ['.', '#', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'],
                         ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
                         ['#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
                         ['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'],
                         ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'],
                         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
                         ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.']]


antennas = find_matching_antennas(test_data)
antinodes = calculate_expected_antinodes(antennas, test_data)

# Draw the map with antinodes
map_with_antinodes = draw_antinodes_map(test_data, antinodes)

# Print the map
print(antennas)
print(sorted(antinodes))
print(len(antinodes))
print_map(map_with_antinodes)

assert map_with_antinodes == test_data_map_correct


assert len(antinodes) == 14

def split_data(data):
    return [list(line) for line in data.splitlines()]


def read_data(file_path):
    with open(file_path, 'r') as file:
        return split_data(file.read())


def part1():
    data = read_data('input_08.txt')
    antennas = find_matching_antennas(data)
    antinodes = calculate_expected_antinodes(antennas, data)
    return len(antinodes)



def part2():
    data = read_data('input_08.txt')
    antennas = find_matching_antennas(data)
    antinodes = calculate_expected_antinodes_2(antennas, data)
    return len(antinodes)


print(part1())
print(part2())
