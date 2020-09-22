import os, eel
from f import download_all, paste

eel.init(os.path.abspath('web'))
eel.start('main.html', size=(700, 200))
