reports_dict = {}
with open('scratch_4.txt', 'r') as file:
    lines = file.read().split('\n')
    for i, line in enumerate(lines):
        reports_dict[f'report_{i + 1}'] = [int(x) for x in line.split()]
counter = 0
for report in reports_dict:
    data = reports_dict[report]
    if all(data[i] < data[i + 1] for i in range(len(data) - 1)) or all(data[i] > data[i + 1] for i in range(len(data) - 1)):
        if all(abs(data[i] - data[i + 1]) <= 3 for i in range(len(data) - 1)):
            counter += 1
    else:
        safe = False
        for i in range(len(data)):
            temp = data[:i] + data[i + 1:]
            if (all(temp[j] < temp[j + 1] for j in range(len(temp) - 1)) or all(temp[j] > temp[j + 1] for j in range(len(temp) - 1))) and all(abs(temp[j] - temp[j + 1]) <= 3 for j in range(len(temp) - 1)):
                safe = True
                break
        if safe:
            counter += 1
print(counter)