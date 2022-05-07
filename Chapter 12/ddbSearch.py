#! python3
#! ddbSearch.py - Searches DNDBeyond.com based on args provided or clipboard.
#! https://www.dndbeyond.com/search?q=

import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    # Get search from args.
    search = ' '.join(sys.argv[1:])
else:
    # Get search from clipboard.
    search = pyperclip.paste()

webbrowser.open('https://www.dndbeyond.com/search?q=' + search)