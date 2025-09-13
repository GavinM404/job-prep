file_name = "numbers.txt"

with open(file_name, "w") as file_object:
    how_many = int(input("How many numbers would you like to write to the file? "))

    for num in range(1, how_many + 1):
        file_object.write(f'{num}\n')
