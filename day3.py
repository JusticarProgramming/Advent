# Regular expresion lib
import re

# File Path 
file_path = 'day3.txt'

# Read File
with open(file_path, 'r') as file:
    data = file.read()

# Pattern to find matches with mul(a,b)
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
pattern_part2 = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"




def calc_mul(data, pattern):            # Part 1
    # Find all matches
    match = re.findall(pattern, data)

    # Sum of all matches
    answer = sum(int(a) * int(b) for a,b in match)
    
    return answer

# print(calc_mul(data, pattern))
print(calc_mul(data, pattern))




def calc_con(data, pattern_part2):  # Part 2
    data = re.findall(pattern_part2, data)
    condition = True
    total_sum = 0

    for info in data: 
        if info == "do()":
            condition = True
        elif info == "don't()":
            condition = False
        elif info.startswith("mul(") and condition:
            nums = re.findall(r"\d{1,3}", info)
            if nums:
                total_sum += int(nums[0]) * int(nums[1])

    return total_sum

print(calc_con(data, pattern_part2))