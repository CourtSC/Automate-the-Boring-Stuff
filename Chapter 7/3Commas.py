import re

stringNum = ['42', '1,234', '6,368,745', '12,34,567', '1234']
commaRegex = re.compile(r'''(
    ^\d{1,3}
    (,\d{3})*$
)''', re.VERBOSE)

matches = []
for s in stringNum:
    mo = commaRegex.search(s)
    if mo != None:
        print(mo.group())