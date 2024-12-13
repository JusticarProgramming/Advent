test_data = ['89010123',
             '78121874',
             '87430965',
             '96549874',
             '45678903',
             '32019012',
             '01329801',
             '10456732']
formatted = {}
# Test data represents a flat map, so we need a 2D array to represent it
# We can replace the index with a number, as we process each row i.e 1,2,3,4,5
# The topographic map indicates the height at each position using a scale from 0 (lowest) to 9 (highest).
# you determine that a good hiking trail is as long as possible and has an even, gradual, uphill slope. For all practical purposes, this means that a hiking trail is any path that starts at height 0, ends at height 9, and always increases by a height of exactly 1 at each step. Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of the map)
# A trailhead is any position that starts one or more hiking trails - here, these positions will always have height 0. Assembling more fragments of pages, you establish that a trailhead's score is the number of 9-height positions reachable from that trailhead via a hiking trail.

for index, row in enumerate(test_data):
    formatted[index] = list(row)


def find_trailheads(formatted_data):
    trailheads = []
    for index, row in formatted_data.items():
        for i, char in enumerate(row):
            if char == '0':
                trailheads.append((index, i))
    return trailheads


def find_trails(formatted_data, trailhead):
    trails = []
    stack = [(trailhead, [trailhead])]
    while stack:
        (x, y), path = stack.pop()
        current_height = int(formatted_data[x][y])
        if current_height == 9:
            trails.append(path)
        possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for new_x, new_y in possible_moves:
            if 0 <= new_x < len(formatted_data) and 0 <= new_y < len(formatted_data[0]):
                next_height = int(formatted_data[new_x][new_y])
                if next_height == current_height + 1:
                    stack.append(((new_x, new_y), path + [(new_x, new_y)]))
    return trails


def count_trails(formatted_data, trailheads):
    total_trails = 0
    for trailhead in trailheads:
        trails = find_trails(formatted_data, trailhead)
        for trail in trails:
            total_trails += 1
    return total_trails


trailheads = find_trailheads(formatted)
total_trails = count_trails(formatted, trailheads)
print(total_trails)  # Output the number of trails starting at each trailhead
