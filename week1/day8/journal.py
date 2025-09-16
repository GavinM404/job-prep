from datetime import datetime

def write_journal():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = input('Please enter journal entry: ')

    with open("journal.txt", "a") as file:
        file.write("Date: " + str(current_datetime) + "\n\n" + text +"\n\n")
        file.write("-" * 40 + "\n\n")

write_journal()


def read_journal():
    with open("journal.txt", "r") as file:
        journal = file.read()
        return journal

print(read_journal())
