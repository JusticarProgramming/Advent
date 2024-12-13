### Day Fucking 3 ###

# %%
import re
test_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("C:/Users/megan/OneDrive/Desktop/Advent/input_day3.txt", "r") as f:
    lines = f.read()
  
# get the pairs    

def search_expression(text):
    total_result = 0
    
    regex_pattern = r"mul\((\d{1,3},\d{1,3})\)"
    pairs = re.findall(regex_pattern, text)
    
    print(pairs) 
 
    for item in pairs:
        parts = item.split(',')
        num1 = int(parts[0])
        num2 = int(parts[1])
        pair_result = num1 * num2
        total_result += pair_result
        
    print(total_result)


# search_expression(test_data)
# search_expression(lines)

test_data2 = "xmul(2,44)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def part_2(text):
    is_state_on = True # we start in a true state
    regex_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    pairs = re.findall(regex_pattern, text)
    
    # print(pairs)
    
    list = []
    total_result = 0
    for item in pairs:  # check if the state is on or off
        if "do()" in item:
            is_state_on = True
            continue
        if "don't()" in item:
            is_state_on = False
            continue
        
        if is_state_on:
            pair = item.replace("mul(", "").replace(")", "") # dankie hannes
            list.append(pair)  # list onodig, maar vir nou in my lewe want dit maak sin
            for item in list:
                parts = item.split(',')
                num1 = int(parts[0])
                num2 = int(parts[1])
                pair_result = num1 * num2
            total_result += pair_result # verstaan nou hkm indentation belangrik is
        
        
    return total_result        
        
    
part_2(test_data2)
part_2(lines)
