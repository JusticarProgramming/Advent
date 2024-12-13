def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def count_floors(directions):
    return directions.count('(') - directions.count(')')

def find_basement_position(directions):
    floor = 0
    for i, direction in enumerate(directions):
        floor += 1 if direction == '(' else -1
        if floor == -1:
            return i + 1
    return None

def main():
    directions = read_from_file('input_1.txt')
    print('Part 1:', count_floors(directions))
    print('Part 2:', find_basement_position(directions))

if __name__ == '__main__':
    main()