'''
Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
'''

import re

def regexStrip(someString, chars=' '):
    # If no chars are passed, remove whitespace
    return someString.strip(chars)

print(regexStrip('     A     '))