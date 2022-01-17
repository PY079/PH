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
import datetime




def res():
    print(Style.RESET_ALL)


getUser = lambda: environ['USERNAME']
user = getUser()

def t30():
    print('\n')
    sys.stdout.write(' Закрытие этой вкладки - 30с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 29с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 28с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 27с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 26с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 25с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 24с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 23с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 22с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 21с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 20с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 19с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 18с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 17с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 16с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 15с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 14с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 13с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 12с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 11с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 10с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 9с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 8с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 7с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 6с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 5с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 4с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 3с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 2с \r')
    time.sleep(1)
    sys.stdout.write(' Закрытие этой вкладки - 1с \r')
    time.sleep(1)
    os.system('cls')


akl = '2.py'
os.system('cls')
time.sleep(1.5)
def py1():
    pathl = pathlib.Path('C:/Users/'+ user +'/-для работы program-/'+akl)
    if pathl.exists() == False:
        print('\n      '+akl+ ' нет, поэтому запуска программы не будет')
        time.sleep(3)
        print('     Авто закрытие программы')
        time.sleep(4)
        sys.exit()
    else:
        print('\n   '+akl+' есть\n\n         Запуск...')
        time.sleep(2)


def py2():
    pathl = pathlib.Path('C:/Users/'+ user +'/-для работы program-/'+'mus.py')
    if pathl.exists() == False:
        print('\n      '+'mus.py'+ ' нет, поэтому запуска программы не будет')
        time.sleep(3)
        print('     Авто закрытие программы')
        time.sleep(4)
        sys.exit()
    else:
        print('\n   '+'mus.py'+' есть\n\n         Запуск...')
        time.sleep(2)

py1(), py2()

