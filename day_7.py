import cProfile
import pstats

# %% Test case.

test = [
    [190, [10, 19]],
    [3267, [81, 40, 27]],
    [83, [17, 5]],
    [156, [15, 6]],
    [7290, [6, 8, 6, 15]],
    [161011, [16, 10, 13]],
    [192, [17, 8, 14]],
    [21037, [9, 7, 18, 13]],
    [292, [11, 6, 16, 20]],
]

# %% Load Data.
with open("2024/vicus/inout_07.txt") as f:
    equations = f.readlines()
    equations = [equation.strip().split(":") for equation in equations]

# %% Helper functions.
def calibrations(value: int, nums: list[int], use_concat: bool = False):
    """Checks that a given equation is valid.

    Args:
    ----
        value: total value for equation.
        nums: numbers used in equation.
        use_concat: switch concatanation operator on/off

    Returns:
    -------
        bool: returns True if quation is valid
    """
    if len(nums) == 1:
        return nums[0] == value
    if calibrations(value, [nums[0] + nums[1]] + nums[2:], use_concat):
        return True
    if calibrations(value, [nums[0] * nums[1]] + nums[2:], use_concat):
        return True
    if use_concat and calibrations(
        value, [int(str(nums[0]) + str(nums[1]))] + nums[2:], use_concat
    ):
        return True

# %% Main function to profile
def main():
    # %% Tests
    part_one_test = 0
    part_two_test = 0

    for equation in test:
        value, nums = equation
        if calibrations(value, nums):
            part_one_test += value
        if calibrations(value, nums, use_concat=True):
            part_two_test += value

    assert part_one_test == 3749
    assert part_two_test == 11387

    # %% Solutions.
    total_part_one = 0
    total_part_two = 0

    for line in equations:
        value, nums = line
        value = int(value)
        nums = [int(x) for x in nums.strip().split()]
        if calibrations(value, nums):
            total_part_one += value
        if calibrations(value, nums, use_concat=True):
            total_part_two += value

    print(f"Part one: {total_part_one}")
    print(f"Part two: {total_part_two}")

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()