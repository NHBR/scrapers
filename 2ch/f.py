import requests, bs4, os, eel, pyperclip


def download_one_media(url, n):
    r = requests.get(url)
    if r.status_code == 200:
        filename = str(n) + '_' + url.split('/')[-1]
        with open(filename, 'wb')as f:
            f.write(r.content)


@eel.expose
def download_all(link_2ch, checkbox_value):
    r = requests.get(link_2ch)
    if r.status_code == 404:
        return 404
    soup = bs4.BeautifulSoup(r.text)
    new_folder = ''.join(soup.find("span", {'class': 'post__title'}).get_text().strip().split('/'))
    if os.path.exists(new_folder):
        return 400
    else:
        os.mkdir(new_folder)
        os.chdir(new_folder)
    links = ['https://2ch.hk' + i.get('href') for i in soup.findAll("a", {"class": "post__image-link"})]
    for n, i in enumerate(links):
        download_one_media(i, n)
    if checkbox_value:
        html_file = new_folder + '.html'
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
            while links:
                f.write('''<div id='line'>''')
                for link in links[:3]:
                    if link.endswith('mp4'):
                        f.write(f"<video controls='controls'><source src='{link}' type='video/mp4;' "
                                f"codecs='avc1.42E01E, mp4a.40.2'></video>\n")
                    elif link.endswith('webm'):
                        f.write(f"<video controls='controls'><source src='{link}' type='video/webm;' "
                                f"codecs='avc1.42E01E, mp4a.40.2'></video>\n")
                    else:
                        f.write(f"<a href='{link}' target='_blank'><img src='{link}'></a>\n")
                f.write('</div><br>')
                if len(links) >= 3:
                    links = links[3:]
                else:
                    break
            f.write('</div>')
    os.chdir('..')


@eel.expose
def paste():
    return pyperclip.paste()
