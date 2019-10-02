def displayInventory(inventory):
    print('Inventory: ')
    i = 0
    for k,v in inventory.items():
        i += v
        print(str(v),str(k))
    print('Total number of items: ' + str(i))
        
newInventory = {'arrow' : 12,'gold coind' : 42,'rope' : 1,'torch' : 6, 'dagger' : 1}
displayInventory(newInventory)
