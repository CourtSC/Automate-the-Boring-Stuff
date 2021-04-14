import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # pass desired pattern to re.compile and store the resulting regex object in phoneNumRegex variable. 
mo = phoneNumRegex.search('My number is 415-555-4242.') # call search() on phoneNumRegex and pass the string we want to search for the regex object in phoneNumRegex.
print('Phone number found: ' + mo.group()) # print the Match Object

phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

phoneNumRegex = re.compile(r'(((\()?\d{3}(\))?)( |-))?(\d{3}( |-)\d{4})') # find phone number in any commonly used format with or without an area code.
