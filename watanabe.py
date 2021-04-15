'''
How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)
'''

import re

names = ['Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe', 'haruto Watanabe', 'Mr. Watanabe', 'Watanabe', 'Haruto watanabe']

# Match with a single word that starts with a capital letter.
# Match with the string Watanabe that starts with a capital letter.
watanabeRegex = re.compile(r'''(
    ^[A-Z]      # First letter of first name.
    [a-zA-Z]*   # Rest of the first name.
    [ ]         # Space
    Watanabe$   #Last name.
)''', re.VERBOSE)

for n in names:
    mo = watanabeRegex.search(n)
    if mo != None:
        print(mo.group())