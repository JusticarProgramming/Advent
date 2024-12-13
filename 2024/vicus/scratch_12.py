from typing import List

test_data = [['A', 'A', 'A', 'A'],
             ['B', 'B', 'C', 'D'],
             ['B', 'B', 'C', 'C'],
             ['E', 'E', 'E', 'C']]

test_data_2 = [['O', 'O', 'O', 'O', 'O'],
               ['O', 'X', 'O', 'X', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'X', 'O', 'X', 'O'],
               ['O', 'O', 'O', 'O', 'O']]

test_data_3 = [
    ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'F', 'F'],
    ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'C', 'F'],
    ['V', 'V', 'R', 'R', 'R', 'C', 'C', 'F', 'F', 'F'],
    ['V', 'V', 'R', 'C', 'C', 'C', 'J', 'F', 'F', 'F'],
    ['V', 'V', 'V', 'V', 'C', 'J', 'J', 'C', 'F', 'E'],
    ['V', 'V', 'I', 'V', 'C', 'C', 'J', 'J', 'E', 'E'],
    ['V', 'V', 'I', 'I', 'I', 'C', 'J', 'J', 'E', 'E'],
    ['M', 'I', 'I', 'I', 'I', 'I', 'J', 'J', 'E', 'E'],
    ['M', 'I', 'I', 'I', 'S', 'I', 'J', 'E', 'E', 'E'],
    ['M', 'M', 'M', 'I', 'S', 'S', 'J', 'E', 'E', 'E']
]

from typing import List, Tuple


def get_neighbors(x: int, y: int, rows: int, cols: int) -> List[Tuple[int, int]]:
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors


def dfs(x: int, y: int, plant: str, garden: List[List[str]], visited: List[List[bool]]) -> Tuple[int, int]:
    stack = [(x, y)]
    area = 0
    perimeter = 0
    rows, cols = len(garden), len(garden[0])

    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        area += 1
        local_perimeter = 4

        for nx, ny in get_neighbors(cx, cy, rows, cols):
            if garden[nx][ny] == plant:
                if not visited[nx][ny]:
                    stack.append((nx, ny))
                local_perimeter -= 1

        perimeter += local_perimeter

    return area, perimeter


def calculate_fence_price(garden: List[List[str]]) -> int:
    if not garden:
        return 0

    rows, cols = len(garden), len(garden[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0

    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                plant = garden[x][y]
                area, perimeter = dfs(x, y, plant, garden, visited)
                total_price += area * perimeter

    return total_price


print(calculate_fence_price(test_data))  # Output should be 140
print(calculate_fence_price(test_data_2))  # Output should be 772
print(calculate_fence_price(test_data_3))  # Output should be 1930


def format_data(data: str) -> List[List[str]]:
    return [list(row) for row in data]


def read_from_file(file_name: str):
    with open(file_name, 'r') as file:
        data = file.read().splitlines()
    return format_data(data)


def part_1(file_name: str):
    garden = read_from_file(file_name)
    return calculate_fence_price(garden)


print(part_1('input_12.txt'))  # Output should be 1467094


def calculate_fence_price_2(garden: List[List[str]]) -> int:
    if not garden:
        return 0

    rows, cols = len(garden), len(garden[0])
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0

    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                plant = garden[x][y]
                area, perimeter = dfs(x, y, plant, garden, visited)
                total_price += area + perimeter

    return total_price

def part_2(file_name: str):
    garden = read_from_file(file_name)
    return calculate_fence_price_2(garden)

print('Part 2')
print(part_2('input_12.txt'))
print(calculate_fence_price_2(test_data))  # 80
print(calculate_fence_price_2(test_data_2))  # 436
print(calculate_fence_price_2(test_data_3))  # 1206
