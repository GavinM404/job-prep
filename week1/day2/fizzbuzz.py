# user_number = int(input('Please enter a number: '))

# while user_number > 0:
#     if user_number % 3 == 0 and user_number % 5 ==0:
#         print('FizzBuzz')
#     elif user_number % 5 == 0:
#         print('Buzz')
#     elif user_number % 3 == 0:
#         print('Fizz')
#     else:
#         print(user_number)
#     user_number -= 1

user_number = int(input('Please enter a number: '))

for n in range(1, user_number + 1):
    if n % 3 == 0 and n % 5 ==0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)