os.system('cls')
while True:
        colorama.init()
        print()                                                                                                                                                                         #
        print(colorama.Fore.GREEN + '                                ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗')
        print(colorama.Fore.GREEN +'                                ║', Fore.CYAN+'   1.Yandex.Browser,', Fore.GREEN + '2.Соцсети,', Fore.YELLOW + '3.Я.Почта,', Fore.CYAN +'4.Ввести запрос или ссылку(без https://),', Fore.GREEN + "5.Еда", Fore.RED + '6.Я.Музыка,', Fore.GREEN+'          ║')                           
        print(colorama.Fore.GREEN + '                                ║', Fore.WHITE+'              7.Фильмы,', Fore.CYAN + '8.Карта,', Fore.YELLOW + '9.Такси,', Fore.RED + '10.Программы', Fore.CYAN + '11. Я.Диск', Fore.RED + '12. Взломанные приложения', Fore.CYAN+'0 - Выход',Fore.GREEN+'           ║', Fore.GREEN+ '\n'+'                                ║                                                                                                                  ║'+'\n'+'                                ║',Fore.WHITE+'                                                      13. Поддержка',Fore.GREEN+'                                             ║')
        print(colorama.Fore.GREEN + '                                ║                                                                                                                  ║')
        print(colorama.Fore.GREEN+'                                ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')
        print(Style.RESET_ALL)
        print()
        s = input('  Введите номер --> ')
        os.system('cls')
        if s == '1':
            print()
            print('  Открытие браузера')
            time.sleep(2)
            os.system('cls')
            webbrowser.open_new_tab('https://yandex.ru')

        if s == '2':
            print()
            colorama.init()
            print(colorama.Fore.GREEN + '  Соцсети:')
            print(Style.RESET_ALL)
            print()
            colorama.init()                                                  #
            print(colorama.Fore.GREEN+'     ╔════════════════════════════════╗')
            print(colorama.Fore.GREEN+'     ║',  Fore.CYAN + ' 1.VK' , colorama.Fore.RED + '2.YouTube',Fore.WHITE+'3. ВК ФУНКЦИИ', Fore.GREEN+' ║')
            print(colorama.Fore.GREEN+'     ╚════════════════════════════════╝')
            print(Style.RESET_ALL)
            print()
            time.sleep(2)
            s1 = input('''  Введите номер  --> ''')
            os.system('cls')
            if s1 == 'выход':
                os.system('cls')
                continue
            print()
            print()   
 
            if s1 == '1':
                webbrowser.open_new_tab('https://vk.com')
                os.system('cls')
            if s1 == '2':
                webbrowser.open_new_tab('https://www.youtube.com/')
                os.system('cls')

            if s1 == '3':
                ac = input('   Какой у вас в id в вк (имя после @) ═> ')
                if ac == '':
                    print('         Вы ничего не ввели - выход')
                    time.sleep(2)
                    os.system('cls')
                    continue
                    
                ac2 = input('   Введите свой id (пример 123456789) ═> ')
                if ac2 == '':
                    print('         Вы ничего не ввели - выход')
                    time.sleep(2)
                    os.system('cls')
                    continue
                    
                os.system('cls')
                while True:
                    colorama.init()
                    print('\n\n')
                    print(colorama.Fore.GREEN+'         ╔═══════════════════╗')   
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 1.  Моя траница   '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 2.  Новости       '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 3.  Месснджер     '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 4.  Звонки        '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 5.  Друзья        '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 6.  Сообщества    '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 7.  Фотографии    '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 8.  Музыка        '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 9.  Видео         '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ║'+Fore.YELLOW+' 0.  ВЫХОД         '+Fore.GREEN+'║')
                    print(colorama.Fore.GREEN+'         ╚═══════════════════╝')
                    res()
                    
                    s2=input('      Что открыть ═> ')
                    os.system('cls')
                    if s2 == '1':
                        webbrowser.open_new_tab('https://vk.com/'+ac)
                        os.system('cls')
                    if s2 == '2':
                         webbrowser.open_new_tab('https://vk.com/feed')
                         os.system('cls')
                    if s2 == '3':
                        webbrowser.open_new_tab('https://vk.com/im?v=')
                        os.system('cls')
                    if s2 == '4':
                        webbrowser.open_new_tab('https://vk.com/calls')
                        os.system('cls')
                    if s2 == '5':
                        webbrowser.open_new_tab('https://vk.com/friends')
                        os.system('cls')
                    if s2 == '6':
                        webbrowser.open_new_tab('https://vk.com/groups')
                        os.system('cls')
                    if s2 == '7':
                        webbrowser.open_new_tab('https://vk.com/albums/'+ac2)
                        os.system('cls')
                    if s2 == '8':
                        webbrowser.open_new_tab('https://vk.com/audios'+ac2)
                        os.system('cls')
                    if s2 == '9':
                        webbrowser.open_new_tab('https://vk.com/video')
                        os.system('cls')
                    if s2 == '0':
                        break
                        os.system('cls')
                    
                    
        if s == '3':
            webbrowser.open_new_tab('https://mail.yandex.ru/')
            time.sleep(1)
            os.system('cls') 

   
        if s == '4':
            print()
            print()
            call = input('  Введите запрос или ссылку --> ')
            os.system('cls')
            if call == 'выход':
                os.system('cls')
                continue
            if re.search(r'\.', call):
                webbrowser.register('Yandex', None, webbrowser.BackgroundBrowser('C:/Users/'+ user +'/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'))
                time.sleep(1)
                os.system('cls')
                webbrowser.get('Yandex').open_new_tab('https://' + call)
                time.sleep(1)
                os.system('cls')
            elif re.search(r'\ ', call):
                webbrowser.register('Yandex', None, webbrowser.BackgroundBrowser('C:/Users/'+ user +'/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'))
                time.sleep(1)
                os.system('cls')
                webbrowser.get('Yandex').open_new_tab('https://yandex.ru/search/?text='+call+'&clid=2270455&banerid=0500000134%3A60e094f2ffcd9e001929067b&win=496&&lr=101140')
                time.sleep(1)
                os.system('cls')
            else:
                webbrowser.register('Yandex', None, webbrowser.BackgroundBrowser('C:/Users/'+ user +'/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'))
                time.sleep(1)
                os.system('cls')
                webbrowser.get('Yandex'). open_new_tab('https://yandex.ru/search/?text='+ call +'&clid=2270455&banerid=0500000134%3A60e094f2ffcd9e001929067b&win=496&&lr=101140')
                time.sleep(1)
                os.system('cls')
            print()
            print()
        
        if s == '7':
            webbrowser.open_new_tab('https://yandex.ru/efir?%3Futm_source=bno&stream_active=category&stream_category=film')
            time.sleep(1)
            os.system('cls') 
        
    
        if s == '5':
            webbrowser.open_new_tab('https://eda.yandex.ru/moscow/?shippingType=delivery')
            time.sleep(1)
            os.system('cls') 
        
        if s == '8':
            webbrowser.open_new_tab('https://yandex.ru/maps/')
            time.sleep(1)
            os.system('cls') 
        
        if s == '9':
            webbrowser.open_new_tab('https://taxi.yandex.ru/?from=tableau_yabro')
            time.sleep(1)
            os.system('cls') 
            
        if s == '6':
            print()
            print()
            print('   Выберите категорию:')
            colorama.init()
            print('\n')                                                                                                                                                                       #
            print(colorama.Fore.GREEN+'     ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
            print(colorama.Fore.CYAN+'     ║', Fore.WHITE+'1.Радостная, 2.Популярное, 3.В тренде, 4.Из кино, 5.Вечные хиты, 6.Для дома, 7.Для работы, 8.Аудиокниги, 9.Эксклюзивы,')
            print(colorama.Fore.CYAN+'     ║','\n',colorama.Fore.CYAN+'    ║', Fore.WHITE+'10.Для тренировок, 11.В нов плей листы, 12. Мощный басс за рулём, 13.Новые хиты, 14.100 хитов, 15.Каверы, 16.Послушать фоном, 17.Для вечеринки,')
            print(colorama.Fore.CYAN+'     ║','\n',colorama.Fore.CYAN+'    ║', Fore.WHITE+'18.Класика, 19.В настроение, 20.Из игр, 21.Эксперты, 22.Выбор редакции, 23.Для души, 24.Поп, 25.Рок, 26.Реп, 27.Танцевальная,')
            print(colorama.Fore.CYAN+'     ║','\n',colorama.Fore.CYAN+'    ║', Fore.WHITE+'28.Релакс, 29.Красивая, 30.Крутая, 31.Бодрая, 32.Грустная')
            print(colorama.Fore.GREEN+'     ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
            print(Style.RESET_ALL)
            print()   
            t = input('  Введите номер --> ')
            os.system('cls')
            if t == 'выход':
                os.system('cls')
                continue
            if t == '1':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/cheerful')
                time.sleep(1)
                os.system('cls')
                
        
            if t == '2':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/top?sort=popular')
                time.sleep(1)
                os.system('cls')
                
            if t == '3':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/hot')
                time.sleep(1)
                os.system('cls')
            
            if t == '4':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/cinema')
                time.sleep(1)
                os.system('cls')
        
            if t == '5':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/classics?sort=popular')
                time.sleep(1)
                os.system('cls')
        
            if t == '6':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/5e6fb7f26ee9e7243ae8c945')
                time.sleep(1)
                os.system('cls')
            
            if t == '7':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/5e8dd99921336d0178d85240')
                time.sleep(1)
                os.system('cls')
            
            if t == '8':
                webbrowser.open_new_tab('https://music.yandex.ru/genre/аудиокниги')
                time.sleep(1)
                os.system('cls')
        
            if t == '9':
                webbrowser.open_new_tab('https://music.yandex.ru/post/5f5f63dacbeb9a3e919dda3f')
                time.sleep(1)
                os.system('cls')
        
            if t == '10':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/sport')
                time.sleep(1)
                os.system('cls')
            
            if t == '11':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/new')
                time.sleep(1)
                os.system('cls')
        
            if t == '12':
                webbrowser.open_new_tab('https://music.yandex.ru/users/music-blog/playlists/1807')
                time.sleep(1)
                os.system('cls')
    
            if t == '13':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/newhits?sort=popular')
                time.sleep(1)
                os.system('cls')
                
            if t == '14':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/100hits')
                time.sleep(1)
                os.system('cls')
        
            if t == '15':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/covers')
                time.sleep(1)
                os.system('cls')
                
            if t == '16':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/background')
                time.sleep(1)
                os.system('cls')
            
            if t == '17':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/вечеринка')
                time.sleep(1)
                os.system('cls')
                
            if t == '18':
               webbrowser.open_new_tab('https://music.yandex.ru/tag/classical')
               time.sleep(1)
               os.system('cls')
            
            if t == '19':
               webbrowser.open_new_tab('https://music.yandex.ru/tag/in%20the%20mood')
               time.sleep(1)
               os.system('cls')
        
            if t == '20':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/games')
                time.sleep(1)
                os.system('cls')
            
            if t == '21':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/experts')
                time.sleep(1)
                os.system('cls')
            
            if t == '22':
                webbrowser.open_new_tab('https://music.yandex.ru/post/5d776caa24c49852264d102d')
                time.sleep(1)
                os.system('cls')
            
            if t == '23':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/soulful')
                time.sleep(1)
                os.system('cls')
            
            if t == '24':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/pop')
                time.sleep(1)
                os.system('cls')
            
            if t == '25':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/rock')
                time.sleep(1)
                os.system('cls')
            
            if t == '26':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/rap')
                time.sleep(1)
                os.system('cls')
            
            if t == '27':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/dance')
                time.sleep(1)
                os.system('cls')
        
            if t == '28':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/relax')
                time.sleep(1)
                os.system('cls')
            
            if t == '29':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/beautiful')
                time.sleep(1)
                os.system('cls')
            
            if t == '30':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/cool')
                time.sleep(1)
                os.system('cls')
            
            if t == '31':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/energetic')
                time.sleep(1)
                os.system('cls')
            
            if t == '32':
                webbrowser.open_new_tab('https://music.yandex.ru/tag/sad')
                time.sleep(1)
                os.system('cls')
   
        if s == '10':
            print()
            print()
            colorama.init()
            print('\n', colorama.Fore.GREEN+'   -----------------------------------------------------------------------------------------------------------------------')
            print(colorama.Fore.GREEN+'    |', Fore.WHITE + '  1.Komodo Edit 12,', Fore.YELLOW + '2.Проводник,', Fore.GREEN + '3.Музыка,',Fore.CYAN + '4.Radio Record', Fore.RED +'  5.YouTube', Fore.WHITE + '6. Ютуб каналы', Fore.CYAN+'7. ActiveState Komodo IDE 12', Fore.GREEN+'  |')
            print(colorama.Fore.GREEN+'    -----------------------------------------------------------------------------------------------------------------------')
            print(Style.RESET_ALL)
            print()
            s = input('     Введите номер --> ')
            os.system('cls')
            if s == 'выход':
                os.system('cls')
                continue
            os.system('cls')
            
            
            if s == '1':
                path = pathlib.Path('C:/Program Files (x86)/ActiveState Komodo Edit 12/Komodo.exe')
                if path.exists() == True:
                        program = "C:/Program Files (x86)/ActiveState Komodo Edit 12/Komodo.exe"
                        process = subprocess.Popen(program)
                        
                        time.sleep(0.5)
                        os.system('cls')
                        continue
                if path.exists() == False:
                        print("Эта программа у вас не установлена")
                        time.sleep(3)
                        os.system('cls')
                
            
            if s == '2':
                path = pathlib.Path('C:/Windows/Explorer.exe')
                if path.exists() == True:
                        program = "explorer"
                        process = subprocess.Popen(program)
                        time.sleep(0.5)
                        os.system('cls')
                        continue
                if path.exists() == False:
                        print('Эта программа у вас не установлена')
                        time.sleep(3)
                        os.system('cls')
            
                
            if s == '4':
                print('\n' + '  1.Канал, 2.Трансляция' + '\n')
                d = input('  Введите номер --> ')
                if d == 'выход':
                        os.system('cls')
                        continue
                os.system('cls')
                if d == '1':
                        webbrowser.open_new_tab('https://www.youtube.com/channel/UCRKIdBctvF1TY9z62m-jazg')
                        os.system('cls')
                if d == '2':
                        colorama.init()
                        print('\n' + colorama.Fore.RED + ' 1. Прямая трансляция, ', colorama.Fore.GREEN + '2.Russian Mix,  ', colorama.Fore.CYAN + '3.Megamix')
                        print(Style.RESET_ALL)
                        time.sleep(1)
                        f = input('  Введите номер --> ')
                        if f == 'выход':
                                os.system('cls')
                                continue
                        os.system('cls')
                        if f == '1':
                                webbrowser.open_new_tab('https://youtu.be/CVjU8gG2poc')
                                os.system('cls')
                                
                        if f == '2':
                                webbrowser.open_new_tab('https://youtu.be/TJG_myVUr48')
                                os.system('cls')
                                
                        if f == '3':
                                webbrowser.open_new_tab('https://youtu.be/M1Mduu66xNo')
                                os.system('cls')
                                
            if s == '5':
                h = input('Введите запрос --> ')
                if h == 'выход':
                        os.system('cls')
                        continue
                webbrowser.open_new_tab(' https://www.youtube.com/results?search_query=' + str(h))
                os.system('cls')               
                time.sleep(0.2)
                os.system('cls')
                continue
            
            if s == '6':
                print('''\n
                Каналы:
                      1. Marmok
                      2. Johan
                      3. Гоша Дударь
                      4. oxxxymironoffical
                      5. GalileoRU
                      6. Overbafer1
                      7. TRIGGER
                      8. Иван Викторович
                      9. Marmok Live
                      10. Johan live''')
                l = input('Ведите номер --> ')
                if l == '1':
                        webbrowser.open_new_tab('https://www.youtube.com/c/MrMarmok')
                        os.system('cls')
                if l == '2':
                        webbrowser.open_new_tab('https://www.youtube.com/channel/UCuQsXgtPrppIkSE7GWjp7HA')
                        os.system('cls')
                if l == '3':
                        webbrowser.open_new_tab('https://www.youtube.com/c/gosha_dudar')
                        os.system('cls')
                if l == '4':
                        webbrowser.open_new_tab('https://www.youtube.com/user/oxxxymironofficial')
                        os.system('cls')
                if l == '5':
                        webbrowser.open_new_tab('https://www.youtube.com/c/GalileoRU')
                        os.system('cls')
                if l == '6':
                        webbrowser.open_new_tab('https://www.youtube.com/c/overbafer1')
                        os.system('cls')
                if l == '7':
                        webbrowser.open_new_tab('https://www.youtube.com/channel/UCz704waoqMOdbxQNyhnjSkA')
                        os.system('cls')
                if l == '8':
                        webbrowser.open_new_tab('https://www.youtube.com/c/IoanPlugar_inf')
                        os.system('cls')
                if l == '9':
                        webbrowser.open_new_tab('https://www.youtube.com/c/MarmokLive')
                        os.system('cls')
                if l == '10':
                        webbrowser.open_new_tab('https://www.youtube.com/channel/UC6XeLTS99Nx1IrP7pSaDuTQ')
                        os.system('cls')
                
            if s == '7':
                path = pathlib.Path('C:/Program Files (x86)/ActiveState Komodo IDE 12/komodo.exe')
                if path.exists() == True:
                        program = "C:/Program Files (x86)/ActiveState Komodo IDE 12/komodo.exe"
                        process = subprocess.Popen(program)
                        time.sleep(0.5)
                        os.system('cls')
                        continue
                if path.exists() == False:
                        print("Эта программа у вас не установлена")
                        time.sleep(3)
                        os.system('cls')
               
                
                
                
            if s == '3':
                print('\n')
                colorama.init()
                os.system('"C:/Users/'+ user +'/-для работы program-/2.py"')
                print('\n')
                time.sleep(3)
                os.system('"C:/Users/'+ user +'/-для работы program-/mus.py"')
                print()
                t = input('  Введите 1-76 --> ')
                os.system('cls')
                print()
                print()
                
                if t == '1':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Alan_Walker_-_Alone.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Alan_Walker_-_Alone.mp3')
                        
                        os.system('cls')
                        
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(0.5)
                    
                        
                
                if t == '2':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Alan_Walker_-_Sing_Me_to_Sleep.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Alan_Walker_-_Sing_Me_to_Sleep.mp3')
                        os.system('cls')
                        time.sleep(0.5)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                       
                
                if t == '3':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Alan_Walker_AAP_Rocky_-_Live_Fast.mp3')
                    if path.exists() == True:
                       os.startfile('C:/Users/'+ user +'/01/Alan_Walker_AAP_Rocky_-_Live_Fast.mp3')
                       os.system('cls')
                       time.sleep(1)
                        
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)   
                    
                
                if t == '4':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Alan_Walker_Imanbek_-_Sweet_Dreams.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Alan_Walker_Imanbek_-_Sweet_Dreams.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)                      
                    
                if t == '5':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Alan_Walker_ISK_-_Sorry.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Alan_Walker_ISK_-_Sorry.mp3')
                        os.system('cls') 
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)       
                        
                        
                        
                                    
                if t == '6':
                    path = pathlib.Path('C:/Users/'+ user +'/01/CHVRCHS_Steve_Mac_Chris_Laws_Iain_Cook_Martin_Doherty_Lauren_Mayberry.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/CHVRCHS_Steve_Mac_Chris_Laws_Iain_Cook_Martin_Doherty_Lauren_Mayberry.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)       
                        

                    
                    
                if t == '7':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Clandestina.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Clandestina.mp3')
                        os.system('cls')
                        time.sleep(1)    
                    else:
                        colorama.init()
                        print(colorama.Fore.RED + '     Этого фала нет в директории')
                        time.sleep(3.5)
                        print(Style.RESET_ALL)
                        os.system('cls')
                        time.sleep(1)    
                        
                    
                    
                if t == '8':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Eminem_-_Rap_God.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Eminem_-_Rap_God.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        colorama.init()
                        print(colorama.Fore.RED + '     Этого фала нет в директории')
                        print(Style.RESET_ALL)
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)      
                        
                        
                    
                    
                if t == '9':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Eva_Simons_-_Bludfire.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Eva_Simons_-_Bludfire.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                    
                    
                    
                    
                    
                if t == '10':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Hans_Zimmer_-_End_Credits.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Hans_Zimmer_-_End_Credits.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)   
                        
                        
                    
                    
                    
                if t == '11':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Katy_Perry_Juicy_J_-_Dark_Horse.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Katy_Perry_Juicy_J_-_Dark_Horse.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)   
                        
                        
                        
                    
                    
                if t == '12':
                    path = pathlib.Path('C:/Users/'+ user +'/01/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                        
            
                if t == '13':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Leonid_Rudenko_ARITMIYA_-_Rain_Sun.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Leonid_Rudenko_ARITMIYA_-_Rain_Sun.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print(          'Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                    
                    
                
                if t == '14':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Minelli_-_Rampampam.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Minelli_-_Rampampam.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                        
                        
                
                if t == '15':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Nessa_Barrett_jxdn_-_la_di_die.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Nessa_Barrett_jxdn_-_la_di_die.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)   
                
                
                if t == '16':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Parah_Dice_-_Hot.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Parah_Dice_-_Hot.mp3')
                        time.sleep(1)
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)   
                    
                if t == '17':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Steve_Aoki_Alan_Walker_Isak_-_Are_You_Lonely.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Steve_Aoki_Alan_Walker_Isak_-_Are_You_Lonely.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)   
                        
                        
                    
                if t == '18':
                    path = pathlib.Path('C:/Users/'+ user +'/01/TOMYGONE_Amvis_-_What_More.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/TOMYGONE_Amvis_-_What_More.mp3')
                        os.system('cls')
                        time.sleep(1)
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)   
               
                if t == '19':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Оксимирон - Цунами.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Оксимирон - Цунами.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '20':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Annodomini - Никто не Нужен.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Annodomini - Никто не Нужен.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '21':
                    path = pathlib.Path('C:/Users/'+ user +'/01/AC_DC - WAR MACHINE.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/AC_DC - WAR MACHINE.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)        
                
                if t == '22':
                    path = pathlib.Path('C:/Users/'+ user +'/01/AC_DC - T_N_T.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/AC_DC - T_N_T.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)        
                
                if t == '23':
                    path = pathlib.Path('C:/Users/'+ user +'/01/AC_DC - Thunderstruck.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/AC_DC - Thunderstruck.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '24':
                    path = pathlib.Path('C:/Users/'+ user +'/01/AC_DC - Highway to Hell.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/AC_DC - Highway to Hell.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                
                if t == '25':
                    path = pathlib.Path('C:/Users/'+ user +'/01/AC_DC - Back in Black.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/AC_DC - Back in Black.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                
                if t == '26':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Ghostemane - Fed Up.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Ghostemane - Fed Up.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                
                if t == '27':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Ghostemane - Venom.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Ghostemane - Venom.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                
                if t == '28':
                    path = pathlib.Path('C:/Users/'+ user +'/01/uicedeboy - LTE.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/uicedeboy - LTE.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '29':
                    path = pathlib.Path('C:/Users/'+ user +'/01/uicideboy - Paris.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/uicideboy - Paris.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '30':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Lil Peep - Star Shopping.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Lil Peep - Star Shopping.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '31':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Король и Шут - Лесник.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Король и Шут - Лесник.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '32':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Lost Frequencies - Reality.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Lost Frequencies - Reality.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '33':
                    path = pathlib.Path('C:/Users/'+ user +'/01/The Score - Head Up.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/The Score - Head Up.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '34':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Disturbed - Old Friend.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Disturbed - Old Friend.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                
                if t == '35':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Король и Шут - Кукла колдуна.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Король и Шут - Кукла колдуна.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '36':
                    path = pathlib.Path('C:/Users/'+ user +'/01/БИ-2, oxxxymiron - Пора возвращаться домой.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/БИ-2, oxxxymiron - Пора возвращаться домой.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '37':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Blues Saraceno - Dogs of War.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Blues Saraceno - Dogs of War.mp3')
                        os.system('cls')  
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                        
                if t == '38':
                    path = pathlib.Path('C:/Users/'+ user +'/01/БИ-2 - Большие города.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/БИ-2 - Большие города.mp3')
                        os.system('cls') 
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '39':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Thousand Foot Krutch - Take It Out On Me.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Thousand Foot Krutch - Take It Out On Me.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                
                if t == '40':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Skillet - Back to Life.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Skillet - Back to Life.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '41':
                    path = pathlib.Path('C:/Users/'+ user +'/01/K.Flay - High Enough.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/K.Flay - High Enough.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '42':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Three Days Grace - So Called Life.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Three Days Grace - So Called Life.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '43':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Chvrches, Matt Berninger - My Enemy.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Chvrches, Matt Berninger - My Enemy.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '44':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Bishop Briggs - River.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Bishop Briggs - River.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '45':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Disturbed - Liberate.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Disturbed - Liberate.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '46':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron, Porchy - Earth Burns.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron, Porchy - Earth Burns.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '47':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Papa Roach - Last Resort.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Papa Roach - Last Resort.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '48':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Slipknot - Dead Memories.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Slipknot - Dead Memories.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '49':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Dope - Die MF Die.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Dope - Die MF Die.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '50':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Slipknot - Before I Forget.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Slipknot - Before I Forget.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                
                if t == '51':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Александр Пушной - Всё идёт по плану.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Александр Пушной - Всё идёт по плану.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '52':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Би-2 - Чёрное солнце.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Би-2 - Чёрное солнце.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '53':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib).mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib).mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '54':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Дело нескольких минут (3 раунд, 17 ib).mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Дело нескольких минут (3 раунд, 17 ib).mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '55':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib).mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib).mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '56':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - В долгий путь (1 раунд 17ib).mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - В долгий путь (1 раунд 17ib).mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '57':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - До зимы.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - До зимы.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '58':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Не от мира сего.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Не от мира сего.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '59':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Признаки жизни.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Признаки жизни.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '60':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Детектор лжи.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Детектор лжи.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '61':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Хитиновый покров.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Хитиновый покров.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '62':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Волапюк.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Волапюк.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '63':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Больше Бена.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Больше Бена.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                        
                if t == '64':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Цифры и цвета.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Цифры и цвета.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '65':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Где нас нет.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Где нас нет.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '66':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Башня из слоновой кости.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Башня из слоновой кости.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '67':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Слово мэра.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Слово мэра.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '68':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Накануне.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Накануне.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '69':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Полигон.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Полигон.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '70':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Колыбельная.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Колыбельная.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '71':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Переплетено.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Переплетено.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '72':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Всего лишь писатель.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Всего лишь писатель.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '73':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Кем ты стал.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Кем ты стал.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '74':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron - Город под подошвой.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron - Город под подошвой.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '75':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron ft. пиэм ft. J. Makonnen ft. Dinast ft. Letai ft. PALMDROPOV - Reality.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron ft. пиэм ft. J. Makonnen ft. Dinast ft. Letai ft. PALMDROPOV - Reality.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
                if t == '76':
                    path = pathlib.Path('C:/Users/'+ user +'/01/Oxxxymiron, Markul - Fata Morgana.mp3')
                    if path.exists() == True:
                        os.startfile('C:/Users/'+ user +'/01/Oxxxymiron, Markul - Fata Morgana.mp3')
                        os.system('cls')
                        time.sleep(1)  
                    else:
                        print('         Этого фала нет в директории')
                        time.sleep(3.5)
                        os.system('cls')
                        time.sleep(1)
                                                
               
                        
                
                
                
        if s == '11':
                webbrowser.open_new_tab('https://disk.yandex.ru/client/disk')
        
        if s == '12':
                print('  !Все приложения только на android!')
                time.sleep(0.5)
                colorama.init()
                print('\n')
                print(colorama.Fore.CYAN+'       |'+Fore.GREEN+'--------------------------------------'+Fore.CYAN+'|')
                print(colorama.Fore.CYAN+'       |'+Fore.WHITE+' 1. Яндекс музыка'+colorama.Fore.CYAN+'                     |')
                print(colorama.Fore.CYAN+'       |'+Fore.GREEN+'--------------------------------------'+Fore.CYAN+'|')
                print(colorama.Fore.CYAN+'       |'+Fore.WHITE+' 2. Ютуб без рекламы (YouTube Vanced)'+colorama.Fore.CYAN+' |')
                print(colorama.Fore.CYAN+'       |'+Fore.GREEN+'--------------------------------------'+Fore.CYAN+'|')
                print(colorama.Fore.CYAN+'       |'+Fore.WHITE+' 3. VK Coffe'+colorama.Fore.CYAN+'                          |')
                print(colorama.Fore.CYAN+'       |'+Fore.GREEN+'--------------------------------------'+Fore.CYAN+'|')
                print(colorama.Fore.CYAN+'       |'+Fore.WHITE+' 4. VPN ORBOT'+colorama.Fore.CYAN+'                         |')
                print(colorama.Fore.CYAN+'       |'+Fore.GREEN+'--------------------------------------'+Fore.CYAN+'|')
                print(colorama.Fore.CYAN+'       |'+Fore.WHITE+' 5. BOOM (vk music)'+colorama.Fore.CYAN+'                   |')
                print(colorama.Fore.CYAN+'       |'+Fore.GREEN+'--------------------------------------'+Fore.CYAN+'|')
                print(Style.RESET_ALL)
                lk = input('  Введите номер --> ')
                os.system('cls')
                if lk ==  '1':
                        print('''\n               Яндекс музыка
                                Модификации:
                                Без рекламы, подписка (но она работает только в этом приложении)
                                Ссылка на скачивание - https://disk.yandex.ru/d/QZfTggdnmwgX6g
                                Телеграм - EasyAPK''')
                        
                        print(colorama.Fore.GREEN+'      |'+Fore.WHITE+'   Переход на сайт')
                        time.sleep(2)
                        webbrowser.open_new_tab('https://disk.yandex.ru/d/QZfTggdnmwgX6g')
                        t30()
                if lk == '2':
                        print('\n         Ютуб без рекламы (YouTube Vanced)')
                        print('''               Модификации:
                                        Просмотр всех видео без рекламы, автопропуск встроенной рекламы, различные темы и т.д
                                        Сайт - https://vancedapp.com/
                                        Скачается установщик программ Vanced''')
                        print(colorama.Fore.GREEN+'      |'+Fore.WHITE+'   Переход на сайт')
                        time.sleep(2)
                        webbrowser.open_new_tab('https://vancedapp.com/')
                        t30()
                if lk == '3':
                        print('\n')
                        print('                 VK Coffe\n')
                        print('''               Модификации:
                                Режим ofline, нечиталка, отключить тайпинг, шифрование, смена иконки клиента, отключение рекламы и др
                                Сайт - https://vk-coffee.ru/
                                Телеграм - https://t.me/s/VKCoffee''')
                        print(colorama.Fore.GREEN+'      |'+Fore.WHITE+'   Переход на сайт')
                        time.sleep(2)
                        webbrowser.open_new_tab('https://vk-coffee.ru/')
                        t30()
                        
                if lk == '4':
                        print('\n')
                        print('                        VPN ORBOT')
                        print('\n')
                        print('''               Модификации:
                                VPN сервис, который скрывает ваш настоящий ip
                                Есть выбор приложений, которые будут запускаться через VPN
                                Есть выбор стран
                                Сайт - https://trashbox.ru/link/orbot-android
                                В Google Play - Orbot''')
                        print(colorama.Fore.GREEN+'      |'+Fore.WHITE+'   Переход на сайт')
                        time.sleep(2)
                        webbrowser.open_new_tab('https://trashbox.ru/link/orbot-android')
                        t30()
                if lk == '5':
                        print('\n')
                        print('                 BOOM (vk music)')
                        print('\n')
                        print('''               Модификации:
                                Подписка, музыка без рекламы, скачивание музыки
                                Минусы - расшифровать скачаные файлы невозможно, т.е послушать музыку в проигрывателе нельзя
                                Доступны 3 версии на сайте - https://www.alpha-ag.ru/programs/20042-vzlomannaya-boom-vip.html
                                Скачать с диска - https://disk.yandex.ru/d/gcd42c3xe-h1mQ
                                Телеграм - EasyAPK''')
                        colorama.init()
                        print('\n\n'+colorama.Fore.GREEN+'       Изменения в обновлении vk music 6.0.9:')
                        print(colorama.Fore.WHITE+'''               — Вернули пропадающий плеер в шторке уведомлений;
                                    — Снизили вероятность появления "ошибки воспроизведения";
                                    — Вылечили ряд крешей.''')
                        print(colorama.Fore.GREEN+'      |'+Fore.WHITE+'   Переход на сайт')
                        time.sleep(2)
                        webbrowser.open_new_tab('https://disk.yandex.ru/d/gcd42c3xe-h1mQ')
                        print('\n')
                        sys.stdout.write(' Закрытие этой вкладки - 45с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 44с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 43с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 42с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 41с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 40с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 39с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 38с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 37с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 36с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 35с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 34с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 33с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 32с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 31с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 30с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 29с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 28с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 27с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 26с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 25с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 24с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 23с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 22с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 21с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 20с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 19с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 18с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 17с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 16с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 15с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 14с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 13с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 12с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 11с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 10с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 9с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 8с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 7с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 6с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 5с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 4с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 3с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 2с \r')
                        time.sleep(1)
                        sys.stdout.write(' Закрытие этой вкладки - 1с \r')
                        time.sleep(1)
                        os.system('cls')
                        
        if s == '13':
            print('\n     1. Почта, 2. Тг канал')
            l = input('\n  Что открыть ->  ')
            os.system('cls')
            if l == '1':
                colorama.init()
                print('\n\n'+ colorama.Fore.YELLOW+'\n      Пожалуйста'+ Fore.WHITE+' укажите тему: баг/ошибка\n     Мне удобно, а вам приятно')
                time.sleep(3.5)
                webbrowser.open_new_tab('https://mail.yandex.ru/compose/?to=Help-753@yandex.ru')
                os.system('cls')
                 
            if l == '2':
                 webbrowser.open_new_tab('https://t.me/programma_py')
                 os.system('cls')
        if s == '0':
            break
        