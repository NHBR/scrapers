import requests, os, eel, pyperclip
from bs4 import BeautifulSoup


def download_one_media(url, n):
    r = requests.get(url)
    if r.status_code == 200:
        filename = str(n) + '_' + url.split('/')[-1]
        with open(filename, 'wb')as f:
            f.write(r.content)


@eel.expose
def download_all(link, checkbox_value):
    r = requests.get(link)
    if r.status_code == 404:
        return 404
    soup = BeautifulSoup(r.text)
    dirname = soup.find('span', {'class': 'yp-info-name'}).get_text()
    if os.path.exists(dirname):
        return 400
    else:
        os.mkdir(dirname)
        os.chdir(dirname)
    pages = int(soup.find('p', {'class': 'paginate-count'}).get_text().split('/')[-1].lstrip())
    all_links = []
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
        all_links += pagelinks
    for n, i in enumerate(all_links):
        download_one_media(i, n)
    if checkbox_value:
        html_file = dirname + '.html'
        style = '''
                body{text-align: center;
                     background-color: #333;}

                img{margin-bottom: 20px;
                    margin-left: 20px;

                    border: groove;
                    width: 300px;}
                video{margin-bottom: 20px;
                    margin-left: 20px;
                    border: groove;
                    width: 300px;}
                #cont{
                    margin: 0 auto;
                    width: 1200px;}
            '''
        with open(html_file, 'a') as f:
            f.write(f'<style type="text/css">{style} </style>')
            f.write('''<div id='cont'>''')
            while all_links:
                f.write('''<div id='line'>''')
                for link in all_links[:3]:
                    if link.endswith('mp4'):
                        f.write(f"<video controls='controls'><source src='{link}' type='video/mp4;' "
                                f"codecs='avc1.42E01E, mp4a.40.2'></video>\n")
                    elif link.endswith('webm'):
                        f.write(f"<video controls='controls'><source src='{link}' type='video/webm;' "
                                f"codecs='avc1.42E01E, mp4a.40.2'></video>\n")
                    else:
                        f.write(f"<a href='{link}' target='_blank'><img src='{link}'></a>\n")
                f.write('</div><br>')
                if len(all_links) >= 3:
                    all_links = all_links[3:]
                else:
                    break
            f.write('</div>')
    os.chdir('..')
    return 'Done'


@eel.expose
def paste():
    return pyperclip.paste()
