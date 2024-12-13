from dataclasses import dataclass
import re


@dataclass
class Machine:
    button_a_x: int
    button_a_y: int
    button_b_x: int
    button_b_y: int
    prize_location_x: int
    prize_location_y: int


def read_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        machines = []
        for i in range(0, len(lines), 4):
            if i + 2 < len(lines):
                button_a_x = int(re.search(r'X\+(\d+)', lines[i]).group(1))
                button_a_y = int(re.search(r'Y\+(\d+)', lines[i]).group(1))
                button_b_x = int(re.search(r'X\+(\d+)', lines[i + 1]).group(1))
                button_b_y = int(re.search(r'Y\+(\d+)', lines[i + 1]).group(1))
                prize_location_x = int(re.search(r'X=(\d+)', lines[i + 2]).group(1))
                prize_location_y = int(re.search(r'Y=(\d+)', lines[i + 2]).group(1))
                machines.append(
                    Machine(button_a_x, button_a_y, button_b_x, button_b_y, prize_location_x, prize_location_y))
    return machines


data = read_data('input_13.txt')


# Part 1 get prize
def get_prize(machine):
    for i in range(0, 100):
        for j in range(0, 100):
            if machine.button_a_x * i + machine.button_b_x * j == machine.prize_location_x and machine.button_a_y * i + machine.button_b_y * j == machine.prize_location_y:
                return i * 3 + j


# Part 2 get prize with large x and y and it works
def get_large_prize(machine):
    machine.prize_location_x += 10000000000000
    machine.prize_location_y += 10000000000000
    number = machine.button_a_x * machine.button_b_x * machine.prize_location_y - machine.button_a_y * machine.button_b_x * machine.prize_location_x
    denominator = machine.button_a_x * machine.button_b_y - machine.button_a_y * machine.button_b_x
    x_intersect = number // denominator
    press_b = x_intersect // machine.button_b_x
    press_a = (machine.prize_location_x - x_intersect) // machine.button_a_x
    if (
            press_a >= 0
            and press_b >= 0
            and machine.button_a_y * press_a + machine.button_b_y * press_b == machine.prize_location_y
            and machine.button_a_x * press_a + machine.button_b_x * press_b == machine.prize_location_x
    ):
        return press_b + 3 * press_a
    return 0

# DOES NOT WORK, I DON'T KNOW WHY, THE MATH IS FOLLOWED TO THE LETTER
# Part 2 get prize with Euclidean algorithm since the x and y of prize is now 10000000000000 larger
# def get_token_amount_with_euclidean_algorithm(machine):
#     def gcd(a, b):
#         while b:
#             a, b = b, a % b
#         return a
#
#     def extended_gcd(a, b):
#         x, y, u, v = 0, 1, 1, 0
#         while a != 0:
#             q, r = b // a, b % a
#             m, n = x - u * q, y - v * q
#             b, a, x, y, u, v = a, r, u, v, m, n
#         return b, x, y
#
#     def modinv(a, m):
#         g, x, y = extended_gcd(a, m)
#         if g != 1:
#             raise ValueError
#         return x % m
#
#     def moddiv(a, b, m):
#         a = a % m
#         inv = modinv(b, m)
#         return (inv * a) % m
#
#     x = machine.prize_location_x
#     y = machine.prize_location_y
#     a = machine.button_a_x
#     b = machine.button_b_x
#     c = machine.button_a_y
#     d = machine.button_b_y
#
#     g = gcd(a, c)
#     if (x - y) % g != 0:
#         return None
#
#     x = moddiv(x - y, g, a // g)
#     y = (x * a - machine.prize_location_x) // machine.button_a_y
#
#     return x * 3 + y


# Test data
machine_1 = Machine(94, 34, 22, 67, 8400, 5400)
machine_2 = Machine(26, 66, 67, 21, 12748, 12176)
machine_3 = Machine(17, 86, 84, 37, 7870, 6450)
machine_4 = Machine(69, 23, 27, 71, 18641, 10279)

print(get_prize(machine_1))
print(get_prize(machine_2))
print(get_prize(machine_3))
print(get_prize(machine_4))
assert get_prize(machine_1) == 280
assert get_prize(machine_2) is None
assert get_prize(machine_3) == 200
assert get_prize(machine_4) is None


# Real data
def part_1(data):
    tokens = 0
    for machine in data:
        token = get_prize(machine)
        if token:
            tokens += token

    return tokens


def part_2(data):
    tokens = 0
    for machine in data:
        token = get_large_prize(machine)
        if token:
            tokens += token
    return tokens

print("Part 2")
print(get_large_prize(machine_1))
print(get_large_prize(machine_2))
print(get_large_prize(machine_3))
print(get_large_prize(machine_4))
# assert get_large_prize(machine_1) == 0
# assert get_large_prize(machine_2) == 459236326669
# assert get_large_prize(machine_3) == 0
# assert get_large_prize(machine_4) == 416082282239

print("Part 2 answer")
print(part_2(data))
