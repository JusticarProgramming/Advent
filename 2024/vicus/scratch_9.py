def is_rule_satisfied(rule: tuple[int, int], update: list[int]) -> bool:
    """Check if a single rule is satisfied within an update."""
    page_a, page_b = rule
    if page_a in update and page_b in update:
        return update.index(page_a) < update.index(page_b)
    return True  # If one of the pages is not in the update, the rule is trivially satisfied


def check_all_rules(rules: list[tuple[int, int]], update: list[int]) -> bool:
    """Check if all rules are satisfied for a given update."""
    for rule in rules:
        if not is_rule_satisfied(rule, update):
            return False
    return True


def filter_updates(rules: list[tuple[int, int]], updates: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    """Filter updates based on the rules."""
    valid_updates = []
    invalid_updates = []
    for update in updates:
        if check_all_rules(rules, update):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates


test_rules_data = [
    (47, 53), (97, 13), (97, 61), (97, 47), (75, 29), (61, 13), (75, 53),
    (29, 13), (97, 29), (53, 29), (61, 53), (97, 53), (61, 29), (47, 13),
    (75, 47), (97, 75), (47, 61), (75, 61), (47, 29), (75, 13), (53, 13),
]

test_data = [
    [75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13],
    [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47],
]


def get_middle_number_and_sum(valid_updates: list[list[int]]) -> int:
    """Find the middle number in the valid updates and calculate the sum."""
    total_sum = 0
    for update in valid_updates:
        middle_number = update[len(update) // 2]
        total_sum += middle_number
    return total_sum


test_valid_updates = filter_updates(test_rules_data, test_data)[0]
assert test_valid_updates == [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13]]
assert get_middle_number_and_sum(test_valid_updates) == 143
print(get_middle_number_and_sum(test_valid_updates))

file_path = 'scratch_4.txt'
rules = []
updates = []

with open(file_path, 'r') as file:
    data = file.read()
    # Split the data into rules and updates
    data = data.split('\n\n')
    # Split the data into rules and updates
    rules_data = data[0].split('\n')
    updates_data = data[1].split('\n')
    # Format the rules
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_data if rule]
    # Format the updates
    updates = [list(map(int, update.split(','))) for update in updates_data if update]

valid_updates, invalid_updates = filter_updates(rules, updates)
print(get_middle_number_and_sum(valid_updates))


# Use the rules to sort in invalid updates
def apply_rules_to_sort(update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    """Apply rules to sort the update list."""
    wrong = True
    while wrong:
        wrong = False
        for rule in rules:
            page_a, page_b = rule
            if page_a in update and page_b in update:
                index_a = update.index(page_a)
                index_b = update.index(page_b)
                if index_a > index_b:
                    # Swap the elements to satisfy the rule
                    update[index_a], update[index_b] = update[index_b], update[index_a]
                    wrong = True
    return update


# Apply the rules to sort each invalid update
sorted_invalid_updates = [apply_rules_to_sort(update, rules) for update in invalid_updates]

sorted_invalid_updates.sort(key=lambda update: update[0])

print(get_middle_number_and_sum(sorted_invalid_updates))
