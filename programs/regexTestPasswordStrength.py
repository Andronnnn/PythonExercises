#! python3
#regexTestPasswordStrength.py - Test the strenth of a password
import re

def testPasswordStrength(password):
    # Check for 8 Character
    regexCharacterCount = re.compile(r'.{8,}')
    print(regexCharacterCount.search(password))
    
    # Search for a digit
    regexDigitSearch = re.compile(r'\d{1,}')
    print(regexDigitSearch.search(password))
    
     # Search uppercase letters
    regexUppercaseLetterSearch = re.compile(r'[A-Z]{1,}')
    print(regexUppercaseLetterSearch.search(password))
    
    # Search for lowercase letters
    regexLowercaseLetterSearch = re.compile(r'[a-z]{1,}')
    print(regexLowercaseLetterSearch.search(password))

    if regexCharacterCount.search(password) == None:
        print('Password is too short. It needs to be at least 8 characters.')
    elif regexDigitSearch.search(password) == None:
        print('Your password needs to contain at leat one digit.')
    elif regexUppercaseLetterSearch.search(password) == None:
        print('Your password needs to contain at least one uppercase letter.')
    elif regexLowercaseLetterSearch.search(password) == None:
        print('Your password needs to contain at least one lowercase letter.')
    else:
        print('Your password is strong enough.')
        
password = 'Tester123456'
testPasswordStrength(password)
