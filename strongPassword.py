'''
Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
'''

import re

requirements = '''
    Minimum 8 characters.
    Contains both upper and lowercase characters.
    Has at least one numerical digit.
'''

lengthRegex = re.compile(r'[a-zA-Z0-9]{8,}')
numRegex = re.compile(r'\d+')
lCaseRegex = re.compile(r'[a-z]+')
uCaseRegex = re.compile(r'[A-Z]+')

def passReq(password):
    reqList = []
    try:
        reqList.append(lengthRegex.search(password).group())
        reqList.append(numRegex.search(password).group())
        reqList.append(lCaseRegex.search(password).group())
        reqList.append(uCaseRegex.search(password).group())
        return True
    except:
        return False

print(requirements)
while passReq(input('Enter a password: ')) != True:
    print('Invalid password.')
    print(requirements)
# 'Password1', '111Leidos', 'LeidosPW99999'
# 'password', 'guest'