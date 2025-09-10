print('Welcome to the tip calculator.')
total = float(input('What was the total bill? '))
tip = int(input('How much would you like to tip? 10 12 15 20 25? '))
the_split = int(input('How many people are splitting the bill? '))

final_total = (total * (tip/100 + 1)) / the_split

print(f'Each person should pay: {round(final_total, 2):.2f}')
