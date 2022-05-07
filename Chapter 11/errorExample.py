
from traceback import format_exc

def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

try:
    spam()
except:
    with open('errorInfo.txt', 'w') as errorFile:
        errorFile.write(format_exc())
    print('The traceback info was written to errorInfo.txt')