#! python3
#! SNOW.py - Searches Service Now based on args provided or clipboard.
#! https://servicenow.adventhealth.com/nav_to.do?uri=%2F$sn_global_search_results.do%3Fsysparm_search%3D

import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    # Get search from args.
    search = ' '.join(sys.argv[1:])
else:
    # Get search from clipboard.
    search = pyperclip.paste()

webbrowser.open('https://servicenow.adventhealth.com/nav_to.do?uri=%2F$sn_global_search_results.do%3Fsysparm_search%3D' + search)