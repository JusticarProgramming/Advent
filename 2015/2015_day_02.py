from dataclasses import dataclass


@dataclass
class Present():
    length: int
    width: int
    height: int

    def surface_area(self):
        return 2 * self.length * self.width + 2 * self.width * self.height + 2 * self.height * self.length

    def smallest_side_area(self):
        return min(self.length * self.width, self.width * self.height, self.height * self.length)

    def smallest_perimeter(self):
        return min(2 * self.length + 2 * self.width, 2 * self.width + 2 * self.height, 2 * self.height + 2 * self.length)

    def volume(self):
        return self.length * self.width * self.height

    def ribbon_length(self):
        return self.smallest_perimeter() + self.volume()

def read_input(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def part1(data):
    presents = [Present(*map(int, present.split('x'))) for present in data]
    return sum(present.surface_area() + present.smallest_side_area() for present in presents)

def part2(data):
    presents = [Present(*map(int, present.split('x'))) for present in data]
    return sum(present.ribbon_length() for present in presents)



test_present = Present(2, 3, 4)
assert test_present.surface_area() == 52
assert test_present.smallest_side_area() == 6
assert test_present.smallest_perimeter() == 10
assert test_present.volume() == 24
assert test_present.ribbon_length() == 34
assert test_present.surface_area() + test_present.smallest_side_area() == 58

test_present = Present(1, 1, 10)
assert test_present.surface_area() == 42
assert test_present.smallest_side_area() == 1
assert test_present.smallest_perimeter() == 4
assert test_present.volume() == 10
assert test_present.ribbon_length() == 14
assert test_present.surface_area() + test_present.smallest_side_area() == 43

data = read_input('input_2.txt')
print(part1(data))
print(part2(data))
