import cProfile
import pstats
import sys
from copy import copy

sys.setrecursionlimit(100000000)

# %%
test_input = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]

def parse_data(line):
    result, values = line.strip().split(":")
    result = int(result)
    values = values.strip().split(" ")
    return [result, values]

test = [parse_data(i) for i in test_input]

with open(f"../../inout_07.txt", "r") as f:
    data = [parse_data(i) for i in f]

def is_valid(operators, answer, total, values):
    copied = copy(values)
    number = copied[0]
    del copied[0]

    for op in operators:
        new_total = eval(f"{total}{op}{number}")
        if new_total > answer:
            continue

        if not copied:
            if new_total == answer:
                return True
            continue

        if is_valid(operators, answer, new_total, copied):
            return True

    return False

def solution(data, operators):
    total = 0
    for answer, values in data:
        if is_valid(operators, answer, values[0], values[1:]):
            total += answer

    return total

def main():
    tp1 = solution(test, ["+", "*"])
    print(f"{tp1=}")
    # assert tp1 == 3749

    dp1 = solution(data, ["+", "*"])
    print(f"{dp1=}")
    # assert dp1 == 2437272016585

    tp2 = solution(test, ["+", "*", ""])
    print(f"{tp2=}")
    # assert tp2 == 11387

    dp2 = solution(data, ["+", "*", ""])
    print(f"{dp2=}")
    # assert dp2 == 162987117690649

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.strip_dirs().print_stats()
    stats.print_stats(10)  # Display the 10 slowest functions