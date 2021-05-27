#! python3
# madLibs.py - Prompts a user to fill in ADJECTIVE, NOUN, ADVERB, or VERB

import re

# For this excercise, I'm creating the madlibfile each time the function is run instead of manually creating a text file in windows.
madlibFile = open('madlib.txt', 'w') 
madlibFile.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')

# Create the mablibUser.txt file where the user's input will be stored each time the program is run.
madlibUserFile = open('madlibUser.txt', 'w')

# Detect the presence of "ADJECTIVE", "NOUN", "ADVERB", or "VERB".
madlibRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

# Read madlibfile and save all madlibs to a match object list.
madlibFile.close()
madlibFile = open('madlib.txt')
madlib = madlibFile.read()
mo = madlibRegex.findall(madlib) # List of regex matches

# Replace match objects with user input in new string.
for m in mo:
    if m == 'ADJECTIVE' or 'ADVERB':
        madlib = madlib.replace(m, input('Enter an ' + m.lower() + ':\n'), 1)
    else:
        madlib = madlib.replace(m, input('Enter a ' + m.lower() + ':\n'), 1)

# Print the madlib and save as a new text file.
print(madlib)
madlibUserFile.write(madlib)

# Close all files.
madlibFile.close()
madlibUserFile.close()