# %%
from copy import copy


def prep_data_1(data):
    if len(data) % 2 > 0:
        data = data + "0"

    result = []
    for id, v in enumerate(zip(data[0::2], data[1::2])):
        value, gap = v
        result += [id] * int(value)
        result += ["."] * int(gap)

    return result


test = "2333133121414131402"
test = prep_data_1(test)

with open(f"data/09.txt", "r") as f:
    data = f.readline().replace("\n", "").strip()
    data = prep_data_1(data)


def part_1(data: list):
    final = copy(data)
    for item in data[::-1]:
        if item == ".":
            del final[-1]
            continue

        try:
            swap = final.index(".")
        except ValueError:
            break

        final[swap] = item
        del final[-1]

    return sum([i * v for i, v in enumerate(final)])


tp1 = part_1(test)
print(f"{tp1=}")
assert tp1 == 1928

dp1 = part_1(data)
print(f"{dp1=}")
assert dp1 == 6359213660505


def prep_data_2(data):
    if len(data) % 2 > 0:
        data = data + "0"

    result = []
    for id, v in enumerate(zip(data[0::2], data[1::2])):
        value, gap = v
        result.append([id] * int(value))
        if int(gap) > 0:
            result.append(["."] * int(gap))

    return result


def part_2(data):
    final = copy(data)

    numbers = [i for i in data[::-1] if not "." in i]
    for num in numbers:
        num_loc = final.index(num)

        iterator = final[:num_loc]
        for i, val in enumerate(iterator):
            if not "." in val:
                continue

            diff = len(val) - len(num)
            if diff < 0:
                continue

            final[num_loc] = ["."] * len(num)
            if diff == 0:
                final = final[:i] + [num] + final[i + 1:]
            else:
                gap = ["."] * diff
                final = final[:i] + [num] + [gap] + final[i + 1:]

            # print(final)
            break

    expanded = []
    for item in final:
        for char in item:
            expanded.append(char)

    # print(expanded)
    total = 0
    for i, v in enumerate(expanded):
        if v == ".":
            continue

        total += i * int(v)

    return total


test = "2333133121414131402"
test = prep_data_2(test)

tp2 = part_2(test)
print(f"{tp2=}")
assert tp2 == 2858

other = prep_data_2("12345")
tp2_2 = part_2(other)
print(f"{tp2_2=}")
assert tp2_2 == 132

other = prep_data_2("14113")
tp2_2 = part_2(other)
print(f"{tp2_2=}")
assert tp2_2 == 16

other = prep_data_2("252")
tp2_2 = part_2(other)
print(f"{tp2_2=}")
assert tp2_2 == 5

other = prep_data_2("1010101010101010101010")
tp2_2 = part_2(other)
print(f"{tp2_2=}")
assert tp2_2 == 385

with open(f"data/09.txt", "r") as f:
    data = f.readline().replace("\n", "").strip()
    print(f"{len(data)=}")
    data = prep_data_2(data)

dp2 = part_2(data)
print(f"{dp2=}")
assert dp2 == 6381624803796
