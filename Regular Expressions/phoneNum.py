import re

phoneNumRegex = re.compile(r'''(  # find phone number in any commonly used format with or without an area code.
    ((\()?\d{3}(\))?)  # area code with or without parentheses.
    (\s|-|\.)?  # separator.
    \d{3}  # first 3 digits.
    (\s|-|\.)?  # separator.
    \d{4}  # last 4 digits.
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension.
    )''', re.VERBOSE)

mo = phoneNumRegex.search('My number is 415-555-4242 x99.') # call search() on phoneNumRegex and pass the string we want to search for the regex object in phoneNumRegex.
print('Phone number found: ' + mo.group()) # print the Match Object
print(mo.group(1))
print(mo.group(2))
print(mo.groups())