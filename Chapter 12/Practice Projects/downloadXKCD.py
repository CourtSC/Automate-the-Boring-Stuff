#! python3
#! downloadXKCD.py - A program to download XKCD Comics.

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    pass
    # Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicURL = 'https:' + comicElem[0].get('src')
        # Download the image.
        print(f'Downloading image {comicURL}...')
        res = requests.get(comicURL)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')