# Read a file and put everything into one long string
string_input = ""

with open("scratch_4.txt", "r") as file:
    for line in file:
        string_input += line

# We need to clean up the string, the only valid character in this format "mul(1,2)", there can be three digit mnumbers but all other special charcters and spaces are illegal
# We can use regular expressions to clean up the string
import re
string_input = re.sub(r"[^0-9\(\),]", "", string_input)
print(string_input)

# Now we should clean up any empty () and commas that are not between numbers
string_input = re.sub(r"\(\s*\)", "", string_input)
string_input = re.sub(r",\s*", ",", string_input)
print(string_input)

# Now for each of the capture groups, we can split them into a list of numbers
numbers = re.findall(r"\d+", string_input)
print(numbers)

# Now we can convert the numbers to integers, then split them into groups of 2
numbers = list(map(int, numbers))
numbers = [numbers[i:i+2] for i in range(0, len(numbers), 2)]
print(numbers)

# Now we can multiply the numbers in each group
result = [x*y for x, y in numbers]
print(result)

# Now we can sum the results
result = sum(result)
print(result)

#Hierdie bo werk nie reg nie, dei capture groups is kak en die antwoord is te hoog

print("=====================================")

import re

# Read the file and put everything into one long string
string_input = ""
with open("scratch_4.txt", "r") as file:
    for line in file:
        string_input += line

# Use regular expressions to find valid mul(X,Y) instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, string_input)

# Convert matches to integers and multiply
results = [int(x) * int(y) for x, y in matches]

# Sum the results
total_sum = sum(results)
print(total_sum)

#Hierdie werk, maar ek het nie die do() en don't() instructions geignore nie, die regex is beter so die antwoord is reg


print("=====================================")

import re

# Read the file and put everything into one long string
string_input = ""
with open("scratch_4.txt", "r") as file:
    for line in file:
        string_input += line

# Use regular expressions to find valid mul(X,Y) instructions and do/don't instructions
pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
matches = re.findall(pattern, string_input)

# Initialize variables
results = []
mul_enabled = True

# Process each match
for match in matches:
    instruction = match[0]
    if instruction == "do()":
        mul_enabled = True
    elif instruction == "don't()":
        mul_enabled = False
    elif mul_enabled and instruction.startswith("mul"):
        x, y = int(match[1]), int(match[2])
        results.append(x * y)

# Sum the results
total_sum = sum(results)
print(total_sum)