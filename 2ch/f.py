import requests, bs4, webbrowser, os, eel, pyperclip


@eel.expose
def main(l2ch):
    r = requests.get(l2ch)
    if r.status_code == 404:
        return 404
    soup = bs4.BeautifulSoup(r.text)

    file = ''.join(soup.find("span", {'class': 'post__title'}).get_text().strip().split('/')) + '.html'

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
    with open(file, 'a') as f:
        f.write(f'<style type="text/css">{style} </style>')
        f.write('''<div id='cont'>''')
        links = ['https://2ch.hk' + i.get('href') for i in soup.findAll("a", {"class": "post__image-link"})]
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
        webbrowser.open('file://' + os.path.abspath(os.path.curdir) + '/' + file)


@eel.expose
def paste():
    return pyperclip.paste()
