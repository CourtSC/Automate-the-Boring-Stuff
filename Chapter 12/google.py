#! python3
#!mapIt.py - Launches a google search from the command line or clipboard
#! https://www.google.com/search?q=

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    search = ' '.join(sys.argv[1:])
else:
    # Get address for clipboard.
    search = pyperclip.paste()

webbrowser.open('https://www.google.com/search?q=' + search)