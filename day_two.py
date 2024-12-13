### Day Fucking 2 ###


# %%
from copy import copy 

test_data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

with open("C:/Users/megan/OneDrive/Desktop/Advent/input_day2.txt") as f:
    rows = []
    for line in f:
        row = (line.strip().split(" "))
        num_row = []
        for number in row:
            number = int(number)
            num_row.append(number)
            
        rows.append(num_row)

# assess the trend

def determine_trend(rows):
    safe_count = 0
    for row in rows:
        # row = [1, 2, 7, 8, 9]
        trend = row[0] - row[1]
        # trend = -1
        # range = 0, 1, 2, 3 
        for index in range(len(row) - 1): # how long list is, one index less
            # index = 1
            first = row[index] # 2
            second = row[index + 1] # 7
            difference = first - second # -5
            if trend > 0:
                if difference > 0:
                    pass # kinda safe
                else:
                    break # unsafe
            else:
                if difference < 0:
                    pass # kinda safe
                else:
                    break # unsafe
                
            difference = abs(difference) # 5    
            if difference > 0:      # at least one
                if difference < 4:  # really safe
                    pass
                else:
                    break # unsafe
            else:
                break # unsafe
        else: # will run if for loop does not break
            safe_count += 1        

    return safe_count        
       

answer = determine_trend(test_data)
print(answer)
   
answer_2 = determine_trend(rows)
print(answer_2)


# a function given a row (list of number) returns True if safe False if unsafe (edit and test if True)
def is_safe(row):
    trend = row[0] - row[1]
    # trend = -1
    # range = 0, 1, 2, 3 
    for index in range(len(row) - 1): # how long list is, one index less
        # index = 1
        first = row[index] # 2
        second = row[index + 1] # 7
        difference = first - second # -5
        if trend > 0:
            if difference > 0:
                pass # kinda safe
            else:
                return False # unsafe
        else:
            if difference < 0:
                pass # kinda safe
            else:
                return False # unsafe
            
        difference = abs(difference) # 5    
        if difference > 0:      # at least one
            if difference < 4:  # really safe
                pass
            else:
                return False # unsafe
        else:
            return False # unsafe
    else: # will run if for loop does not break
        return True      

    
test_line = [1, 3, 2, 4, 5]
is_safe(test_line)

is_safe(test_data[0])

def part_2(rows):
    safe_count = 0
    for row in rows:
        if is_safe(row):
            safe_count += 1
        else:
            # range = [0, 1, 2, 3, 4] 
            for index in range(len(row)):
                # index = 0
                shorter_row = copy(row)
                del shorter_row[index]
                if is_safe(shorter_row):
                    safe_count += 1
                    break # safe (for loop)
                else: # not safe
                    continue
                                
    return safe_count    

part_2(test_data)
part_2(rows)


