import requests, os, eel, pyperclip
from bs4 import BeautifulSoup


def download1(url, n):
    r = requests.get(url)
    if r.status_code == 200:
        filename = str(n) + '_' + url.split('/')[-1]
        with open(filename, 'wb')as f:
            f.write(r.content)


@eel.expose
def scrapyiff(link):
    r = requests.get(link)
    if r.status_code == 404:
        return 404
    soup = BeautifulSoup(r.text)
    dirname = soup.find('span', {'class': 'yp-info-name'}).get_text()
    os.mkdir(dirname)
    os.chdir(dirname)
    pages = int(soup.find('p', {'class': 'paginate-count'}).get_text().split('/')[-1].lstrip())
    alllinks = []
    for page in range(1, pages + 1):
        r = requests.get(link + '?p=' + str(page))
        soup = BeautifulSoup(r.text)
        post_files = [i.get('href') for i in soup.find_all('a', text='Post file')]
        soup = soup.find_all('p', {'style': 'margin-top:-15px;'})
        soup = '\n'.join([str(i) for i in soup])
        soup = BeautifulSoup(soup)
        soup = soup.find_all('a')
        pagelinks = [i.get('href') for i in soup]
        for i in post_files:
            if i not in pagelinks:
                pagelinks.append(i)
        alllinks += pagelinks
    for n, i in enumerate(alllinks):
        download1(i, n)
    os.chdir('..')
    return 'Готово'


@eel.expose
def paste():
    return pyperclip.paste()
