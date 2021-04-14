import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # pass desired pattern to re.compile and store the resulting regex object in phoneNumRegex variable. 
mo = phoneNumRegex.search('My number is 415-555-4242.') # call search() on phoneNumRegex and pass the string we want to search for the regex object in phoneNumRegex.
print('Phone number found: ' + mo.group()) # print the Match Object

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

phoneNumRegex = re.compile(r'((\()?\d{3}(\))?)( |-)(\d{3}( |-)\d{4})') # find phone number in any commonly used format

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())