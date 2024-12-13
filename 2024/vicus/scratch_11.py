from collections import deque

test_data = [0, 1, 10, 99, 999]
trickier_data = [125, 17]

def process_stone(stone, memo):
    if stone in memo:
        return memo[stone]
    if stone == 0:
        processed = [1]
    elif len(str(stone)) % 2 == 0 and stone != 1:
        stone_str = str(stone)
        half = len(stone_str) // 2
        processed = [int(stone_str[:half]), int(stone_str[half:])]
    else:
        processed = [stone * 2024]
    memo[stone] = processed
    return processed

def run_x_time(x, data):
    memo = {}
    data = deque(data)
    for _ in range(x):
        print(f"Processing {_} times")
        new_data = deque()
        while data:
            stone = data.popleft()
            new_data.extend(process_stone(stone, memo))
        data = new_data
    return list(data)

# Test cases
assert run_x_time(1, test_data) == [1, 2024, 1, 0, 9, 9, 2021976]
assert run_x_time(6, trickier_data) == [2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2]

def part_1():
    with open('input_11.txt', 'r') as file:
        data = file.read()
    data = list(map(int, data.split()))
    final = run_x_time(25, data)
    return len(final)

def part_2():
    with open('input_11.txt', 'r') as file:
        data = file.read()
    data = list(map(int, data.split()))
    final = run_x_time(75, data)
    return len(final)

print(part_1())
print(part_2())

# 259112729857522