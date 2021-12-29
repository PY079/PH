import pyautogui
import time
import pathlib
from pathlib import Path
from os import environ, getcwd
import urllib.request
import time
import os
import sys


getUser = lambda: environ['USERNAME']
a = getUser()

print('     Ищу Yandex\n')
path = pathlib.Path('C:/Users/'+a+'/AppData/Local/Yandex')
if path.exists() == True:
    time.sleep(1)
    print('           Установка не требуется')
    time.sleep(5)
    sys.exit()
    
else:
    time.sleep(1)
    print('         Yandex нет\n')
    print('             Запускаю установку Yandex')
    time.sleep(3.5)
    os.system('cls')    




print('     Ищу Chrome')
path = pathlib.Path('C:/Program Files/Google/Chrome')
if path.exists() == True:
    time.sleep(1)
    print('             Нашёл')
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
    time.sleep(2)
    pyautogui.typewrite('chrome')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(1340, 90)
    time.sleep(3)
    pyautogui.click(502, 43) 
    pyautogui.typewrite('https://browser.yandex.ru/') #скачать яндекс
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(125, 469)
    time.sleep(2)
    pyautogui.click(196, 414)
    time.sleep(5)
    pyautogui.click(109, 697)
    time.sleep(3)
    pyautogui.click(722, 386)
    time.sleep(2)
    pyautogui.click(389, 495)
    time.sleep(1)
    pyautogui.click(920, 487)
    sys.exit()

    
else:
    time.sleep(1)
    print('                 Chrome нет\n')
    time.sleep(3.5)
    os.system('cls')
    
    
print('         Ищу FireFox')
path = pathlib.Path('C:/Program Files/Mozilla Firefox')
if path.exists() == True:
    time.sleep(1)
    print('                 Нашёл')
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
    time.sleep(2)
    pyautogui.typewrite('firefox')
    pyautogui.hotkey('enter')
    time.sleep(10)
    pyautogui.click(1339, 131)
    time.sleep(3)
    pyautogui.click(466, 64)
    pyautogui.typewrite('https://browser.yandex.ru/')
    pyautogui.hotkey('enter')
    time.sleep(3)
    pyautogui.click(124, 481)
    time.sleep(2)
    pyautogui.click(196, 414)
    time.sleep(6)
    pyautogui.click(746, 430)
    time.sleep(3)
    pyautogui.click(1303, 54) #открытие загрузок
    time.sleep(3)
    pyautogui.click(1034, 121)
    time.sleep(1) 
    pyautogui.click(722, 386)
    time.sleep(2)
    pyautogui.click(389, 495)
    time.sleep(1)
    pyautogui.click(920, 487)
    sys.exit()
else:
    time.sleep(1)
    print('         FireFox нет\n')
    time.sleep(3.5)
    os.system('cls')
    
print('         Ищу Opera')
path = pathlib.Path('C:/Users/'+ a +'/AppData/Local/Programs/Opera')
if path.exists() == True:
    time.sleep(1)
    print('                 Нашёл')
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
    time.sleep(2)
    pyautogui.typewrite('opera')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.click(499, 51)
    pyautogui.typewrite('https://browser.yandex.ru/')
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.click(164, 485)
    pyautogui.click(230, 422)
    time.sleep(6)
    pyautogui.click(82, 177)
    time.sleep(5)
    pyautogui.click(507, 445)
    time.sleep(5)
    pyautogui.click(1048, 131)
    pyautogui.click(1048, 131)
    time.sleep(6)
    pyautogui.click(731, 395)
    time.sleep(5)
    pyautogui.click(388, 500)
    time.sleep(5)
    pyautogui.click(925, 482)
    
    

else:
    time.sleep(1)
    print('         Opera нет\n')
    time.sleep(2)
    print('     Браузеров нет')
    time.sleep(3.5)
    os.system('cls')