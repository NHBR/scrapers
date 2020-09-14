import os,eel
from f import main, paste

eel.init(os.path.abspath('web'))
eel.start('main.html', size=(700,200))
