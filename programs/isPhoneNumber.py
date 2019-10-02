import re

def searchPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    text = phoneNumRegex.findall(text)
    return text

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
numbers = searchPhoneNumber(message)
for i in range(len(numbers)):
    print('Phone number found: ' + numbers[i])
print('Done')
