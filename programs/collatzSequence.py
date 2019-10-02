def collatz(collatzNumber):
    if int(collatzNumber) % 2 == 0:
        collatzNumber = int(collatzNumber) / 2
        return collatzNumber
    else:  
        return 3 * int(collatzNumber) + 1
    
print('Enter number:')
number = input()
while number != 1:
    number = collatz(number)
    print(str(number))
