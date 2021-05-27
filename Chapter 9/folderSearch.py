#! python3
# folderSearch.py - A program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression.

from pathlib import Path
import random, re

# Create files with random number sequences
for f in range(5):
    numFile = open(f'file {f + 1}.txt', 'w')
    for n in range(1000):
        numFile.write(str(random.randint(0,9)))
    numFile.close()

# Get a list of all text files in a folder.
p = Path.cwd() # Change this to the directory you want to search or to prompt for user input.
pathList = list(p.glob('*.txt')) # List of all .txt files as Path objects.

# Check each file for the user-supplied regex and print results with file name.
searchStr = input('Enter a search string: ')
print('')
for p in pathList:
    data = p.open().readline()
    matchList = re.findall(searchStr, data) # Get a list of matches.
    matchIndices = [m.start() for m in re.finditer(searchStr, data)] # Get a list of indices for matches.
    if len(matchList) == 0:
        print(f'No matches found in {p.name}.\n')
    else:
        print(f'{len(matchList)} matches found in {p.name}.')
        for i, m in enumerate(matchList):
            print(f'{m} found at index {matchIndices[i]}.')
        print('')