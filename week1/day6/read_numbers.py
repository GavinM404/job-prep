# file_path = "numbers.txt"

# with open(file_path, 'r') as file:
#     lines = file.readlines()
#     for index, line in enumerate(lines):
#         lines[index] = line.strip()

file_path = "numbers.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(f'Number: {line.strip()} \tSquared: {int(line.strip()) **2 }')
