#! python3
#!mapIt.py - Launches a map in the browser using and address from the command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.