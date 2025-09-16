def write_todo():
    with open("todo.txt", "w") as file:
        count = 0
        while True:
            text = input("Add a todo or type done: ")

            if text.lower() == "done":
                break

            count += 1
            file.write(f'{count}: {text} \n')


write_todo()

def read_todo():
    with open("todo.txt", "r") as file:
        todo = file.read()
        return todo

print(read_todo())
