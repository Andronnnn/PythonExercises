def spam(divideBy):
    try:
        return 42 /divideBy
    except ZeroDivisionError:
        print('error: invalid argument')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

print('******************************************************')
def bacon(divideBy):
        return 42 /divideBy
try:
    print(bacon(2))
    print(bacon(12))
    print(bacon(0))
    print(bacon(1))
except ZeroDivisionError:
        print('Error: Invalid argument')
