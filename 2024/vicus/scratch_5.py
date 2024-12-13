
reports_dict = {}
with open('scratch_4.txt', 'r') as file:
    lines = file.read().split('\n')
    for i, line in enumerate(lines):
        reports_dict[f'report_{i + 1}'] = [int(x) for x in line.split()]

def is_safe(data):
    return ((all(data[i] < data[i + 1] for i in range(len(data) - 1)) or
            all(data[i] > data[i + 1] for i in range(len(data) - 1))) and
            all(abs(data[i] - data[i + 1]) <= 3 for i in range(len(data) - 1)))

def count_safe_reports(reports_dict):
    counter = 0
    for report in reports_dict:
        data = reports_dict[report]
        if is_safe(data):
            counter += 1
        else:
            for i in range(len(data)):
                temp = data[:i] + data[i + 1:]
                if is_safe(temp):
                    counter += 1
                    break
    return counter

print(count_safe_reports(reports_dict))