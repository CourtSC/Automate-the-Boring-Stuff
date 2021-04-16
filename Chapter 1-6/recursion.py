def recursionFunc(a_string):
    if len(a_string) > 0:
        return recursionFunc(a_string[:-1]) + a_string
    else:
        return ''
print(recursionFunc(str(input('Enter a string.\n'))))