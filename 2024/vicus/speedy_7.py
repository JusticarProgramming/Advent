import cProfile
import pstats
import time
import logging
from concurrent.futures import ProcessPoolExecutor, as_completed

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_file(file_path):
    with open(file_path, 'r') as file:
        return [[int(result), list(map(int, values.split()))] for result, values in
                (line.strip().split(':') for line in file)]

def join_numbers(a, b):
    return int(f"{a}{b}")

def compute_expression(total, num, op):
    try:
        if op == "||":
            return join_numbers(total, num)
        elif op == "+":
            return total + num
        elif op == "*":
            return total * num
    except Exception as e:
        logging.error(f"Error in compute_expression: {e}")
        raise

def check_validity(ops, target, total, nums):
    if not nums:
        return total == target

    num = nums[0]
    for op in ops:
        new_total = compute_expression(total, num, op)
        if new_total <= target and check_validity(ops, target, new_total, nums[1:]):
            return True
    return False

def process_equation(equation, ops):
    target, nums = equation
    return target if check_validity(ops, target, nums[0], nums[1:]) else 0

def process_equations(data, ops):
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_equation, eq, ops) for eq in data]
        results = []
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as e:
                logging.error(f"Error in process_equations: {e}")
        return sum(results)

def main():
    start_time = time.time()

    input_data = parse_file('inout_07.txt')
    result = process_equations(input_data, ["+", "*", "||"])

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Result: {result}")
    print(f"Execution time: {execution_time} seconds")

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.strip_dirs().print_stats()
    stats.print_stats(10)  # Display the 10 slowest functions