import os
import sys
import pathlib
from pathlib import Path
from os import environ, getcwd
import urllib.request
import time
import colorama
from colorama import Fore, Back, Style



getUser = lambda: environ['USERNAME']
a = getUser()


colorama.init()


try:
    d = 'c:/Users/'+a+'/01'
    os.mkdir(d)
    print('         Папка 01 создана в '+ d)
except FileExistsError:
    print("     Эта папка"+ colorama.Fore.CYAN+ ' уже '+ Style.RESET_ALL +'существует\n')
    time.sleep(3)
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_-_Alone.mp3')
if path.exists() == False:
    
    url = 'https://ru.hitmotop.com/get/music/20170916/Alan_Walker_-_Alone_48615855.mp3'
    urllib.request.urlretrieve(url, 'c:/Users/'+a+'/01/Alan_Walker_-_Alone.mp3') 
    print('\n     Файл Alan Walker - Alone' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('\n     Файл Alan Walker - Alone'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_-_Sing_Me_to_Sleep.mp3')
if path.exists() == False:
    url2 = 'https://ru.hitmotop.com/get/music/20170916/Alan_Walker_-_Sing_Me_to_Sleep_48615865.mp3'
    urllib.request.urlretrieve(url2, 'c:/Users/'+a+'/01/Alan_Walker_-_Sing_Me_to_Sleep.mp3')
    print('     Файл Alan Walker - Sing Me to Sleep' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
    
else:
    print('     Файл Alan Walker - Sing Me to Sleep'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    

path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_AAP_Rocky_-_Live_Fast.mp3')
if path.exists() == False:
    url3 = 'https://ru.hitmotop.com/get/music/20190726/Alan_Walker_AAP_Rocky_-_Live_Fast_65685794.mp3'
    urllib.request.urlretrieve(url3, 'c:/Users/'+a+'/01/Alan_Walker_AAP_Rocky_-_Live_Fast.mp3')
    print('     Файл Alan Walker, AAP Rocky - Live_Fast' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Alan Walker, AAP Rocky - Live_Fast'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')



path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_Imanbek_-_Sweet_Dreams.mp3')
if path.exists() == False:
    url4 = 'https://ru.hitmotop.com/get/music/20210611/Alan_Walker_Imanbek_-_Sweet_Dreams_72998823.mp3'
    urllib.request.urlretrieve(url4, 'c:/Users/'+a+'/01/Alan_Walker_Imanbek_-_Sweet_Dreams.mp3')
    print('     Файл Alan Walker, Imanbek - Sweet Dreams' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Alan Walker, Imanbek - Sweet Dreamst'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    

path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_ISK_-_Sorry.mp3')
if path.exists() == False:                      
    url5 = 'https://ru.hitmotop.com/get/music/20210129/Alan_Walker_ISK_-_Sorry_72487884.mp3'
    urllib.request.urlretrieve(url5, 'c:/Users/'+a+'/01/Alan_Walker_ISK_-_Sorry.mp3')
    print('     Файл Alan Walker, ISK - Sorry' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Alan Walker, ISK - Sorry'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/CHVRCHS_Steve_Mac_Chris_Laws_Iain_Cook_Martin_Doherty_Lauren_Mayberry.mp3')
if path.exists() == False:
    url6 = 'https://ru.hitmotop.com/get/music/20180415/CHVRCHS_Steve_Mac_Chris_Laws_Iain_Cook_Martin_Doherty_Lauren_May_-_Miracle_55326188.mp3'
    urllib.request.urlretrieve(url6, 'c:/Users/'+a+'/01/CHVRCHS_Steve_Mac_Chris_Laws_Iain_Cook_Martin_Doherty_Lauren_Mayberry.mp3')
    print('     Файл CHVRCHS, Steve Mac, Chris Laws, Iain Cook, Martin Doherty, Lauren May - Miracle' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл CHVRCHS, Steve Mac, Chris Laws, Iain Cook, Martin Doherty, Lauren May - Miracle'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/Clandestina.mp3')
if path.exists() == False:
    url7 = 'https://ru.hitmotop.com/get/music/20190907/Filv_Edmofo_Emma_Peters_-_Clandestina_66465349.mp3'
    urllib.request.urlretrieve(url7, 'c:/Users/'+a+'/01/Clandestina.mp3')
    print('     Файл Clandestina' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Clandestina'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')   
    
 
path = pathlib.Path('C:/Users/'+ a +'/01/Eminem_-_Rap_God.mp3')
if path.exists() == False:                          
    url8 = 'https://ru.hitmotop.com/get/music/20170902/Eminem_-_Rap_God_47964975.mp3'
    urllib.request.urlretrieve(url8, 'c:/Users/'+a+'/01/Eminem_-_Rap_God.mp3')
    print('     Файл Eminem - Rap God' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Eminem - Rap God'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')             
          

path = pathlib.Path('C:/Users/'+ a +'/01/Eva_Simons_-_Bludfire.mp3')
if path.exists() == False:                                      
    url9 = 'https://ru.hitmotop.com/get/music/20170901/Eva_Simons_-_Bludfire_47911889.mp3'
    urllib.request.urlretrieve(url9, 'c:/Users/'+a+'/01/Eva_Simons_-_Bludfire.mp3')
    print('     Файл Eva Simons - Bludfire' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Eva_Simons - Bludfire'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')       
      

path = pathlib.Path('C:/Users/'+ a +'/01/Hans_Zimmer_-_End_Credits.mp3')
if path.exists() == False:                         
    url10 = 'https://ru.hitmotop.com/get/music/20180429/Hans_Zimmer_-_End_Credits_55636452.mp3'
    urllib.request.urlretrieve(url10, 'c:/Users/'+a+'/01/Hans_Zimmer_-_End_Credits.mp3')
    print('     Файл Hans Zimmer - End Credits' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Zimmer - End Credits'+ colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    

    
    

    
path = pathlib.Path('C:/Users/'+ a +'/01/Katy_Perry_Juicy_J_-_Dark_Horse.mp3')
if path.exists() == False:                          
    url11 = 'https://ru.hitmotop.com/get/music/20170830/Katy_Perry_Juicy_J_-_Dark_Horse_47836298.mp3'
    urllib.request.urlretrieve(url11, 'c:/Users/'+a+'/01/Katy_Perry_Juicy_J_-_Dark_Horse.mp3')
    print('     Файл Katy Perry, Juicy J - Dark Horse' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Katy Perry, Juicy J - Dark Horse'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die.mp3')
if path.exists() == False:                         
    url12 = 'https://ru.hitmotop.com/get/music/20180303/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die_54268252.mp3'
    urllib.request.urlretrieve(url12, 'c:/Users/'+a+'/01/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die.mp3')
    print('     Файл Alan Walker - Legends Never Die' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL) 
else:
    print('     Файл Alan Walker - Legends Never Die'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')   
     
 
 
path = pathlib.Path('C:/Users/'+ a +'/01/Leonid_Rudenko_ARITMIYA_-_Rain_Sun.mp3')
if path.exists() == False:                          
    url13 = 'https://ru.hitmotop.com/get/music/20191112/Leonid_Rudenko_ARITMIYA_-_Rain_Sun_67253102.mp3'
    urllib.request.urlretrieve(url13, 'c:/Users/'+a+'/01/Leonid_Rudenko_ARITMIYA_-_Rain_Sun.mp3')
    print('     Файл Leonid Rudenko, ARITMIYA - Rain Sun' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Leonid Rudenko, ARITMIYA - Rain Sun'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n') 
    
    
 
path = pathlib.Path('C:/Users/'+ a +'/01/Minelli_-_Rampampam.mp3')
if path.exists() == False:                          
    url14 = 'https://ru.hitmotop.com/get/music/20210326/Minelli_-_Rampampam_72874060.mp3'
    urllib.request.urlretrieve(url14, 'c:/Users/'+a+'/01/Minelli_-_Rampampam.mp3')
    print('     Файл Minelli - Rampampam' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Minelli - Rampampam'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n') 
    
    
    

path = pathlib.Path('C:/Users/'+ a +'/01/Nessa_Barrett_jxdn_-_la_di_die.mp3')
if path.exists() == False:                         
    url15 = 'https://ru.hitmotop.com/get/music/20210223/Nessa_Barrett_jxdn_-_la_di_die_72757984.mp3'
    urllib.request.urlretrieve(url15, 'c:/Users/'+a+'/01/Nessa_Barrett_jxdn_-_la_di_die.mp3')
    print('     Файл Nessa, Barrett jxdn - la di die' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Nessa, Barrett jxdn - la di die'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n') 
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Parah_Dice_-_Hot.mp3')
if path.exists() == False:                           
    url16 = 'https://ru.hitmotop.com/get/music/20190904/Parah_Dice_-_Hot_66419964.mp3'
    urllib.request.urlretrieve(url16, 'c:/Users/'+a+'/01/Parah_Dice_-_Hot.mp3')
    print('     Файл Parah Dice - Hot' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Parah Dice - Hot'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')    
    
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Steve_Aoki_Alan_Walker_Isak_-_Are_You_Lonely.mp3')
if path.exists() == False:                           
    url17 = 'https://ru.hitmotop.com/get/music/20190223/Steve_Aoki_Alan_Walker_Isak_-_Are_You_Lonely_62321994.mp3'
    urllib.request.urlretrieve(url17, 'c:/Users/'+a+'/01/Steve_Aoki_Alan_Walker_Isak_-_Are_You_Lonely.mp3')
    print('     Файл Steve Aoki, Alan Walker, Isak - Are You Lonely' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Steve Aoki, Alan_Walker, Isak - Are You Lonely'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')  
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/TOMYGONE_Amvis_-_What_More.mp3')
if path.exists() == False:                           
    url18 = 'https://ru.hitmotop.com/get/music/20190321/TOMYGONE_Amvis_-_What_More_62936027.mp3'
    urllib.request.urlretrieve(url18, 'c:/Users/'+a+'/01/TOMYGONE_Amvis_-_What_More.mp3')
    print('     Файл TOMYGONE Amvis - What More' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл TOMYGONE Amvis - What More'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n') 

             
path = pathlib.Path('C:/Users/'+ a +'/01/Оксимирон - Цунами.mp3')
if path.exists() == False:                           
    url19 = 'https://ru.hitmotop.com/get/music/20211109/Oxxxymiron_-_CUNAMI_73294261.mp3'
    urllib.request.urlretrieve(url19, 'c:/Users/'+a+'/01/Оксимирон - Цунами.mp3')
    print('     Файл Оксимирон - Цунами' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Оксимирон - Цунами'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n') 

path = pathlib.Path('C:/Users/'+ a +'/01/Annodomini - Никто не Нужен.mp3')
if path.exists() == False:                           
    url20 = 'https://cdn.2mz.me/api/track/tuaKtoah'
    urllib.request.urlretrieve(url20, 'c:/Users/'+a+'/01/Annodomini - Никто не Нужен.mp3')
    print('     Файл Annodomini - Никто не Нужен' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Annodomini - Никто не Нужен'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - WAR MACHINE.mp3')
if path.exists() == False:                           
    url21 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_War_Machine_47830058.mp3'
    urllib.request.urlretrieve(url21, 'c:/Users/'+a+'/01/AC_DC - WAR MACHINE.mp3')
    print('     Файл AC_DC - WAR MACHINE ' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл AC_DC - WAR MACHINE'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - T_N_T.mp3')
if path.exists() == False:                           
    url22 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_TNT_47830049.mp3'
    urllib.request.urlretrieve(url22, 'c:/Users/'+a+'/01/AC_DC - T_N_T.mp3')
    print('     Файл AC_DC - T.N.T' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл AC_DC - T.N.T'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')

path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - Thunderstruck.mp3')
if path.exists() == False:                           
    url23 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_Thunderstruck_47830044.mp3'
    urllib.request.urlretrieve(url23, 'c:/Users/'+a+'/01/AC_DC - Thunderstruck.mp3')
    print('     Файл AC_DC - Thunderstruck' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл AC_DC - Thunderstruck'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - Highway to Hell.mp3')
if path.exists() == False:                           
    url24 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_Highway_to_Hell_47830059.mp3'
    urllib.request.urlretrieve(url24, 'c:/Users/'+a+'/01/AC_DC - Highway to Hell.mp3')
    print('     Файл AC_DC - Highway to Hell' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл AC_DC - Highway to Hell'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - Back in Black.mp3')
if path.exists() == False:                           
    url25 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_Back_In_Black_47830042.mp3'
    urllib.request.urlretrieve(url25, 'c:/Users/'+a+'/01/AC_DC - Back in Black.mp3')
    print('     Файл AC_DC - Back in Black' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл AC_DC - Back in Black'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/Ghostemane - Fed Up.mp3')
if path.exists() == False:                           
    url26 = 'https://ru.hitmotop.com/get/music/20201022/Ghostemane_-_Fed_Up_71339681.mp3'
    urllib.request.urlretrieve(url26, 'c:/Users/'+a+'/01/Ghostemane - Fed Up.mp3')
    print('     Файл Ghostemane - Fed Up' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Ghostemane - Fed Up'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    

path = pathlib.Path('C:/Users/'+ a +'/01/Ghostemane - Venom.mp3')
if path.exists() == False:                           
    url27 = 'https://ru.hitmotop.com/get/music/20180217/Ghostemane_-_Venom_53899755.mp3'
    urllib.request.urlretrieve(url27, 'c:/Users/'+a+'/01/Ghostemane - Venom.mp3')
    print('     Файл Ghostemane - Venom' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Ghostemane - Venom'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/uicedeboy - LTE.mp3')
if path.exists() == False:                           
    url28 = 'https://ru.hitmotop.com/get/music/20170902/uicideboy_-_Lte_47965279.mp3'
    urllib.request.urlretrieve(url28, 'c:/Users/'+a+'/01/uicedeboy - LTE.mp3')
    print('     Файл uicedeboy - LTE' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл uicedeboy - LTE'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')  
 
 
 
path = pathlib.Path('C:/Users/'+ a +'/01/uicideboy - Paris.mp3')
if path.exists() == False:                           
    url29 = 'https://ru.hitmotop.com/get/music/20190518/uicideBoy_-_Paris_64294324.mp3'
    urllib.request.urlretrieve(url29, 'c:/Users/'+a+'/01/uicideboy - Paris.mp3')
    print('     Файл uicideboy - Paris' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл uicideboy - Paris'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Lil Peep - Star Shopping.mp3')
if path.exists() == False:                           
    url30 = 'https://ru.hitmotop.com/get/music/20190523/Lil_Peep_-_Star_Shopping_64429583.mp3'
    urllib.request.urlretrieve(url30, 'c:/Users/'+a+'/01/Lil Peep - Star Shopping.mp3')
    print('     Файл Lil Peep - Star Shopping' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Lil Peep - Star Shopping'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Король и Шут - Лесник.mp3')
if path.exists() == False:                           
    url31 = 'https://ru.hitmotop.com/get/music/20190305/Korol_i_SHut_-_Lesnik_62571704.mp3'
    urllib.request.urlretrieve(url31, 'c:/Users/'+a+'/01/Король и Шут - Лесник.mp3')
    print('     Файл Король и Шут - Лесник' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Король и Шут - Лесник'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Lost Frequencies - Reality.mp3')
if path.exists() == False:                           
    url32 = 'https://ru.hitmotop.com/get/music/20170905/Lost_Frequencies_-_Reality_48241226.mp3'
    urllib.request.urlretrieve(url32, 'c:/Users/'+a+'/01/Lost Frequencies - Reality.mp3')
    print('     Файл Lost Frequencies - Reality' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Lost Frequencies - Reality'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/The Score - Head Up.mp3')
if path.exists() == False:                           
    url33 = 'https://ru.hitmotop.com/get/music/20210925/The_Score_-_Head_Up_73172695.mp3'
    urllib.request.urlretrieve(url33, 'c:/Users/'+a+'/01/The Score - Head Up.mp3')
    print('     Файл The Score - Head Up ' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл The Score - Head Up'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Disturbed - Old Friend.mp3')
if path.exists() == False:                           
    url34 = 'https://ru.hitmotop.com/get/music/20170906/Disturbed_-_Old_Friend_48270873.mp3'
    urllib.request.urlretrieve(url34, 'c:/Users/'+a+'/01/Disturbed - Old Friend.mp3')
    print('     Файл Disturbed - Old Friend' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Disturbed - Old Friend'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n') 



path = pathlib.Path('C:/Users/'+ a +'/01/Король и Шут - Кукла колдуна.mp3')
if path.exists() == False:                           
    url35 = 'https://ru.hitmotop.com/get/music/20190305/Korol_i_SHut_-_Kukla_kolduna_62570545.mp3'
    urllib.request.urlretrieve(url35, 'c:/Users/'+a+'/01/Король и Шут - Кукла колдуна.mp3')
    print('     Файл Король и Шут - Кукла колдуна' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Король и Шут - Кукла колдуна'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    

path = pathlib.Path('C:/Users/'+ a +'/01/БИ-2, oxxxymiron - Пора возвращаться домой.mp3')
if path.exists() == False:                           
    url36 = 'https://ru.hitmotop.com/get/music/20190307/Bi-2_i_Oksimiron_-_Pora_vozvrashhatsya_domojj_62621464.mp3'
    urllib.request.urlretrieve(url36, 'c:/Users/'+a+'/01/БИ-2, oxxxymiron - Пора возвращаться домой.mp3')
    print('     Файл БИ-2, oxxxymiron - Пора возвращаться домой' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл БИ-2, oxxxymiron - Пора возвращаться домой'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Blues Saraceno - Dogs of War.mp3')
if path.exists() == False:                           
    url37 = 'https://ru.hitmotop.com/get/music/20190323/Blues_Saraceno_-_Dogs_of_War_62987608.mp3'
    urllib.request.urlretrieve(url37, 'c:/Users/'+a+'/01/Blues Saraceno - Dogs of War.mp3')
    print('     Файл  Blues Saraceno - Dogs of War' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Blues Saraceno - Dogs of War'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
path = pathlib.Path('C:/Users/'+ a +'/01/БИ-2 - Большие города.mp3')
if path.exists() == False:                           
    url38 = 'https://ru.hitmotop.com/get/music/20110924/Bi-2_-_Bolshie_goroda_1447463.mp3'
    urllib.request.urlretrieve(url38, 'c:/Users/'+a+'/01/БИ-2 - Большие города.mp3')
    print('     Файл БИ-2 - Большие города' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл БИ-2 - Большие города'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Thousand Foot Krutch - Take It Out On Me.mp3')
if path.exists() == False:                           
    url39 = 'https://ru.hitmotop.com/get/music/20190202/Thousand_Foot_Krutch_-_Take_It_Out_On_Me_61822012.mp3'
    urllib.request.urlretrieve(url39, 'c:/Users/'+a+'/01/Thousand Foot Krutch - Take It Out On Me.mp3')
    print('     Файл Thousand Foot Krutch - Take It Out On Me' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Thousand Foot Krutch - Take It Out On Me'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')

# kjnbrhjbnjbj
path = pathlib.Path('C:/Users/'+ a +'/01/Skillet - Back to Life.mp3')
if path.exists() == False:                           
    url40 = 'https://ru.hitmotop.com/get/music/20190802/Skillet_-_Back_to_Life_65833904.mp3'
    urllib.request.urlretrieve(url40, 'c:/Users/'+a+'/01/Skillet - Back to Life.mp3')
    print('     Файл Skillet - Back to Life' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл  Skillet - Back to Life'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/K.Flay - High Enough.mp3')
if path.exists() == False:                           
    url41 = 'https://ru.hitmotop.com/get/music/20170907/KFlay_-_High_Enough_48324857.mp3'
    urllib.request.urlretrieve(url41, 'c:/Users/'+a+'/01/K.Flay - High Enough.mp3')
    print('     Файл K.Flay - High Enough' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл K.Flay - High Enough'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
  
  
path = pathlib.Path('C:/Users/'+ a +'/01/Three Days Grace - So Called Life.mp3')
if path.exists() == False:                           
    url42 = 'https://ru.hitmotop.com/get/music/20211130/Three_Days_Grace_-_So_Called_Life_73405444.mp3'
    urllib.request.urlretrieve(url42, 'c:/Users/'+a+'/01/Three Days Grace - So Called Life.mp3')
    print('     Файл Three Days Grace - So Called Life' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Three Days Grace - So Called Life'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Chvrches, Matt Berninger - My Enemy.mp3')
if path.exists() == False:                           
    url43 = 'https://ru.hitmotop.com/get/music/20180304/CHVRCHS_Matt_Berninger_-_My_Enemy_54291829.mp3'
    urllib.request.urlretrieve(url43, 'c:/Users/'+a+'/01/Chvrches, Matt Berninger - My Enemy.mp3')
    print('     Файл Chvrches, Matt Berninger - My Enemy' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Chvrches, Matt Berninger - My Enemy'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Bishop Briggs - River.mp3')
if path.exists() == False:                           
    url44 = 'https://ru.hitmotop.com/get/music/20170907/Bishop_Briggs_-_River_48327621.mp3'
    urllib.request.urlretrieve(url44, 'c:/Users/'+a+'/01/Bishop Briggs - River.mp3')
    print('     Файл Bishop Briggs - River' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Bishop Briggs - River'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Disturbed - Liberate.mp3')
if path.exists() == False:                           
    url45 = 'https://ru.hitmotop.com/get/music/20170830/Disturbed_-_Liberate_47829330.mp3'
    urllib.request.urlretrieve(url45, 'c:/Users/'+a+'/01/Disturbed - Liberate.mp3')
    print('     Файл  Disturbed - Liberate' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Disturbed - Liberate'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Oxxxymiron, Porchy - Earth Burns.mp3')
if path.exists() == False:                           
    url46 = 'https://ru.hitmotop.com/get/music/20191202/Oxxxymiron_PORCHY_-_Earth_Burns_67486938.mp3'
    urllib.request.urlretrieve(url46, 'c:/Users/'+a+'/01/Oxxxymiron, Porchy - Earth Burns.mp3')
    print('     Файл Oxxxymiron, Porchy - Earth Burns' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Oxxxymiron, Porchy - Earth Burns'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Papa Roach - Last Resort.mp3')
if path.exists() == False:                           
    url47 = 'https://ru.hitmotop.com/get/music/20170831/Papa_Roach_-_Last_Resort_47872825.mp3'
    urllib.request.urlretrieve(url47, 'c:/Users/'+a+'/01/Papa Roach - Last Resort.mp3')
    print('     Файл Papa Roach - Last Resort' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Papa Roach - Last Resort'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Slipknot - Dead Memories.mp3')
if path.exists() == False:                           
    url48 = 'https://ru.hitmotop.com/get/music/20170902/Slipknot_-_Dead_Memories_47954351.mp3'
    urllib.request.urlretrieve(url48, 'c:/Users/'+a+'/01/Slipknot - Dead Memories.mp3')
    print('     Файл Slipknot - Dead Memories' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Slipknot - Dead Memories'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
path = pathlib.Path('C:/Users/'+ a +'/01/Dope - Die MF Die.mp3')
if path.exists() == False:                           
    url49 = 'https://ru.hitmotop.com/get/music/20170831/Dope_-_Die_MF_Die_47880361.mp3'
    urllib.request.urlretrieve(url49, 'c:/Users/'+a+'/01/Dope - Die MF Die.mp3')
    print('     Файл Dope - Die MF Die' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Dope - Die MF Die'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    


    
path = pathlib.Path('C:/Users/'+ a +'/01/Slipknot - Before I Forget.mp3')
if path.exists() == False:                           
    url50 = 'https://ru.hitmotop.com/get/music/20170902/Slipknot_-_Before_I_Forget_47954384.mp3'
    urllib.request.urlretrieve(url50, 'c:/Users/'+a+'/01/Slipknot - Before I Forget.mp3')
    print('     Файл Slipknot - Before I Forget' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Slipknot - Before I Forget'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Александр Пушной - Всё идёт по плану.mp3')
if path.exists() == False:                           
    url51 = 'https://ru.hitmotop.com/get/music/20210402/Aleksandr_Pushnojj_-_Vsjo_idjot_po_planu_72885602.mp3'
    urllib.request.urlretrieve(url51, 'c:/Users/'+a+'/01/Александр Пушной - Всё идёт по плану.mp3')
    print('     Файл Александр Пушной - Всё идёт по плану' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Александр Пушной - Всё идёт по плану'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Би-2 - Чёрное солнце.mp3')
if path.exists() == False:                           
    url52 = 'https://ru.hitmotop.com/get/music/20170929/Bi-2_-_CHjornoe_solnce_49018604.mp3'
    urllib.request.urlretrieve(url52, 'c:/Users/'+a+'/01/Би-2 - Чёрное солнце.mp3')
    print('     Файл Би-2 - Чёрное солнце' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
else:
    print('     Файл Би-2 - Чёрное солнце'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
    
    
time.sleep(1)
path = pathlib.Path('C:/Users/'+ a + '/oksy.py')
if path.exists() == True:
    print('\n Открываю oksy.py\n')
    time.sleep(3)
    os.system('C:/Users/'+ a + '/oksy.py')   
if path.exists() == False:
    print(" Этой программы у вас нет")
    time.sleep(3)
    os.system('cls')
    

    
time.sleep(3)
os.system('cls')
