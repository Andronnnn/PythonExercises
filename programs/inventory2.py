def addToInventory(inventory, addedItems):
    for i in addedItems:
        itemCount = inventory.get(i,0)
        if itemCount == 0:
            inventory[i] = 1
        else:
            inventory[i] += 1
    return inventory

def displayInventory(inventory):
    print('Inventory: ')
    i = 0
    for k,v in inventory.items():
        i += v
        print(str(v),str(k))
    print('Total number of items: ' + str(i))

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = {'gold coin' : 42,'rope' : 1}
inv = addToInventory(inv,dragonLoot)
displayInventory(inv)
