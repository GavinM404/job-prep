import os

def read_counter():
    file_path = "counter.txt"

    with open(file_path, "r") as file:
        counter_number = (file.read().strip() or 0)
        return counter_number


def counter():
    file_path = "counter.txt"

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            counter_number = 1
            file.write(str(counter_number))
            print(f'This script has been run {counter_number} times.')
    else:
        counter_number = read_counter()
        counter_number += 1
        print(counter_number)
        with open(file_path, "w") as file:
            file.write(str(counter_number))

            print(f'This script has been run {counter_number} times.')

counter()
