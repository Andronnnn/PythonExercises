import random
r = random.randint(1,20)
number = 0
i = 0
print('I am thinking of a number between 1 and 20.')
while number != r:
    i = i + 1
    print('Take a guess')
    number = input()
    if int(number) < r:
        print('Your guess is too low.')
        continue
    elif int(number) > r:
        print('Your number is too high.')
        continue
    else:
        print('Good job! You guessed my number in' + str(i) + ' guesses!')
        break
