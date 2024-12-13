# F this shit 

file_path = 'day4.txt'

with open(file_path, 'r') as file:
    grid = [line.strip() for line in file.readlines()]


# Part1 Get XMAS
def get_xmas(grid,comp ="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    comp = "XMAS" # Comparison word
    comp_length = 4


    directions = [
        (0, 1),  
        (0, -1), 
        (1, 0),   
        (-1, 0), 
        (1, 1),  
        (-1, -1), 
        (1, -1),
        (-1, 1),
    ]

    def word_test(grid, row, col ,direction):
        d_row, d_col = direction
        for i in range (comp_length):
            n_row, n_col = row + i * d_row, col + i * d_col
            if not (0 <= n_row < rows and 0 <= n_col < cols) or grid[n_row][n_col] != comp[i]:
                return False
        return True
    

    count = 0 
    for row in range(rows):
        for col in range(cols):
            for direction in directions:
                if word_test(grid, row, col, direction):
                    count += 1
    return count


xmas_count = get_xmas(grid) 

print(f"Part 1 answer: ",xmas_count)






# Part 2 Get X-MAS

def find_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    def test_x_mas(grid, row, col):
        # Validate if the center point is 'A' and run the diagonal test from 'A' pos
        if grid[row][col] != 'A':
            return False
        
        # Diagonals for MAS
        diagonals = [
            [(-1, -1), (0, 0), (1, 1)],  
            [(-1, 1), (0, 0), (1, -1)]  
        ]
        
        # Test for MAS in diagonals
        valid_diagonals = 0
        for diagonal in diagonals:
            try:
                mas_forward = ''.join(
                    grid[row + d_row][col + d_col] 
                    for d_row, d_col in diagonal
                )
                mas_backward = mas_forward[::-1]
                if mas_forward == "MAS" or mas_backward == "MAS":
                    valid_diagonals += 1
            except IndexError:
                continue
        return valid_diagonals == 2

    count = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if test_x_mas(grid, row, col):
                count += 1

    return count


x_mas = find_x_mas(grid)
print(f"Part 2 answer: ",x_mas)

            

