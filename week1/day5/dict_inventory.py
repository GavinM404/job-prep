player_inventory = {"sword": 1, "potion": 1}

def add_item(inventory, item):
    inventory[item] = inventory.get(item, 0) + 1

def remove_item(inventory, item):
    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
    else:
        print(f'Cannot remove {item}, not in inventory or count is 0')
