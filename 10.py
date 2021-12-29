
import pyautogui
import time
import pathlib
from pathlib import Path
from os import environ, getcwd
import urllib.request
import time
import os
import sys
from PIL import Image





getUser = lambda: environ['USERNAME']
user = getUser()



print('     Ищу Kinoplay')                          #проверка на существование kinoplay
path = pathlib.Path('C:/Program Files/Kinoplay')
if path.exists() == True:
    time.sleep(1)
    print('             Установка не нужна\n')
    
    
else:
    print('\n   Ищу Yandex')
    time.sleep(1)
    path = pathlib.Path('C:/Users/'+ a +'/AppData/Local/Yandex')
    if path.exists() == True:
            time.sleep(1)
            print('             Нашёл Yandex\n')
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.hotkey('shift', 'alt') #сменя языка на русский
            pyautogui.hotkey('shift', 'alt') #сменя языка на англ
            time.sleep(2)
            pyautogui.typewrite('yandex')
            pyautogui.press('enter')
            time.sleep(15)
            pyautogui.click(1303, 24) #окно во весь экран
            time.sleep(2)
            pyautogui.click(502, 43) #строка поиска
            pyautogui.typewrite('https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg?hl=ru')
            pyautogui.press('enter')
            time.sleep(8)
            pyautogui.click(1141, 260) #нажать на установить
            time.sleep(7)
            pyautogui.click(672, 255)  # нажимает установить расширение
            time.sleep(30)
            pyautogui.click(1349, 95) #закрыть диалогово окно
            time.sleep(6)
            pyautogui.click(502, 43) #строка поиска
            time.sleep(3)
            pyautogui.typewrite('chrome-extension://bgnkhhnnamicmpeenaelnjfhikgbkllg/pages/options.html')
            pyautogui.press('enter')
            time.sleep(6)
            pyautogui.click(434, 193) #клик в пустоту
            time.sleep(1)
            pyautogui.click(246, 337)
            time.sleep(2)
            pyautogui.scroll (-600) # прокрутить вниз
            time.sleep(3)
            pyautogui.click(1131, 502)#x потом y; чем ниже y тем выше поднимается, ЧЕМ НИЖЕ X , тем левеее
            time.sleep(30)
            pyautogui.click(502, 43) #строка поиска
            time.sleep(5)
            pyautogui.typewrite('https://disk.yandex.ru/d/ydU5WsPq7JubQQ')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.click(200, 311)
            time.sleep(1)
            pyautogui.scroll (-600) # прокрутить вниз
            time.sleep(1)
            pyautogui.click(802, 479)
            
            
            while True:
                path = pathlib.Path('C:/Users/User/Downloads/Kinoplay.msi')
                if path.exists() == False:
                    time.sleep(10)
                else:
                    pyautogui.hotkey('win')
                    time.sleep(4)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    time.sleep(4)
                    pyautogui.typewrite('ghjdjlybr')
                    pyautogui.press('enter')
                    time.sleep(4)
                    pyautogui.click(59, 148)
                    time.sleep(4)
                    pyautogui.click(1254, 36)
                    time.sleep(4)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(3)
                    pyautogui.doubleClick(224, 165)
                    time.sleep(10)
                    pyautogui.click(773, 381)
                    time.sleep(5)
                    pyautogui.click(792, 529)
                    time.sleep(5)
                    pyautogui.click(792, 529)
                    time.sleep(5)
                    pyautogui.click(792, 529)
                    time.sleep(35)
                    pyautogui.click(788, 531) 
                    break

            









    
