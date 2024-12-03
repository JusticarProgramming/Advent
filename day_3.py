# %% Imports
import re


# %% Load input data.
with open("scratch_4.txt") as f:
    text = f.read().strip()


# %% Helper functions.


def extract_operations(text: str) -> list[tuple]:
    """extract all non-overlapping occurences of mul(int, int).

    Args:
    ----
        text: Full day 3 input text

    Returns:
    -------
        operations: tuple of integers of all valid mul operations.
    """
    operations = re.findall("mul\(\d+,\d+\)", text)
    return [eval(operation.replace("mul", "")) for operation in operations]


def extract_operations_with_instructions(text: str) -> list[tuple]:
    """extract all non-overlapping occurences of mul(int, int).

    Args:
    ----
        text: Full day 3 input text

    Returns:
    -------
        operations: tuple of integers of all valid mul operations.
    """
    operations = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", text)

    for i, operation in enumerate(operations):
        if "mul" in operation:
            operations[i] = eval(re.sub("mul", "", operation))

    return operations


def sum_of_products(operations: list[tuple]) -> int:
    """Calculate the sum of products for all valid operations.

    Args:
    ----
        operations: valid mul operations.

    Returns:
    -------
        total: sum of products.
    """
    total = 0
    do = True

    for operation in operations:
        if operation == "don't()":
            do = False
        elif operation == "do()":
            do = True
        else:
            if do:
                x, y = operation
                total += x * y

    return total


# %% Tests.

test_data_p1 = (
    "-:-]what()(+/mul(957,396)?mul((550,844)%+why())-? #}from()mul(488,628)%}"
)

assert extract_operations(test_data_p1) == [(957, 396), (488, 628)]
assert sum_of_products(extract_operations(test_data_p1)) == 685436

test_data_p2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)

assert extract_operations_with_instructions(test_data_p2) == [
    (2, 4),
    "don't()",
    (5, 5),
    (11, 8),
    "do()",
    (8, 5),
]
assert sum_of_products(extract_operations_with_instructions(test_data_p2)) == 48


# %% Solutions.

print(f"Part 1: {sum_of_products(extract_operations(text))}")
print(f"Part 2: {sum_of_products(extract_operations_with_instructions(text))}")
