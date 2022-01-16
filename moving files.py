import os
import sys
import time
import webbrowser
import re
import subprocess
import colorama
from colorama import Fore, Back, Style
import pathlib
from pathlib import Path
from os import environ, getcwd







getUser = lambda: environ['USERNAME']
a = getUser()


colorama.init()

bc2 = 'C:/Users/'+a+'/-для работы program-/'


try:
    d = 'c:/Users/'+a+'/-для работы program-'
    os.mkdir(d)
    print('         Папка -для работы program- создана в '+ d)
except FileExistsError:
    print("     Эта папка"+ colorama.Fore.CYAN+ ' уже '+ Style.RESET_ALL +'существует\n')
    time.sleep(3)
    


try:
        os.replace('c:/Users/'+a+'/Desktop/09/2.py', bc2+'2.py')
        print(' Файл переместил\n')
except FileNotFoundError:
        print(' Файла 2.py нет в папке 09\n')
try:
        os.replace('c:/Users/'+a+'/Desktop/09/mus.py', bc2+'mus.py')
        print(' Файл переместил\n')
except FileNotFoundError:
        print(' Файла mus.py нет в папке 09\n')


try:
        os.replace('c:/Users/'+a+'/Desktop/09/oksy.py', bc2+'oksy.py')
        print(' Файл переместил\n')
except FileNotFoundError:
        print(' Файла oksy.py нет в папке 09\n')
