import re

def read_and_process_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print("File content:")
    print(repr(content))  # Using repr() to show all characters including whitespace
    return content

filename = "day-3-input-data.txt"

content = read_and_process_file(filename)
ex2 = re.compile(r"mul\((?P<first>\d+),(?P<second>\d+)\)|don't\(\)|do\(\)")

total2 = 0  # Initialize sum variable
should_multiply = True  # Flag to track whether we should multiply

for match in ex2.finditer(content):
    matched_text = match.group(0)  # Get the full matched text
    print(f"Matched: {matched_text}")
    
    if matched_text == "don't()":
        print("Found don't()")
        should_multiply = False
        continue
    elif matched_text == "do()":
        print("Found do()")
        should_multiply = True
        continue
    
    if should_multiply:
        first = int(match.group('first'))
        second = int(match.group('second'))
        product = first * second
        print(f"Multiplying: {first} * {second} = {product}")
        total2 += product

print(f"Sum of all products: {total2}")