while True:
    os.chdir (r'C:/Users/'+user+'/Downloads/')
    print('\n')
    print(' Что нужно скачать:')
    print('     1. Импровизация, 2.Фильмы MARVEL\n')
    a = input('    Введите номер --> ')
    if a == '1':
        print('\n   Сезоны:')
        print(' 1\n 2 \n 3 \n 4 \n 5 \n 6 \n 7 \n 8\n')
        imp = input('   Выберите сезон --> ')
        if imp == '1':
            print('\n   1 сезон весит - 18.748 мб')
            print(' Серии: ')
            print(' 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n 11\n 12\n 13\n 14\n 15\n 16\n 17\n 18\n 19\n 20\n')
            im = input('    Выберите серию --> ')
            if im == '1':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(2)
                    pyautogui.click(1175, 52)
                    time.sleep(1)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)

                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    a = pyautogui.locateOnScreen("скачать.png")
                    print(a) #кнопка скачать
                    pyautogui.click(a)
                    time.sleep(1)   
                    
                    a1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(a1) #копка скачать
                    pyautogui.click(a1)
                    time.sleep(5) 
                   
                    a2 = pyautogui.locateOnScreen("1 серия.png")
                    print(a2) #копка скачать
                    pyautogui.click(a2)
                    time.sleep(4)   
                   
                    a3 = pyautogui.locateOnScreen("720.png")
                    print(a3) #копка скачать
                    pyautogui.click(a3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
    
            
            if im == '2':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(1)
                    pyautogui.click(1175, 52)
                    time.sleep(0.5)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    b = pyautogui.locateOnScreen("скачать.png")
                    print(b) #копка скачать
                    pyautogui.click(b)
                    time.sleep(1)
                    
                    b1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(b1) #копка скачать
                    pyautogui.click(b1)
                    time.sleep(1)
                    
                    b2 = pyautogui.locateOnScreen("2 серия.png")
                    print(b2) #копка скачать
                    pyautogui.click(b2)
                    time.sleep(1)
                    
                    b3 = pyautogui.locateOnScreen("720.png")
                    print(b3) #копка скачать
                    pyautogui.click(b3)
                
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            if im == '3':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    c = pyautogui.locateOnScreen("скачать.png")
                    print(c) #копка скачать
                    pyautogui.click(c)
                    time.sleep(1)
                    
                    c1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(c1) #копка скачать
                    pyautogui.click(c1)
                    time.sleep(1)
                    
                    c2 = pyautogui.locateOnScreen("3 серия.png")
                    print(c2) #копка скачать
                    pyautogui.click(c2)
                    time.sleep(1)
                    
                    c3 = pyautogui.locateOnScreen("720.png")
                    print(c3) #копка скачать
                    pyautogui.click(c3)
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка       
            
            
            if im == '4':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                  
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    d = pyautogui.locateOnScreen("скачать.png")
                    print(d) #копка скачать
                    pyautogui.click(d)
                    time.sleep(1)
                    
                    d1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(d1) #копка скачать
                    pyautogui.click(d1)
                    time.sleep(1)
                    
                    d2 = pyautogui.locateOnScreen("4 серия.png")
                    print(d2) #копка скачать
                    pyautogui.click(d2)
                    time.sleep(1)
                    
                    d3 = pyautogui.locateOnScreen("720.png")
                    print(d3) #копка скачать
                    pyautogui.click(d3)
                  
                  
                  
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            
            if im == '5':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    e = pyautogui.locateOnScreen("скачать.png")
                    print(e) #копка скачать
                    pyautogui.click(e)
                    time.sleep(1)
                    
                    e1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(e1) #копка скачать
                    pyautogui.click(e1)
                    time.sleep(1)
                    
                    e2 = pyautogui.locateOnScreen("5 серия.png")
                    print(e2) #копка скачать
                    pyautogui.click(e2)
                    time.sleep(1)
                    
                    e3 = pyautogui.locateOnScreen("720.png")
                    print(e3) #копка скачать
                    pyautogui.click(e3)
                    
                    
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '6':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    f = pyautogui.locateOnScreen("скачать.png")
                    print(f) #копка скачать
                    pyautogui.click(f)
                    time.sleep(1)
                    
                    f1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(f1) #копка скачать
                    pyautogui.click(f1)
                    time.sleep(4)
                    
                    f2 = pyautogui.locateOnScreen("6 серия.png")
                    print(f2) #копка скачать
                    pyautogui.click(f2)
                    time.sleep(1)
                    
                    f3 = pyautogui.locateOnScreen("720.png")
                    print(f3) #копка скачать
                    pyautogui.click(f3)
                    
                    
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка        
                    
                    
                
            
            if im == '7':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    g = pyautogui.locateOnScreen("скачать.png")
                    print(g) #копка скачать
                    pyautogui.click(g)
                    time.sleep(1)
                    
                    g1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(g1) #копка скачать
                    pyautogui.click(g1)
                    time.sleep(4)
                    
                    g2 = pyautogui.locateOnScreen("7 серия.png")
                    print(g2) #копка скачать
                    pyautogui.click(g2)
                    time.sleep(1)
                    
                    g3 = pyautogui.locateOnScreen("720.png")
                    print(g3) #копка скачать
                    pyautogui.click(g3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab')
                    time.sleep(5)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            if im == '8':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    h = pyautogui.locateOnScreen("скачать.png")
                    print(h) #копка скачать
                    pyautogui.click(h)
                    time.sleep(1)
                    
                    h1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(h1) #копка скачать
                    pyautogui.click(h1)
                    time.sleep(4)
                    
                    h2 = pyautogui.locateOnScreen("8 серия.png")
                    print(h2) #копка скачать
                    pyautogui.click(h2)
                    time.sleep(1)
                    
                    h3 = pyautogui.locateOnScreen("720.png")
                    print(h3) #копка скачать
                    pyautogui.click(h3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            
            
            if im == '9':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    i = pyautogui.locateOnScreen("скачать.png")
                    print(i) #копка скачать
                    pyautogui.click(i)
                    time.sleep(1)
                    
                    i1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(i1) #копка скачать
                    pyautogui.click(i1)
                    time.sleep(4)
                    
                    i2 = pyautogui.locateOnScreen("9 серия.png")
                    print(i2) #копка скачать
                    pyautogui.click(i2)
                    time.sleep(1)
                    
                    i3 = pyautogui.locateOnScreen("720.png")
                    print(i3) #копка скачать
                    pyautogui.click(i3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
            
            
            
            if im == '10':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    j = pyautogui.locateOnScreen("скачать.png")
                    print(j) #копка скачать
                    pyautogui.click(j)
                    time.sleep(1)
                    
                    j1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(j1) #копка скачать
                    pyautogui.click(j1)
                    time.sleep(4)
                    
                    j2 = pyautogui.locateOnScreen("10 серия.png")
                    print(j2) #копка скачать
                    pyautogui.click(j2)
                    time.sleep(1)
                    
                    j3 = pyautogui.locateOnScreen("720.png")
                    print(j3) #копка скачать
                    pyautogui.click(j3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            
            if im == '11':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    k = pyautogui.locateOnScreen("скачать.png")
                    print(k) #копка скачать
                    pyautogui.click(k)
                    time.sleep(1)
                    k1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(k1) #копка скачать
                    pyautogui.click(k1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    k2 = pyautogui.locateOnScreen("11 серия.png")
                    print(k2) #копка скачать
                    pyautogui.click(k2)
                    time.sleep(1)
                    
                    k3 = pyautogui.locateOnScreen("720.png")
                    print(k3) #копка скачать
                    pyautogui.click(k3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            
            if im == '12':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    l = pyautogui.locateOnScreen("скачать.png")
                    print(l) #копка скачать
                    pyautogui.click(l)
                    time.sleep(1)
                    l1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(l1) #копка скачать
                    pyautogui.click(l1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    l2 = pyautogui.locateOnScreen("12 серия.png")
                    print(l2) #копка скачать
                    pyautogui.click(l2)
                    time.sleep(1)
                    
                    l3 = pyautogui.locateOnScreen("720.png")
                    print(l3) #копка скачать
                    pyautogui.click(l3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
            if im == '13':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    m = pyautogui.locateOnScreen("скачать.png")
                    print(m) #копка скачать
                    pyautogui.click(m)
                    time.sleep(1)
                   
                    k1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(m) #копка скачать
                    pyautogui.click(m)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    m2 = pyautogui.locateOnScreen("13 серия.png")
                    print(m2) #копка скачать
                    pyautogui.click(m2)
                    time.sleep(1)
                    
                    m3 = pyautogui.locateOnScreen("720.png")
                    print(m3) #копка скачать
                    pyautogui.click(m3)
                    
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
            if im == '14':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    n = pyautogui.locateOnScreen("скачать.png")
                    print(n) #копка скачать
                    pyautogui.click(n)
                    time.sleep(1)
                    
                    n1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(n1) #копка скачать
                    pyautogui.click(n1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    n2 = pyautogui.locateOnScreen("14 серия.png")
                    print(n2) #копка скачать
                    pyautogui.click(n2)
                    time.sleep(1)
                    
                    n3 = pyautogui.locateOnScreen("720.png")
                    print(n3) #копка скачать
                    pyautogui.click(n3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '15':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    o = pyautogui.locateOnScreen("скачать.png")
                    print(o) #копка скачать
                    pyautogui.click(o)
                    time.sleep(1)
                    
                    o1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(o1) #копка скачать
                    pyautogui.click(o1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    
                    o2 = pyautogui.locateOnScreen("15 серия.png")
                    print(o2) #копка скачать
                    pyautogui.click(o2)
                    time.sleep(1)
                    
                    o3 = pyautogui.locateOnScreen("720.png")
                    print(o3) #копка скачать
                    pyautogui.click(o3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '16':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    p = pyautogui.locateOnScreen("скачать.png")
                    print(p) #копка скачать
                    pyautogui.click(p)
                    time.sleep(1)
                    
                    p1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(p1) #копка скачать
                    pyautogui.click(p1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    p2 = pyautogui.locateOnScreen("16 серия.png")
                    print(p2) #копка скачать
                    pyautogui.click(p2)
                    time.sleep(1)
                    
                    p3 = pyautogui.locateOnScreen("720.png")
                    print(p3) #копка скачать
                    pyautogui.click(p3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '17':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    q = pyautogui.locateOnScreen("скачать.png")
                    print(q) #копка скачать
                    pyautogui.click(q)
                    time.sleep(1)
                    
                    q1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(q1) #копка скачать
                    pyautogui.click(q1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    q2 = pyautogui.locateOnScreen("17 серия.png")
                    print(q2) #копка скачать
                    pyautogui.click(q2)
                    time.sleep(1)
                    
                    q3 = pyautogui.locateOnScreen("720.png")
                    print(q3) #копка скачать
                    pyautogui.click(q3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '18':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    r = pyautogui.locateOnScreen("скачать.png")
                    print(r) #копка скачать
                    pyautogui.click(r)
                    time.sleep(1)
                    
                    r1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(r1) #копка скачать
                    pyautogui.click(r1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    r2 = pyautogui.locateOnScreen("18 серия.png")
                    print(r2) #копка скачать
                    pyautogui.click(r2)
                    time.sleep(1)
                    
                    r3 = pyautogui.locateOnScreen("720.png")
                    print(r3) #копка скачать
                    pyautogui.click(r3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '19':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    s = pyautogui.locateOnScreen("скачать.png")
                    print(s) #копка скачать
                    pyautogui.click(s)
                    time.sleep(1)
                    
                    s1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(s1) #копка скачать
                    pyautogui.click(s1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    s2 = pyautogui.locateOnScreen("19 серия.png")
                    print(s2) #копка скачать
                    pyautogui.click(s2)
                    time.sleep(1)
                    
                    s3 = pyautogui.locateOnScreen("720.png")
                    print(s3) #копка скачать
                    pyautogui.click(s3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '20':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    t = pyautogui.locateOnScreen("скачать.png")
                    print(t) #копка скачать
                    pyautogui.click(t)
                    time.sleep(1)
                    
                    t1 = pyautogui.locateOnScreen("сезон 1.png")
                    print(t1) #копка скачать
                    pyautogui.click(t1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    t2 = pyautogui.locateOnScreen("20 серия.png")
                    print(t2) #копка скачать
                    pyautogui.click(t2)
                    time.sleep(1)
                    
                    t3 = pyautogui.locateOnScreen("720.png")
                    print(t3) #копка скачать
                    pyautogui.click(t3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
                #       старый код
                 #    1225 строк - сезон   
                    #2 сезон
                    
        if imp == '2':
            print(' Серии: ')
            print(' 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n 11\n 12\n 13\n 14\n 15\n 16\n 17\n 18\n 19\n ')
            im = input('    Выберите серию --> ')
            if im == '1':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(2)
                    pyautogui.click(1175, 52)
                    time.sleep(1)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    aa = pyautogui.locateOnScreen("скачать.png")
                    print(aa) #кнопка скачать
                    pyautogui.click(aa)
                    time.sleep(1)   
                    
                    aa1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(aa1) #копка скачать
                    pyautogui.click(aa1)
                    time.sleep(5) 
                   
                    aa2 = pyautogui.locateOnScreen("1 серия.png")
                    print(aa2) #копка скачать
                    pyautogui.click(aa2)
                    time.sleep(4)   
                   
                    aa3 = pyautogui.locateOnScreen("720.png")
                    print(aa3) #копка скачать
                    pyautogui.click(aa3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
    
            
            if im == '2':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(1)
                    pyautogui.click(1175, 52)
                    time.sleep(0.5)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    bb = pyautogui.locateOnScreen("скачать.png")
                    print(bb) #копка скачать
                    pyautogui.click(bb)
                    time.sleep(1)
                    
                    bb1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(bb1) #копка скачать
                    pyautogui.click(bb1)
                    time.sleep(1)
                    
                    bb2 = pyautogui.locateOnScreen("2 серия.png")
                    print(bb2) #копка скачать
                    pyautogui.click(bb2)
                    time.sleep(1)
                    
                    bb3 = pyautogui.locateOnScreen("720.png")
                    print(bb3) #копка скачать
                    pyautogui.click(bb3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            if im == '3':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    cc = pyautogui.locateOnScreen("скачать.png")
                    print(cc) #копка скачать
                    pyautogui.click(cc)
                    time.sleep(1)
                    
                    cc1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(cc1) #копка скачать
                    pyautogui.click(cc1)
                    time.sleep(1)
                    
                    cc2 = pyautogui.locateOnScreen("3 серия.png")
                    print(cc2) #копка скачать
                    pyautogui.click(cc2)
                    time.sleep(1)
                    
                    cc3 = pyautogui.locateOnScreen("720.png")
                    print(cc3) #копка скачать
                    pyautogui.click(cc3)
                    
                
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            if im == '4':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                  
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    dd = pyautogui.locateOnScreen("скачать.png")
                    print(dd) #копка скачать
                    pyautogui.click(dd)
                    time.sleep(1)
                    
                    dd1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(dd1) #копка скачать
                    pyautogui.click(dd1)
                    time.sleep(1)
                    
                    dd2 = pyautogui.locateOnScreen("4 серия.png")
                    print(dd2) #копка скачать
                    pyautogui.click(dd2)
                    time.sleep(1)
                    
                    dd3 = pyautogui.locateOnScreen("720.png")
                    print(dd3) #копка скачать
                    pyautogui.click(dd3)
                  
                  

                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            
            if im == '5':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    ee = pyautogui.locateOnScreen("скачать.png")
                    print(ee) #копка скачать
                    pyautogui.click(ee)
                    time.sleep(1)
                    
                    ee1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(ee1) #копка скачать
                    pyautogui.click(ee1)
                    time.sleep(1)
                    
                    ee2 = pyautogui.locateOnScreen("5 серия.png")
                    print(ee2) #копка скачать
                    pyautogui.click(ee2)
                    time.sleep(1)
                    
                    ee3 = pyautogui.locateOnScreen("720.png")
                    print(ee3) #копка скачать
                    pyautogui.click(ee3)
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '6':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ff = pyautogui.locateOnScreen("скачать.png")
                    print(ff) #копка скачать
                    pyautogui.click(ff)
                    time.sleep(1)
                    
                    ff1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(ff1) #копка скачать
                    pyautogui.click(ff1)
                    time.sleep(4)
                    
                    ff2 = pyautogui.locateOnScreen("6 серия.png")
                    print(ff2) #копка скачать
                    pyautogui.click(ff2)
                    time.sleep(1)
                    
                    ff3 = pyautogui.locateOnScreen("720.png")
                    print(ff3) #копка скачать
                    pyautogui.click(ff3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                
            
            if im == '7':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    gg = pyautogui.locateOnScreen("скачать.png")
                    print(gg) #копка скачать
                    pyautogui.click(gg)
                    time.sleep(1)
                    
                    gg1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(gg1) #копка скачать
                    pyautogui.click(gg1)
                    time.sleep(4)
                    
                    gg2 = pyautogui.locateOnScreen("7 серия.png")
                    print(gg2) #копка скачать
                    pyautogui.click(gg2)
                    time.sleep(1)
                    
                    gg3 = pyautogui.locateOnScreen("720.png")
                    print(gg3) #копка скачать
                    pyautogui.click(gg3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            if im == '8':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    hh = pyautogui.locateOnScreen("скачать.png")
                    print(hh) #копка скачать
                    pyautogui.click(hh)
                    time.sleep(1)
                    
                    hh1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(hh1) #копка скачать
                    pyautogui.click(hh1)
                    time.sleep(4)
                    
                    hh2 = pyautogui.locateOnScreen("8 серия.png")
                    print(hh2) #копка скачать
                    pyautogui.click(hh2)
                    time.sleep(1)
                    
                    hh3 = pyautogui.locateOnScreen("720.png")
                    print(hh3) #копка скачать
                    pyautogui.click(hh3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
            
            
            if im == '9':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ii = pyautogui.locateOnScreen("скачать.png")
                    print(ii) #копка скачать
                    pyautogui.click(ii)
                    time.sleep(1)
                    
                    ii1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(ii1) #копка скачать
                    pyautogui.click(ii1)
                    time.sleep(4)
                    
                    ii2 = pyautogui.locateOnScreen("9 серия.png")
                    print(ii2) #копка скачать
                    pyautogui.click(ii2)
                    time.sleep(1)
                    
                    ii3 = pyautogui.locateOnScreen("720.png")
                    print(ii3) #копка скачать
                    pyautogui.click(ii3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            
            if im == '10':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    jj = pyautogui.locateOnScreen("скачать.png")
                    print(jj) #копка скачать
                    pyautogui.click(jj)
                    time.sleep(1)
                    
                    jj1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(jj1) #копка скачать
                    pyautogui.click(jj1)
                    time.sleep(4)
                    
                    jj2 = pyautogui.locateOnScreen("10 серия.png")
                    print(jj2) #копка скачать
                    pyautogui.click(jj2)
                    time.sleep(1)
                    
                    jj3 = pyautogui.locateOnScreen("720.png")
                    print(jj3) #копка скачать
                    pyautogui.click(jj3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
            
            
            if im == '11':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    kk = pyautogui.locateOnScreen("скачать.png")
                    print(kk) #копка скачать
                    pyautogui.click(kk)
                    time.sleep(1)
                    
                    kk1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(kk1) #копка скачать
                    pyautogui.click(kk1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(2)
                    
                    kk2 = pyautogui.locateOnScreen("11 серия.png")
                    print(kk2) #копка скачать
                    pyautogui.click(kk2)
                    time.sleep(1)
                    
                    kk3 = pyautogui.locateOnScreen("720.png")
                    print(kk3) #копка скачать
                    pyautogui.click(kk3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
            
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            if im == '12':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ll = pyautogui.locateOnScreen("скачать.png")
                    print(ll) #копка скачать
                    pyautogui.click(ll)
                    time.sleep(1)
                    
                    ll1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(ll1) #копка скачать
                    pyautogui.click(ll1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    ll2 = pyautogui.locateOnScreen("12 серия.png")
                    print(ll2) #копка скачать
                    pyautogui.click(ll2)
                    time.sleep(1)
                    
                    ll3 = pyautogui.locateOnScreen("720.png")
                    print(ll3) #копка скачать
                    pyautogui.click(ll3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '13':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    mm = pyautogui.locateOnScreen("скачать.png")
                    print(mm) #копка скачать
                    pyautogui.click(mm)
                    time.sleep(1)
                   
                    mm1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(mm1) #копка скачать
                    pyautogui.click(mm1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    mm2 = pyautogui.locateOnScreen("13 серия.png")
                    print(mm2) #копка скачать
                    pyautogui.click(mm2)
                    time.sleep(1)
                    
                    mm3 = pyautogui.locateOnScreen("720.png")
                    print(mm3) #копка скачать
                    time.sleep(30)
                    pyautogui.click(mm3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
            if im == '14':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    nn = pyautogui.locateOnScreen("скачать.png")
                    print(nn) #копка скачать
                    pyautogui.click(nn)
                    time.sleep(1)
                    
                    nn1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(nn1) #копка скачать
                    pyautogui.click(nn1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    nn2 = pyautogui.locateOnScreen("14 серия.png")
                    print(nn2) #копка скачать
                    pyautogui.click(nn2)
                    time.sleep(1)
                    
                    nn3 = pyautogui.locateOnScreen("720.png")
                    print(nn3) #копка скачать
                    pyautogui.click(nn3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '15':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    oo = pyautogui.locateOnScreen("скачать.png")
                    print(oo) #копка скачать
                    pyautogui.click(oo)
                    time.sleep(1)
                    
                    oo1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(oo1) #копка скачать
                    pyautogui.click(oo1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    oo2 = pyautogui.locateOnScreen("15 серия.png")
                    print(oo2) #копка скачать
                    pyautogui.click(oo2)
                    time.sleep(1)
                    
                    oo3 = pyautogui.locateOnScreen("720.png")
                    print(oo3) #копка скачать
                    pyautogui.click(oo3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '16':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    pp = pyautogui.locateOnScreen("скачать.png")
                    print(pp) #копка скачать
                    pyautogui.click(pp)
                    time.sleep(1)
                    
                    pp1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(pp1) #копка скачать
                    pyautogui.click(pp1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    pp2 = pyautogui.locateOnScreen("16 серия.png")
                    print(pp2) #копка скачать
                    pyautogui.click(pp2)
                    time.sleep(1)
                    
                    pp3 = pyautogui.locateOnScreen("720.png")
                    print(pp3) #копка скачать
                    pyautogui.click(pp3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '17':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    qq = pyautogui.locateOnScreen("скачать.png")
                    print(qq) #копка скачать
                    pyautogui.click(qq)
                    time.sleep(1)
                    
                    qq1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(qq1) #копка скачать
                    pyautogui.click(qq1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    qq2 = pyautogui.locateOnScreen("17 серия.png")
                    print(qq2) #копка скачать
                    pyautogui.click(qq2)
                    time.sleep(1)
                    
                    qq3 = pyautogui.locateOnScreen("720.png")
                    print(qq3) #копка скачать
                    pyautogui.click(qq3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '18':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    rr = pyautogui.locateOnScreen("скачать.png")
                    print(rr) #копка скачать
                    pyautogui.click(rr)
                    time.sleep(1)
                    
                    rr1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(rr1) #копка скачать
                    pyautogui.click(rr1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    rr2 = pyautogui.locateOnScreen("18 серия.png")
                    print(rr2) #копка скачать
                    pyautogui.click(rr2)
                    time.sleep(1)
                    
                    rr3 = pyautogui.locateOnScreen("720.png")
                    print(rr3) #копка скачать
                    pyautogui.click(rr3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ   pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
            if im == '19':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ss = pyautogui.locateOnScreen("скачать.png")
                    print(ss) #копка скачать
                    pyautogui.click(ss)
                    time.sleep(1)
                    
                    ss1 = pyautogui.locateOnScreen("2 сезон.png")
                    print(ss1) #копка скачать
                    pyautogui.click(ss1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    ss2 = pyautogui.locateOnScreen("19 серия.png")
                    print(ss2) #копка скачать
                    pyautogui.click(ss2)
                    time.sleep(1)
                    
                    ss3 = pyautogui.locateOnScreen("720.png")
                    print(ss3) #копка скачать
                    pyautogui.click(ss3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(3)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    # старый код
                    # 2321 строк - 1096 строк 2 сезон
                    
         # 3 сезон
                
        if imp == '3':
            print('\n   1 сезон весит - 18.748 мб')
            print(' Серии: ')
            print(' 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n 11\n 12\n 13\n 14\n 15\n 16\n 17\n 18\n 19\n 20\n 21\n 22\n 23\n 24\n')
            im = input('    Выберите серию --> ')
            if im == '1':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(2)
                    pyautogui.click(1175, 52)
                    time.sleep(1)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    aaa = pyautogui.locateOnScreen("скачать.png")
                    print(aaa) #кнопка скачать
                    pyautogui.click(aaa)
                    time.sleep(1)   
                    
                    aaa1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(aaa1) #копка скачать
                    pyautogui.click(aaa1)
                    time.sleep(5) 
                   
                    aaa2 = pyautogui.locateOnScreen("1 серия.png")
                    print(aaa2) #копка скачать
                    pyautogui.click(aaa2)
                    time.sleep(4)   
                   
                    aaa3 = pyautogui.locateOnScreen("720.png")
                    print(aaa3) #копка скачать
                    pyautogui.click(aaa3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
    
            
            if im == '2':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(1)
                    pyautogui.click(1175, 52)
                    time.sleep(0.5)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    bbb = pyautogui.locateOnScreen("скачать.png")
                    print(bbb) #копка скачать
                    pyautogui.click(bbb)
                    time.sleep(1)
                    
                    bbb1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(bbb1) #копка скачать
                    pyautogui.click(bbb1)
                    time.sleep(1)
                    
                    bbb2 = pyautogui.locateOnScreen("2 серия.png")
                    print(bbb2) #копка скачать
                    pyautogui.click(bbb2)
                    time.sleep(1)
                    
                    bbb3 = pyautogui.locateOnScreen("720.png")
                    print(bbb3) #копка скачать
                    pyautogui.click(bbb3)
                
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            if im == '3':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    ccc = pyautogui.locateOnScreen("скачать.png")
                    print(ccc) #копка скачать
                    pyautogui.click(ccc)
                    time.sleep(1)
                    
                    ccc1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(ccc1) #копка скачать
                    pyautogui.click(ccc1)
                    time.sleep(1)
                    
                    ccc2 = pyautogui.locateOnScreen("3 серия.png")
                    print(ccc2) #копка скачать
                    pyautogui.click(ccc2)
                    time.sleep(1)
                    
                    ccc3 = pyautogui.locateOnScreen("720.png")
                    print(ccc3) #копка скачать
                    pyautogui.click(ccc3)
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка       
            
            
            if im == '4':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                  
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    ddd = pyautogui.locateOnScreen("скачать.png")
                    print(ddd) #копка скачать
                    pyautogui.click(ddd)
                    time.sleep(1)
                    
                    ddd1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(ddd1) #копка скачать
                    pyautogui.click(ddd1)
                    time.sleep(1)
                    
                    ddd2 = pyautogui.locateOnScreen("4 серия.png")
                    print(ddd2) #копка скачать
                    pyautogui.click(ddd2)
                    time.sleep(1)
                    
                    ddd3 = pyautogui.locateOnScreen("720.png")
                    print(ddd3) #копка скачать
                    pyautogui.click(ddd3)
                  
                  
                  
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') 
            
            
            
            if im == '5':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    eee = pyautogui.locateOnScreen("скачать.png")
                    print(eee) #копка скачать
                    pyautogui.click(eee)
                    time.sleep(1)
                    
                    eee1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(eee1) #копка скачать
                    pyautogui.click(eee1)
                    time.sleep(1)
                    
                    eee2 = pyautogui.locateOnScreen("5 серия.png")
                    print(eee2) #копка скачать
                    pyautogui.click(eee2)
                    time.sleep(1)
                    
                    eee3 = pyautogui.locateOnScreen("720.png")
                    print(eee3) #копка скачать
                    pyautogui.click(eee3)
                    
                    
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') 
                    
                    
            if im == '6':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    fff = pyautogui.locateOnScreen("скачать.png")
                    print(fff) #копка скачать
                    pyautogui.click(fff)
                    time.sleep(1)
                    
                    fff1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(fff1) #копка скачать
                    pyautogui.click(fff1)
                    time.sleep(4)
                    
                    fff2 = pyautogui.locateOnScreen("6 серия.png")
                    print(fff2) #копка скачать
                    pyautogui.click(fff2)
                    time.sleep(1)
                    
                    fff3 = pyautogui.locateOnScreen("720.png")
                    print(fff3) #копка скачать
                    pyautogui.click(fff3)
                    
                    
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4')        
                    
                    
                
            
            if im == '7':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ggg = pyautogui.locateOnScreen("скачать.png")
                    print(ggg) #копка скачать
                    pyautogui.click(ggg)
                    time.sleep(1)
                    
                    ggg1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(ggg1) #копка скачать
                    pyautogui.click(ggg1)
                    time.sleep(4)
                    
                    ggg2 = pyautogui.locateOnScreen("7 серия.png")
                    print(ggg2) #копка скачать
                    pyautogui.click(ggg2)
                    time.sleep(1)
                    
                    ggg3 = pyautogui.locateOnScreen("720.png")
                    print(ggg3) #копка скачать
                    pyautogui.click(ggg3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab')
                    time.sleep(5)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            if im == '8':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    hhh = pyautogui.locateOnScreen("скачать.png")
                    print(hhh) #копка скачать
                    pyautogui.click(hhh)
                    time.sleep(1)
                    
                    hhh1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(hhh1) #копка скачать
                    pyautogui.click(hhh1)
                    time.sleep(4)
                    
                    hhh2 = pyautogui.locateOnScreen("8 серия.png")
                    print(hhh2) #копка скачать
                    pyautogui.click(hhh2)
                    time.sleep(1)
                    
                    hhh3 = pyautogui.locateOnScreen("720.png")
                    print(hhh3) #копка скачать
                    pyautogui.click(hhh3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            
            
            if im == '9':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    iii = pyautogui.locateOnScreen("скачать.png")
                    print(iii) #копка скачать
                    pyautogui.click(iii)
                    time.sleep(1)
                    
                    iii1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(iii1) #копка скачать
                    pyautogui.click(iii1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    iii2 = pyautogui.locateOnScreen("9 серия.png")
                    print(iii2) #копка скачать
                    pyautogui.click(iii2)
                    time.sleep(1)
                    
                    iii3 = pyautogui.locateOnScreen("720.png")
                    print(iii3) #копка скачать
                    pyautogui.click(iii3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') 
                    
            
            
            
            if im == '10':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    jjj = pyautogui.locateOnScreen("скачать.png")
                    print(jjj) #копка скачать
                    pyautogui.click(jjj)
                    time.sleep(1)
                    
                    jjj1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(jjj1) #копка скачать
                    pyautogui.click(jjj1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    jjj2 = pyautogui.locateOnScreen("10 серия.png")
                    print(jjj2) #копка скачать
                    pyautogui.click(jjj2)
                    time.sleep(1)
                    
                    jjj3 = pyautogui.locateOnScreen("720.png")
                    print(jjj3) #копка скачать
                    pyautogui.click(jjj3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') 
            
            
            
            if im == '11':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    kkk = pyautogui.locateOnScreen("скачать.png")
                    print(kkk) #копка скачать
                    pyautogui.click(kkk)
                    time.sleep(1)
                    
                    kkk1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(kkk1) #копка скачать
                    pyautogui.click(kkk1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    kkk2 = pyautogui.locateOnScreen("11 серия.png")
                    print(kkk2) #копка скачать
                    pyautogui.click(kkk2)
                    time.sleep(1)
                    
                    kkk3 = pyautogui.locateOnScreen("720.png")
                    print(kkk3) #копка скачать
                    pyautogui.click(kkk3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            
            if im == '12':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    lll = pyautogui.locateOnScreen("скачать.png")
                    print(lll) #копка скачать
                    pyautogui.click(lll)
                    time.sleep(1)
                    
                    lll1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(lll1) #копка скачать
                    pyautogui.click(lll1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    lll2 = pyautogui.locateOnScreen("12 серия.png")
                    print(lll2) #копка скачать
                    pyautogui.click(lll2)
                    time.sleep(1)
                    
                    lll3 = pyautogui.locateOnScreen("720.png")
                    print(lll3) #копка скачать
                    pyautogui.click(lll3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
            if im == '13':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    mmm = pyautogui.locateOnScreen("скачать.png")
                    print(mmm) #копка скачать
                    pyautogui.click(mmm)
                    time.sleep(1)
                   
                    mmm1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(mmm) #копка скачать
                    pyautogui.click(mmm)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    mmm2 = pyautogui.locateOnScreen("13 серия.png")
                    print(mmm2) #копка скачать
                    pyautogui.click(mmm2)
                    time.sleep(1)
                    
                    mmm3 = pyautogui.locateOnScreen("720.png")
                    print(mmm3) #копка скачать
                    pyautogui.click(mmm3)
                    
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
            if im == '14':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    nnn = pyautogui.locateOnScreen("скачать.png")
                    print(nnn) #копка скачать
                    pyautogui.click(nnn)
                    time.sleep(1)
                    
                    nnn1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(nnn1) #копка скачать
                    pyautogui.click(nnn1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    nnn2 = pyautogui.locateOnScreen("14 серия.png")
                    print(nnn2) #копка скачать
                    pyautogui.click(nnn2)
                    time.sleep(1)
                    
                    nnn3 = pyautogui.locateOnScreen("720.png")
                    print(nnn3) #копка скачать
                    pyautogui.click(nnn3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '15':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ooo = pyautogui.locateOnScreen("скачать.png")
                    print(ooo) #копка скачать
                    pyautogui.click(ooo)
                    time.sleep(1)
                    
                    ooo1 = pyautogui.locateOnScreen("1 сезон.png")
                    print(ooo1) #копка скачать
                    pyautogui.click(ooo1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    
                    ooo2 = pyautogui.locateOnScreen("15 серия.png")
                    print(ooo2) #копка скачать
                    pyautogui.click(ooo2)
                    time.sleep(1)
                    
                    ooo3 = pyautogui.locateOnScreen("720.png")
                    print(ooo3) #копка скачать
                    pyautogui.click(ooo3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '16':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ppp = pyautogui.locateOnScreen("скачать.png")
                    print(ppp) #копка скачать
                    pyautogui.click(ppp)
                    time.sleep(1)
                    
                    ppp1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(ppp1) #копка скачать
                    pyautogui.click(ppp1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    ppp2 = pyautogui.locateOnScreen("16 серия.png")
                    print(ppp2) #копка скачать
                    pyautogui.click(ppp2)
                    time.sleep(1)
                    
                    ppp3 = pyautogui.locateOnScreen("720.png")
                    print(ppp3) #копка скачать
                    pyautogui.click(ppp3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '17':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    q = pyautogui.locateOnScreen("скачать.png")
                    print(q) #копка скачать
                    pyautogui.click(q)
                    time.sleep(1)
                    
                    qqq1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(qqq1) #копка скачать
                    pyautogui.click(qqq1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    qqq2 = pyautogui.locateOnScreen("17 серия.png")
                    print(qqq2) #копка скачать
                    pyautogui.click(qqq2)
                    time.sleep(1)
                    
                    qqq3 = pyautogui.locateOnScreen("720.png")
                    print(qqq3) #копка скачать
                    pyautogui.click(qqq3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '18':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    rrr = pyautogui.locateOnScreen("скачать.png")
                    print(rrr) #копка скачать
                    pyautogui.click(rrr)
                    time.sleep(1)
                    
                    rrr1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(rrr1) #копка скачать
                    pyautogui.click(rrr1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    rrr2 = pyautogui.locateOnScreen("18 серия.png")
                    print(rrr2) #копка скачать
                    pyautogui.click(rrr2)
                    time.sleep(1)
                    
                    rrr3 = pyautogui.locateOnScreen("720.png")
                    print(rrr3) #копка скачать
                    pyautogui.click(rrr3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '19':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    sss = pyautogui.locateOnScreen("скачать.png")
                    print(sss) #копка скачать
                    pyautogui.click(sss)
                    time.sleep(1)
                    
                    sss1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(sss1) #копка скачать
                    pyautogui.click(sss1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    sss2 = pyautogui.locateOnScreen("19 серия.png")
                    print(sss2) #копка скачать
                    pyautogui.click(sss2)
                    time.sleep(1)
                    
                    sss3 = pyautogui.locateOnScreen("720.png")
                    print(sss3) #копка скачать
                    pyautogui.click(sss3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '20':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ttt = pyautogui.locateOnScreen("скачать.png")
                    print(ttt) #копка скачать
                    pyautogui.click(ttt)
                    time.sleep(1)
                    
                    ttt1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(ttt1) #копка скачать
                    pyautogui.click(ttt1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    ttt2 = pyautogui.locateOnScreen("20 серия.png")
                    print(ttt2) #копка скачать
                    pyautogui.click(ttt2)
                    time.sleep(1)
                    
                    ttt3 = pyautogui.locateOnScreen("720.png")
                    print(ttt3) #копка скачать
                    pyautogui.click(ttt3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка        
                
            if im == '21':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    uuu = pyautogui.locateOnScreen("скачать.png")
                    print(uuu) #копка скачать
                    pyautogui.click(uuu)
                    time.sleep(1)
                    
                    uuu1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(uuu1) #копка скачать
                    pyautogui.click(uuu1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    uuu2 = pyautogui.locateOnScreen("21 серия.png")
                    print(qqq2) #копка скачать
                    pyautogui.click(qqq2)
                    time.sleep(1)
                    
                    uuu3 = pyautogui.locateOnScreen("720.png")
                    print(uuu3) #копка скачать
                    pyautogui.click(uuu3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '22':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    vvv = pyautogui.locateOnScreen("скачать.png")
                    print(rrr) #копка скачать
                    pyautogui.click(rrr)
                    time.sleep(1)
                    
                    vvv1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(vvv1) #копка скачать
                    pyautogui.click(vvv1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    vvv2 = pyautogui.locateOnScreen("22 серия.png")
                    print(vvv2) #копка скачать
                    pyautogui.click(vvv2)
                    time.sleep(1)
                    
                    vvv3 = pyautogui.locateOnScreen("720.png")
                    print(vvv3) #копка скачать
                    pyautogui.click(vvv3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '23':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    www = pyautogui.locateOnScreen("скачать.png")
                    print(www) #копка скачать
                    pyautogui.click(www)
                    time.sleep(1)
                    
                    www1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(www1) #копка скачать
                    pyautogui.click(www1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    www2 = pyautogui.locateOnScreen("23 серия.png")
                    print(www2) #копка скачать
                    pyautogui.click(www2)
                    time.sleep(1)
                    
                    www3 = pyautogui.locateOnScreen("720.png")
                    print(www3) #копка скачать
                    pyautogui.click(www3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '24':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    xxx = pyautogui.locateOnScreen("скачать.png")
                    print(xxx) #копка скачать
                    pyautogui.click(xxx)
                    time.sleep(1)
                    
                    xxx1 = pyautogui.locateOnScreen("3 сезон.png")
                    print(xxx1) #копка скачать
                    pyautogui.click(xxx1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    xxx2 = pyautogui.locateOnScreen("24 серия.png")
                    print(xxx2) #копка скачать
                    pyautogui.click(xxx2)
                    time.sleep(1)
                    
                    xxx3 = pyautogui.locateOnScreen("720.png")
                    print(xxx3) #копка скачать
                    pyautogui.click(xxx3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка      
                
        if imp == '4':
            print(' Серии: ')
            print(' 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n т.к начиная с 10 серии качесвто 360p')
            im = input('    Выберите серию --> ')
            if im == '1':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(2)
                    pyautogui.click(1175, 52)
                    time.sleep(1)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    aaaa = pyautogui.locateOnScreen("скачать.png")
                    print(aaaa) #кнопка скачать
                    pyautogui.click(aaaa)
                    time.sleep(1)   
                    
                    aaaa1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(aaaa1) #копка скачать
                    pyautogui.click(aaaa1)
                    time.sleep(5) 
                   
                    aaaa2 = pyautogui.locateOnScreen("1 серия.png")
                    print(aaaa2) #копка скачать
                    pyautogui.click(aaaa2)
                    time.sleep(4)   
                   
                    aaaa3 = pyautogui.locateOnScreen("720.png")
                    print(aaaa3) #копка скачать
                    pyautogui.click(aaaa3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
    
            
            if im == '2':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(1)
                    pyautogui.click(1175, 52)
                    time.sleep(0.5)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    bbbb = pyautogui.locateOnScreen("скачать.png")
                    print(bbbb) #копка скачать
                    pyautogui.click(bbbb)
                    time.sleep(1)
                    
                    bbbb1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(bbbb1) #копка скачать
                    pyautogui.click(bbbb1)
                    time.sleep(1)
                    
                    bbbb2 = pyautogui.locateOnScreen("2 серия.png")
                    print(bbbb2) #копка скачать
                    pyautogui.click(bbbb2)
                    time.sleep(1)
                    
                    bbbb3 = pyautogui.locateOnScreen("720.png")
                    print(bbbb3) #копка скачать
                    pyautogui.click(bbbb3)
                
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            if im == '3':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    ccc = pyautogui.locateOnScreen("скачать.png")
                    print(cccc) #копка скачать
                    pyautogui.click(cccc)
                    time.sleep(1)
                    
                    cccc1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(cccc1) #копка скачать
                    pyautogui.click(cccc1)
                    time.sleep(1)
                    
                    cccc2 = pyautogui.locateOnScreen("3 серия.png")
                    print(cccc2) #копка скачать
                    pyautogui.click(cccc2)
                    time.sleep(1)
                    
                    cccc3 = pyautogui.locateOnScreen("720.png")
                    print(cccc3) #копка скачать
                    pyautogui.click(cccc3)
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка       
            
            
            if im == '4':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                  
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    dddd = pyautogui.locateOnScreen("скачать.png")
                    print(dddd) #копка скачать
                    pyautogui.click(dddd)
                    time.sleep(1)
                    
                    dddd1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(dddd1) #копка скачать
                    pyautogui.click(dddd1)
                    time.sleep(1)
                    
                    dddd2 = pyautogui.locateOnScreen("4 серия.png")
                    print(dddd2) #копка скачать
                    pyautogui.click(dddd2)
                    time.sleep(1)
                    
                    dddd3 = pyautogui.locateOnScreen("720.png")
                    print(dddd3) #копка скачать
                    pyautogui.click(dddd3)
                  
                  
                  
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') 
            
            
            
            if im == '5':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    eeee = pyautogui.locateOnScreen("скачать.png")
                    print(eeee) #копка скачать
                    pyautogui.click(eeee)
                    time.sleep(1)
                    
                    eeee1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(eeee1) #копка скачать
                    pyautogui.click(eeee1)
                    time.sleep(1)
                    
                    eeee2 = pyautogui.locateOnScreen("5 серия.png")
                    print(eeee2) #копка скачать
                    pyautogui.click(eeee2)
                    time.sleep(1)
                    
                    eeee3 = pyautogui.locateOnScreen("720.png")
                    print(eeee3) #копка скачать
                    pyautogui.click(eeee3)
                    
                    
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') 
                    
                    
            if im == '6':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ffff = pyautogui.locateOnScreen("скачать.png")
                    print(ffff) #копка скачать
                    pyautogui.click(ffff)
                    time.sleep(1)
                    
                    ffff1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(ffff1) #копка скачать
                    pyautogui.click(ffff1)
                    time.sleep(4)
                    
                    ffff2 = pyautogui.locateOnScreen("6 серия.png")
                    print(ffff2) #копка скачать
                    pyautogui.click(ffff2)
                    time.sleep(1)
                    
                    ffff3 = pyautogui.locateOnScreen("720.png")
                    print(ffff3) #копка скачать
                    pyautogui.click(ffff3)
                    
                    
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4')        
                    
                    
                
            
            if im == '7':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    gggg = pyautogui.locateOnScreen("скачать.png")
                    print(gggg) #копка скачать
                    pyautogui.click(gggg)
                    time.sleep(1)
                    
                    gggg1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(gggg1) #копка скачать
                    pyautogui.click(gggg1)
                    time.sleep(4)
                    
                    gggg2 = pyautogui.locateOnScreen("7 серия.png")
                    print(gggg2) #копка скачать
                    pyautogui.click(gggg2)
                    time.sleep(1)
                    
                    gggg3 = pyautogui.locateOnScreen("720.png")
                    print(gggg3) #копка скачать
                    pyautogui.click(gggg3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab')
                    time.sleep(5)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            if im == '8':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    hhhh = pyautogui.locateOnScreen("скачать.png")
                    print(hhhh) #копка скачать
                    pyautogui.click(hhhh)
                    time.sleep(1)
                    
                    hhhh1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(hhhh1) #копка скачать
                    pyautogui.click(hhhh1)
                    time.sleep(4)
                    pyautogui.scroll (-300) # прокрутить вниз
                    time.sleep(3)
                    
                    hhhh2 = pyautogui.locateOnScreen("8 серия.png")
                    print(hhhh2) #копка скачать
                    pyautogui.click(hhhh2)
                    time.sleep(1)
                    
                    hhhh3 = pyautogui.locateOnScreen("720.png")
                    print(hhhh3) #копка скачать
                    pyautogui.click(hhhh3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            
            
            if im == '9':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    iiii = pyautogui.locateOnScreen("скачать.png")
                    print(iiii) #копка скачать
                    pyautogui.click(iiii)
                    time.sleep(1)
                    
                    iiii1 = pyautogui.locateOnScreen("4 сезон.png")
                    print(iiii1) #копка скачать
                    pyautogui.click(iiii1)
                    time.sleep(4)
                    pyautogui.scroll (-300) # прокрутить вниз
                    time.sleep(3)
                    
                    iiii2 = pyautogui.locateOnScreen("9 серия.png")
                    print(iiii2) #копка скачать
                    pyautogui.click(iiii2)
                    time.sleep(1)
                    
                    iiii3 = pyautogui.locateOnScreen("720.png")
                    print(iiii3) #копка скачать
                    pyautogui.click(iiii3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') 
                    
            
            
            
        if imp == '5':
            print(' Серии: ')
            print(' 1\n 2\n 3\n 4\n 5\n 6\n 8\n 9\n 10\n 11\n 12\n 13\n 14\n 15\n 16\n 17\n 18\n 19\n 20\n')
            print('     В 7 и 21 серии плохое качество - 360p')
            im = input('    Выберите серию --> ')
            if im == '1':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(2)
                    pyautogui.click(1175, 52)
                    time.sleep(1)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    
                    a0 = pyautogui.locateOnScreen('импровизация.png')
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    aaaaa = pyautogui.locateOnScreen("скачать.png")
                    print(aaaaa) #кнопка скачать
                    pyautogui.click(aaaaa)
                    time.sleep(1)   
                    
                    aaaaa1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(aaaaa1) #копка скачать
                    pyautogui.click(aaaaa1)
                    time.sleep(5) 
                   
                    aaaaa2 = pyautogui.locateOnScreen("1 серия.png")
                    print(aaaaa2) #копка скачать
                    pyautogui.click(aaaaa2)
                    time.sleep(4)   
                   
                    aaaaa3 = pyautogui.locateOnScreen("720.png")
                    print(aaaaa3) #копка скачать
                    pyautogui.click(aaaaa3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
    
            
            if im == '2':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11)
                    time.sleep(1)
                    pyautogui.click(1175, 52)
                    time.sleep(0.5)
                    pyautogui.click(751, 130)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    bbbbb = pyautogui.locateOnScreen("скачать.png")
                    print(bbbbb) #копка скачать
                    pyautogui.click(bbbbb)
                    time.sleep(1)
                    
                    bbbbb1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(bbbbb1) #копка скачать
                    pyautogui.click(bbbbb1)
                    time.sleep(1)
                    
                    bbbbb2 = pyautogui.locateOnScreen("2 серия.png")
                    print(bbbbb2) #копка скачать
                    pyautogui.click(bbbbb2)
                    time.sleep(1)
                    
                    bbbbb3 = pyautogui.locateOnScreen("720.png")
                    print(bbbbb3) #копка скачать
                    pyautogui.click(bbbbb3)
                    
                    
                    time.sleep(30)
                    pyautogui.click(1110, 304)
                    time.sleep(1)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            if im == '3':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    ccccc = pyautogui.locateOnScreen("скачать.png")
                    print(ccccc) #копка скачать
                    pyautogui.click(ccccc)
                    time.sleep(1)
                    
                    ccccc1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(ccccc1) #копка скачать
                    pyautogui.click(ccccc1)
                    time.sleep(1)
                    
                    ccccc2 = pyautogui.locateOnScreen("3 серия.png")
                    print(ccccc2) #копка скачать
                    pyautogui.click(ccccc2)
                    time.sleep(1)
                    
                    ccccc3 = pyautogui.locateOnScreen("720.png")
                    print(ccccc3) #копка скачать
                    pyautogui.click(ccccc3)
                    
                
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            if im == '4':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                  
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    ddddd = pyautogui.locateOnScreen("скачать.png")
                    print(ddddd) #копка скачать
                    pyautogui.click(ddddd)
                    time.sleep(1)
                    
                    ddddd1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(ddddd1) #копка скачать
                    pyautogui.click(ddddd1)
                    time.sleep(1)
                    
                    ddddd2 = pyautogui.locateOnScreen("4 серия.png")
                    print(ddddd2) #копка скачать
                    pyautogui.click(ddddd2)
                    time.sleep(1)
                    
                    ddddd3 = pyautogui.locateOnScreen("720.png")
                    print(ddddd3) #копка скачать
                    pyautogui.click(ddddd3)
                  
                  

                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            
            if im == '5':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    a0 = pyautogui.locateOnScreen("импровизация.png")
                    print(a0) #импровизация
                    pyautogui.click(a0)
                    time.sleep(10)
                    
                    
                    eeeee = pyautogui.locateOnScreen("скачать.png")
                    print(eeeee) #копка скачать
                    pyautogui.click(eeeee)
                    time.sleep(1)
                    
                    eeeee1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(eeeee1) #копка скачать
                    pyautogui.click(eeeee1)
                    time.sleep(1)
                    
                    eeeee2 = pyautogui.locateOnScreen("5 серия.png")
                    print(eeeee2) #копка скачать
                    pyautogui.click(eeeee2)
                    time.sleep(1)
                    
                    eeeee3 = pyautogui.locateOnScreen("720.png")
                    print(eeeee3) #копка скачать
                    pyautogui.click(eeeee3)
                    
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '6':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(6)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    fffff = pyautogui.locateOnScreen("скачать.png")
                    print(fffff) #копка скачать
                    pyautogui.click(fffff)
                    time.sleep(1)
                    
                    fffff1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(fffff1) #копка скачать
                    pyautogui.click(fffff1)
                    time.sleep(4)
                    
                    fffff2 = pyautogui.locateOnScreen("6 серия.png")
                    print(fffff2) #копка скачать
                    pyautogui.click(fffff2)
                    time.sleep(1)
                    
                    fffff3 = pyautogui.locateOnScreen("720.png")
                    print(fffff3) #копка скачать
                    pyautogui.click(fffff3)
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                
            
            if im == '8':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ggggg = pyautogui.locateOnScreen("скачать.png")
                    print(ggggg) #копка скачать
                    pyautogui.click(ggggg)
                    time.sleep(1)
                    
                    ggggg1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(ggggg1) #копка скачать
                    pyautogui.click(ggggg1)
                    time.sleep(4)
                    pyautogui.scroll (-450) # прокрутить вниз
                    time.sleep(3)
                    
                    ggggg2 = pyautogui.locateOnScreen("8 серия.png")
                    print(ggggg2) #копка скачать
                    pyautogui.click(ggggg2)
                    time.sleep(1)
                    
                    ggggg3 = pyautogui.locateOnScreen("720.png")
                    print(ggggg3) #копка скачать
                    pyautogui.click(ggggg3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            if im == '9':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    hhhhh = pyautogui.locateOnScreen("скачать.png")
                    print(hhhhh) #копка скачать
                    pyautogui.click(hhhhh)
                    time.sleep(1)
                    
                    hhhhh1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(hhhhh1) #копка скачать
                    pyautogui.click(hhhhh1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    hhhhh2 = pyautogui.locateOnScreen("9 серия.png")
                    print(hhhhh2) #копка скачать
                    pyautogui.click(hhhhh2)
                    time.sleep(1)
                    
                    hhhhh3 = pyautogui.locateOnScreen("720.png")
                    print(hhhhh3) #копка скачать
                    pyautogui.click(hhhhh3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
            
            
            if im == '10':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ii = pyautogui.locateOnScreen("скачать.png")
                    print(ii) #копка скачать
                    pyautogui.click(ii)
                    time.sleep(1)
                    
                    iiiii1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(iiiii1) #копка скачать
                    pyautogui.click(iiiii1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    iiiii2 = pyautogui.locateOnScreen("10 серия.png")
                    print(iiiii2) #копка скачать
                    pyautogui.click(iiiii2)
                    time.sleep(1)
                    
                    iiiii3 = pyautogui.locateOnScreen("720.png")
                    print(iiiii3) #копка скачать
                    pyautogui.click(iiiii3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            
            
            if im == '11':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    jjjjj = pyautogui.locateOnScreen("скачать.png")
                    print(jjjjj) #копка скачать
                    pyautogui.click(jjjjj)
                    time.sleep(1)
                    
                    jjjjj1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(jjjjj1) #копка скачать
                    pyautogui.click(jjjjj1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    jjjjj2 = pyautogui.locateOnScreen("11 серия.png")
                    print(jjjjj2) #копка скачать
                    pyautogui.click(jjjjj2)
                    time.sleep(1)
                    
                    jjjjj3 = pyautogui.locateOnScreen("720.png")
                    print(jjjjj3) #копка скачать
                    pyautogui.click(jjjjj3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
            
            
            if im == '12':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    kkkkk = pyautogui.locateOnScreen("скачать.png")
                    print(kkkkk) #копка скачать
                    pyautogui.click(kkkkk)
                    time.sleep(1)
                    
                    kkkkk1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(kkkkk1) #копка скачать
                    pyautogui.click(kkkkk1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(2)
                    
                    kkkkk2 = pyautogui.locateOnScreen("12 серия.png")
                    print(kkkkk2) #копка скачать
                    pyautogui.click(kkkkk2)
                    time.sleep(1)
                    
                    kkkkk3 = pyautogui.locateOnScreen("720.png")
                    print(kkkkk3) #копка скачать
                    pyautogui.click(kkkkk3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
            
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
            
            if im == '13':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    lllll = pyautogui.locateOnScreen("скачать.png")
                    print(lllll) #копка скачать
                    pyautogui.click(lllll)
                    time.sleep(1)
                    
                    lllll1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(lllll1) #копка скачать
                    pyautogui.click(lllll1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    lllll2 = pyautogui.locateOnScreen("13 серия.png")
                    print(lllll2) #копка скачать
                    pyautogui.click(lllll2)
                    time.sleep(1)
                    
                    lllll3 = pyautogui.locateOnScreen("720.png")
                    print(lllll3) #копка скачать
                    pyautogui.click(lllll3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '14':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    mmmmm = pyautogui.locateOnScreen("скачать.png")
                    print(mmmmm) #копка скачать
                    pyautogui.click(mmmmm)
                    time.sleep(1)
                   
                    mmmmm1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(mmmmm1) #копка скачать
                    pyautogui.click(mmmmm1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    mmmmm2 = pyautogui.locateOnScreen("14 серия.png")
                    print(mmmmm2) #копка скачать
                    pyautogui.click(mmmmm2)
                    time.sleep(1)
                    
                    mmmmm3 = pyautogui.locateOnScreen("720.png")
                    print(mmmmm3) #копка скачать
                    time.sleep(30)
                    pyautogui.click(mmmmm3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
            
                    
                    
                    
                    
            if im == '15':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ooooo = pyautogui.locateOnScreen("скачать.png")
                    print(ooooo) #копка скачать
                    pyautogui.click(ooooo)
                    time.sleep(1)
                    
                    ooooo1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(ooooo1) #копка скачать
                    pyautogui.click(ooooo1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    ooooo2 = pyautogui.locateOnScreen("15 серия.png")
                    print(ooooo2) #копка скачать
                    pyautogui.click(ooooo2)
                    time.sleep(1)
                    
                    ooooo3 = pyautogui.locateOnScreen("720.png")
                    print(ooooo3) #копка скачать
                    pyautogui.click(ooooo3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '16':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ppppp = pyautogui.locateOnScreen("скачать.png")
                    print(ppppp) #копка скачать
                    pyautogui.click(ppppp)
                    time.sleep(1)
                    
                    ppppp1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(ppppp1) #копка скачать
                    pyautogui.click(ppppp1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    ppppp2 = pyautogui.locateOnScreen("16 серия.png")
                    print(ppppp2) #копка скачать
                    pyautogui.click(ppppp2)
                    time.sleep(1)
                    
                    ppppp3 = pyautogui.locateOnScreen("720.png")
                    print(ppppp3) #копка скачать
                    pyautogui.click(ppppp3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
                    
                    
            if im == '17':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    qqqqq = pyautogui.locateOnScreen("скачать.png")
                    print(qqqqq) #копка скачать
                    pyautogui.click(qqqqq)
                    time.sleep(1)
                    
                    qqqqq1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(qqqqq1) #копка скачать
                    pyautogui.click(qqqqq1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    qqqqq2 = pyautogui.locateOnScreen("17 серия.png")
                    print(qqqqq2) #копка скачать
                    pyautogui.click(qqqqq2)
                    time.sleep(1)
                    
                    qqqqq3 = pyautogui.locateOnScreen("720.png")
                    print(qqqqq3) #копка скачать
                    pyautogui.click(qqqqq3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
                    
            if im == '18':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    rrrrr = pyautogui.locateOnScreen("скачать.png")
                    print(rrrrr) #копка скачать
                    pyautogui.click(rrrrr)
                    time.sleep(1)
                    
                    rrrrr1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(rrrrr1) #копка скачать
                    pyautogui.click(rrrrr1)
                    time.sleep(4)
                    pyautogui.scroll (-350) # прокрутить вниз
                    time.sleep(3)
                    
                    rrrrr2 = pyautogui.locateOnScreen("18 серия.png")
                    print(rrrrr2) #копка скачать
                    pyautogui.click(rrrrr2)
                    time.sleep(1)
                    
                    rrrrr3 = pyautogui.locateOnScreen("720.png")
                    print(rrrrr3) #копка скачать
                    pyautogui.click(rrrrr3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ   pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка
                    
            if im == '19':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    sssss = pyautogui.locateOnScreen("скачать.png")
                    print(sssss) #копка скачать
                    pyautogui.click(sssss)
                    time.sleep(1)
                    
                    sssss1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(sssss1) #копка скачать
                    pyautogui.click(sssss1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    sssss2 = pyautogui.locateOnScreen("19 серия.png")
                    print(sssss2) #копка скачать
                    pyautogui.click(sssss2)
                    time.sleep(1)
                    
                    sssss3 = pyautogui.locateOnScreen("720.png")
                    print(sssss3) #копка скачать
                    pyautogui.click(sssss3)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(3)
                    pyautogui.hotkey('alt', 'f4') #Оштбка        
                
                
            if im == '20':
                path = pathlib.Path('C:/Program Files/Kinoplay')
                if path.exists() == True:
                    time.sleep(1)
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('kinoplay')
                    pyautogui.press('enter')
                    time.sleep(5)
                    pyautogui.click(1234, 11) #на весь экран
                    time.sleep(1)
                    pyautogui.click(1175, 52) #нажать на лупу
                    time.sleep(0.5)
                    pyautogui.click(751, 130) #нажать на поиск
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.typewrite('bvghjdbpfwbz') #написать импровизация
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(5)
                    
                    i0 = pyautogui.locateOnScreen("импровизация.png")
                    print(i0) #импровизация
                    pyautogui.click(i0)
                    time.sleep(10)  
                    
                    ttttt = pyautogui.locateOnScreen("скачать.png")
                    print(ttttt) #копка скачать
                    pyautogui.click(ttttt)
                    time.sleep(1)
                    
                    ttttt1 = pyautogui.locateOnScreen("5 сезон.png")
                    print(ttttt1) #копка скачать
                    pyautogui.click(ttttt1)
                    time.sleep(4)
                    pyautogui.scroll (-500) # прокрутить вниз
                    time.sleep(3)
                    
                    ttttt2 = pyautogui.locateOnScreen("20 серия.png")
                    print(ttttt2) #копка скачать
                    pyautogui.click(ttttt2)
                    time.sleep(1)
                    
                    ttttt3 = pyautogui.locateOnScreen("720.png")
                    print(ttttt3) #копка скачать
                    pyautogui.click(ttttt3)
                   
                    time.sleep(30)
                    pyautogui.hotkey('alt', 'tab') #Оштбка
                    time.sleep(2)
                    pyautogui.hotkey('alt', 'f4') #Оштбка    
            
            
            
            
            
                 
                
                
                    
                
        
                    
                    
    if a == '2':
        print('''\n1. Железный человек (3 части), 2. Тор(3 части), 3. Мстители (4 части), 4. Халк (2 части), 5. Веном(2 части), 6. Дэдпул(2 части)
                 7. Человек паук(8 частей), 8. Люди икс(7 частей) 9. Логан, 10.Фантастическая четвёрка (3 части), 11. Чёрная вдова,
                  12. Стражи галактики(2 части), 13. Доктор Стрэндж, 14. Человек муравей (2 части), 15. Первый мститель(3 части)\n''')
        film = input('Введите номер фильма --> ')
        if film == '1':
            print('\n1. Железный человек, 2. Железный человек 2, 3. Железный человек 3\n')
            jel = input('Введите номер фильма --> ')
            print('\n')
            if jel == '1':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
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
                        pyautogui.typewrite('')          
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
                        
            if jel == '2':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
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
                        pyautogui.typewrite('')              
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
            if jel == '3':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                        pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                        time.sleep(2)
                        pyautogui.typewrite('chrome')
                        pyautogui.press('enter')
                        time.sleep(3)
                        pyautogui.click(502, 43) 
                        pyautogui.typewrite('')              
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')   
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
                    
        if film == '2':
            print('\n1. Тор, 2. Тор 2: Царство тьмы, 3. Тор 3: Рагнарёк\n')
            tor = input('Введите номер фильма --> ')
            if tor == '1':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                            time.sleep(1)
                            print('             Нашёл\n')
                            pyautogui.hotkey('win')
                            time.sleep(1)
                            pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                            pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                            time.sleep(2)
                            pyautogui.typewrite('chrome')
                            pyautogui.press('enter')
                            time.sleep(3)
                            pyautogui.click(502, 43) 
                            pyautogui.typewrite('')              
                            pyautogui.press('enter')
                            os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
                        
            if tor == '2':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                        pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                        time.sleep(2)
                        pyautogui.typewrite('chrome')
                        pyautogui.press('enter')
                        time.sleep(3)
                        pyautogui.click(502, 43) 
                        pyautogui.typewrite('')              
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67)
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
            
            if tor == '3':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                        pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                        time.sleep(2)
                        pyautogui.typewrite('chrome')
                        pyautogui.press('enter')
                        time.sleep(3)
                        pyautogui.click(502, 43) 
                        pyautogui.typewrite('')              
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
                    
                    
        if film == '3':
            print('\n1. Мстители, 2. Мстители: Эра Альтрона, 3. Мстители: Война бесконечности, 4. Мстители: Финал\n')
            mst = input('   Введите номер фильма --> ')
            if mst == '1':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                        pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                        time.sleep(2)
                        pyautogui.typewrite('chrome')
                        pyautogui.press('enter')
                        time.sleep(3)
                        pyautogui.click(502, 43) 
                        pyautogui.typewrite('')              
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
                    
            if mst == '2':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                        pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                        time.sleep(2)
                        pyautogui.typewrite('chrome')
                        pyautogui.press('enter')
                        time.sleep(3)
                        pyautogui.click(502, 43) 
                        pyautogui.typewrite('')              
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
                    
            if mst == '3':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                        pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                        time.sleep(2)
                        pyautogui.typewrite('chrome')
                        pyautogui.press('enter')
                        time.sleep(3)
                        pyautogui.click(502, 43) 
                        pyautogui.typewrite('')              
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
            
            if mst == '4':
                print('     Ищу Chrome')
                path = pathlib.Path('C:/Program Files/Google/Chrome')
                if path.exists() == True:
                        time.sleep(1)
                        print('             Нашёл\n')
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                        pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                        time.sleep(2)
                        pyautogui.typewrite('chrome')
                        pyautogui.press('enter')
                        time.sleep(3)
                        pyautogui.click(502, 43) 
                        pyautogui.typewrite('')              
                        pyautogui.press('enter')
                        os.system('cls')
                else:
                    print('\n Chrome не нашёл')
                    time.sleep(1)
                    print('             Нашёл Yandex\n')
                    pyautogui.hotkey('win')
                    time.sleep(1)
                    pyautogui.hotkey('shift', 'alt') #сменя языка на русский
                    pyautogui.hotkey('shift', 'alt') #сменя языка на англ
                    time.sleep(2)
                    pyautogui.typewrite('yandex')
                    pyautogui.press('enter')
                    time.sleep(7)
                    pyautogui.click(455, 67) 
                    pyautogui.typewrite('')          
                    pyautogui.press('enter')
                    os.system('cls')
                    
        
            
       
        
    
    
    
