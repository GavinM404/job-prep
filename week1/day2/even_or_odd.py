try:
    user_number = int(input('Pick a number: '))

    if user_number % 2 == 0:
        print(f'{user_number} is even!')
    else:
        print(f'{user_number} is odd!')
except ValueError:
    print('Please enter a valid number')
