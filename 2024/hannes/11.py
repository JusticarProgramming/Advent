# %%
from functools import cache
from collections import Counter, defaultdict

test = [125, 17]

data = [510613,358,84,40702,4373582,2,0,1584]


@cache
def create(num):
    if num == 0:
        return [1]

    char = str(num)
    length = len(char)
    if length % 2 == 0:
        half = int(length / 2)
        return [int(char[:half]), int(char[half:])]

    return [num * 2024]


def run(data, blinks):
    counter = Counter(data)
    temp = defaultdict(int)
    temp.update(counter)

    for i in range(blinks):
        print(f"{i}/{blinks}", end="\r")

        numbers = temp.copy()
        temp = defaultdict(int)

        for key in numbers:
            result = create(key)
            for r in result:
                temp[r] += numbers[key]

    return sum(temp.values())


tp1 = run(test, 25)
print(f"{tp1=}")
assert tp1 == 55312

dp1 = run(data, 25)
print(f"{dp1=}")
# assert dp1 == 200446

dp2 = run(data, 75)
print(f"{dp2=}")
