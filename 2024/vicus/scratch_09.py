def reorder_data(expanded_data, part=1):
    if part == 1:
        flat_data = [item for sublist in expanded_data.values() for item in sublist]
        last_number_index = None
        last_number = None

        for index in range(len(flat_data) - 1, -1, -1):
            if flat_data[index].isnumeric():
                last_number_index = index
                last_number = flat_data[index]
                break

        for index, char in enumerate(flat_data):
            if char == '.':
                if last_number_index is None or last_number_index < index:
                    break
                flat_data[index] = last_number
                flat_data[last_number_index] = '.'
                last_number_index -= 1
                while last_number_index >= 0 and not flat_data[last_number_index].isnumeric():
                    last_number_index -= 1
                if last_number_index >= 0:
                    last_number = flat_data[last_number_index]
        return flat_data


    elif part == 2:
        for num_index in range(len(expanded_data) - 1, -1, -1):
            num_list = expanded_data[num_index]
            if "." in num_list:
                continue
            for index, char_list in enumerate(expanded_data[:num_index]):
                if "." in char_list:
                    size_diff = len(char_list) - len(num_list)
                    if size_diff >= 0:
                        expanded_data[num_index] = ["."] * len(num_list)
                        expanded_data[index] = num_list + ["."] * size_diff
                        break
        return [char for sublist in expanded_data.values() for char in sublist]


def part_1(data):
    formatted_data = format_input_data(data)
    string_data = expand_data(formatted_data)
    ordered_string_data = reorder_data(string_data, part=1)
    return calculate_checksum(ordered_string_data)


def part_2(data):
    formatted_data = format_input_data(data)
    string_data = expand_data(formatted_data)
    ordered_string_data = reorder_data(string_data, part=2)
    return calculate_checksum(ordered_string_data)


def calculate_checksum(ordered_data):
    return sum(int(data) * index for index, data in enumerate(ordered_data) if data.isnumeric())


def format_input_data(data):
    return [int(d) for d in str(data)]


def expand_data(formatted_data):
    expanded_data = {}
    counter = 0
    for index, data in enumerate(formatted_data):
        if index % 2 == 0:
            expanded_data[index] = [str(counter)] * data
            counter += 1
        else:
            expanded_data[index] = ['.'] * data
    return expanded_data


def read_input_file(file):
    with open(file, 'r') as f:
        return f.read()


def check_remaining_numbers(data, index):
    return any(d.isnumeric() for d in data[index:])
