

def shopping_list():

    grocery_list = []

    print('Welcome to the grocery list function')

    while True:
        grocery_item = input('What would you like to put in your list? Type "done" to be finished ')

        if grocery_item.lower() == 'done':
            print(' Your grocery list: ' + ", ".join(grocery_list))
            print('Thanks for using the grocery function')
            break
        else:
            grocery_list.append(grocery_item)

shopping_list()
