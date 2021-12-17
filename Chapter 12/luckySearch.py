#! python3
#! luckySearch.py - Searches google using provided arguments or clipboard and opens the top 5 results as new tabs.

import webbrowser, pyperclip, sys, requests_html, bs4

# Read command line args from sys.argv or the clipboard.
# Fetch search result page with requests module.
print('Googling...') # display text while downloading the Google page.
session = requests_html.HTMLSession()
if len(sys.argv) > 1:
    res = session.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
else:
    res = session.get('https://google.com/search?q=' + pyperclip.paste())
res.raise_for_status

# Find the links to each search result.
soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElems = soup.select('.yuRUbf a')

# Call the webbrowser.open() function to open the web browser.
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))