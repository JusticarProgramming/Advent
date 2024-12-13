# %% Test data.
test_data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


# %% Load input data.
with open("C:/Users/User/Documents/Advent_of_Code/2024/input/day_4.txt") as f:
    lines = f.readlines()
    lines = [i.strip() for i in lines]


# %% Helper functions.
def find_xmas_count(lines: list[str]) -> int:
    """Find all occurences of XMAS. Occurences may be overlapping.

    Args:
    ----
        lines: Formatted puzzle input.

    Returns:
    -------
        count: count of XMAS occurences
    """
    count = 0
    row_count = len(lines)
    line_length = len(lines[0])
    matches = ["XMAS", "SAMX"]
    for row in range(row_count):
        for position in range(line_length):
            if position + 3 < line_length and (
                lines[row][position]
                + lines[row][position + 1]
                + lines[row][position + 2]
                + lines[row][position + 3]
                in matches
            ):
                count += 1

            if row + 3 < row_count and (
                lines[row][position]
                + lines[row + 1][position]
                + lines[row + 2][position]
                + lines[row + 3][position]
                in matches
            ):
                count += 1

            if (
                (row + 3 < row_count)
                and (position + 3 < line_length)
                and (
                    lines[row][position]
                    + lines[row + 1][position + 1]
                    + lines[row + 2][position + 2]
                    + lines[row + 3][position + 3]
                    in matches
                )
            ):
                count += 1

            if (
                (row - 3 >= 0)
                and (position + 3 < line_length)
                and (
                    lines[row][position]
                    + lines[row - 1][position + 1]
                    + lines[row - 2][position + 2]
                    + lines[row - 3][position + 3]
                    in matches
                )
            ):
                count += 1

    return count


def find_x_mas_count(lines: list[str]) -> int:
    """Find all occurences of MAS in the shape of an X.

    Args:
    ----
        lines: Formatted puzzle input.

    Returns:
    -------
        count: count of crossed MAS occurences
    """
    count = 0
    row_count = len(lines)
    line_length = len(lines[0])
    matches = ["MAS", "SAM"]
    for row in range(row_count):
        for position in range(line_length):
            if (row + 2 < row_count) and (position + 2 < line_length):
                if (
                    lines[row][position]
                    + lines[row + 1][position + 1]
                    + lines[row + 2][position + 2]
                    in matches
                    and lines[row + 2][position]
                    + lines[row + 1][position + 1]
                    + lines[row][position + 2]
                    in matches
                ):
                    count += 1

    return count


# %% Tests.
assert find_xmas_count(test_data) == 18
assert find_x_mas_count(test_data) == 9


# %% Solutions.
print(f"Part one: {find_xmas_count(lines)}")
print(f"Part two: {find_x_mas_count(lines)}")
