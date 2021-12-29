import os
import sys
import pathlib
from pathlib import Path
from os import environ, getcwd
import urllib.request
import time

getUser = lambda: environ['USERNAME']
a = getUser()



try:
    d = 'c:/Users/'+a+'/01'
    os.mkdir(d)
    print('         Папка 01 создана в '+ d)
except FileExistsError:
    print("     Эта папка уже существует")
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_-_Alone.mp3')
if path.exists() == False:
    url = 'https://moa.hotmo.org/get/music/20170916/Alan_Walker_-_Alone_48615855.mp3'
    urllib.request.urlretrieve(url, 'c:/Users/'+a+'/01/Alan_Walker_-_Alone.mp3')
    print('\n     Файл Alan Walker - Alone скачан\n')
else:
    print('\n     Файл Alan Walker - Alone уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_-_Sing_Me_to_Sleep.mp3')
if path.exists() == False:
    url2 = 'https://moa.hotmo.org/get/music/20170916/Alan_Walker_-_Sing_Me_to_Sleep_48615865.mp3'
    urllib.request.urlretrieve(url2, 'c:/Users/'+a+'/01/Alan_Walker_-_Sing_Me_to_Sleep.mp3')
    print('     Файл Alan Walker - Sing Me to Sleep скачан\n')
    
else:
    print('     Файл Alan Walker - Sing Me to Sleep уже скачан\n')
    

path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_AAP_Rocky_-_Live_Fast.mp3')
if path.exists() == False:
    url3 = 'https://moa.hotmo.org/get/music/20190726/Alan_Walker_AAP_Rocky_-_Live_Fast_65685794.mp3'
    urllib.request.urlretrieve(url3, 'c:/Users/'+a+'/01/Alan_Walker_AAP_Rocky_-_Live_Fast.mp3')
    print('     Файл Alan Walker, AAP Rocky - Live_Fast скачан\n')
else:
    print('     Файл Alan Walker, AAP Rocky - Live_Fast уже скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_Imanbek_-_Sweet_Dreams.mp3')
if path.exists() == False:
    url4 = 'https://moa.hotmo.org/get/music/20210611/Alan_Walker_Imanbek_-_Sweet_Dreams_72998823.mp3'
    urllib.request.urlretrieve(url4, 'c:/Users/'+a+'/01/Alan_Walker_Imanbek_-_Sweet_Dreams.mp3')
    print('     Файл Alan Walker, Imanbek - Sweet Dreams скачан\n')
else:
    print('     Файл Alan Walker, Imanbek - Sweet Dreams уже скачан\n')
    

path = pathlib.Path('C:/Users/'+ a +'/01/Alan_Walker_ISK_-_Sorry.mp3')
if path.exists() == False:                      
    url5 = 'https://moa.hotmo.org/get/music/20210129/Alan_Walker_ISK_-_Sorry_72487884.mp3'
    urllib.request.urlretrieve(url5, 'c:/Users/'+a+'/01/Alan_Walker_ISK_-_Sorry.mp3')
    print('     Файл Alan Walker, ISK - Sorry скачан\n')
else:
    print('     Файл Alan Walker, ISK - Sorry уже скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/CHVRCHS_Steve_Mac_Chris_Laws_Iain_Cook_Martin_Doherty_Lauren_Mayberry.mp3')
if path.exists() == False:
    url6 = 'https://moa.hotmo.org/get/music/20180415/CHVRCHS_Steve_Mac_Chris_Laws_Iain_Cook_Martin_Doherty_Lauren_May_-_Miracle_55326188.mp3'
    urllib.request.urlretrieve(url6, 'c:/Users/'+a+'/01/CHVRCHS_Steve_Mac_Chris_Laws_Iain_Cook_Martin_Doherty_Lauren_Mayberry.mp3')
    print('     Файл CHVRCHS, Steve Mac, Chris Laws, Iain Cook, Martin Doherty, Lauren May - Miracle скачан\n')
else:
    print('     Файл CHVRCHS, Steve Mac, Chris Laws, Iain Cook, Martin Doherty, Lauren May - Miracle уже скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/Clandestina.mp3')
if path.exists() == False:
    url7 = 'https://moa.hotmo.org/get/music/20190907/Filv_Edmofo_Emma_Peters_-_Clandestina_66465349.mp3'
    urllib.request.urlretrieve(url7, 'c:/Users/'+a+'/01/Clandestina.mp3')
    print('     Файл Clandestina скачан\n')
else:
    print('     Файл Clandestina уже скачан\n')   
    
 
path = pathlib.Path('C:/Users/'+ a +'/01/Eminem_-_Rap_God.mp3')
if path.exists() == False:                          
    url8 = 'https://moa.hotmo.org/get/music/20170902/Eminem_-_Rap_God_47964975.mp3'
    urllib.request.urlretrieve(url8, 'c:/Users/'+a+'/01/Eminem_-_Rap_God.mp3')
    print('     Файл Eminem - Rap God скачан\n')
else:
    print('     Файл Eminem - Rap Go уже скачан\n')             
          

path = pathlib.Path('C:/Users/'+ a +'/01/Eva_Simons_-_Bludfire.mp3')
if path.exists() == False:                                      
    url9 = 'https://moa.hotmo.org/get/music/20170901/Eva_Simons_-_Bludfire_47911889.mp3'
    urllib.request.urlretrieve(url9, 'c:/Users/'+a+'/01/Eva_Simons_-_Bludfire.mp3')
    print('     Файл Eva Simons - Bludfire скачан\n')
else:
    print('     Файл Eva_Simons - Bludfire уже скачан\n')       
      

path = pathlib.Path('C:/Users/'+ a +'/01/Hans_Zimmer_-_End_Credits.mp3')
if path.exists() == False:                         
    url10 = 'https://moa.hotmo.org/get/music/20180429/Hans_Zimmer_-_End_Credits_55636452.mp3'
    urllib.request.urlretrieve(url10, 'c:/Users/'+a+'/01/Hans_Zimmer_-_End_Credits.mp3')
    print('     Файл Hans Zimmer - End Credits скачан\n')
else:
    print('     Файл Zimmer - End Credits уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Katy_Perry_Juicy_J_-_Dark_Horse.mp3')
if path.exists() == False:                          
    url11 = 'https://moa.hotmo.org/get/music/20170830/Katy_Perry_Juicy_J_-_Dark_Horse_47836298.mp3'
    urllib.request.urlretrieve(url11, 'c:/Users/'+a+'/01/Katy_Perry_Juicy_J_-_Dark_Horse.mp3')
    print('     Файл Katy Perry, Juicy J - DarkHorse скачан\n')
else:
    print('     Файл Katy Perry, Juicy J - DarkHorse уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die.mp3')
if path.exists() == False:                         
    url12 = 'https://moa.hotmo.org/get/music/20180303/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die_54268252.mp3'
    urllib.request.urlretrieve(url12, 'c:/Users/'+a+'/01/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die.mp3')
    print('     Файл Alan Walker - Legends Never Die скачан\n') 
else:
    print('     Файл Alan Walker - Legends Never Die уже скачан\n')     
     
 
 
path = pathlib.Path('C:/Users/'+ a +'/01/Leonid_Rudenko_ARITMIYA_-_Rain_Sun.mp3')
if path.exists() == False:                          
    url13 = 'https://moa.hotmo.org/get/music/20191112/Leonid_Rudenko_ARITMIYA_-_Rain_Sun_67253102.mp3'
    urllib.request.urlretrieve(url13, 'c:/Users/'+a+'/01/Leonid_Rudenko_ARITMIYA_-_Rain_Sun.mp3')
    print('     Файл Leonid Rudenko, ARITMIYA - Rain Sun скачан\n')
else:
    print('     Файл eonid Rudenko, ARITMIYA - Rain Sun уже скачан\n') 
    
    
 
path = pathlib.Path('C:/Users/'+ a +'/01/Minelli_-_Rampampam.mp3')
if path.exists() == False:                          
    url14 = 'https://moa.hotmo.org/get/music/20210326/Minelli_-_Rampampam_72874060.mp3'
    urllib.request.urlretrieve(url14, 'c:/Users/'+a+'/01/Minelli_-_Rampampam.mp3')
    print('     Файл Minelli - Rampampam скачан\n')
else:
    print('     Файл Minelli - Rampampam уже скачан\n')
    
    
    

path = pathlib.Path('C:/Users/'+ a +'/01/Nessa_Barrett_jxdn_-_la_di_die.mp3')
if path.exists() == False:                         
    url15 = 'https://moa.hotmo.org/get/music/20210223/Nessa_Barrett_jxdn_-_la_di_die_72757984.mp3'
    urllib.request.urlretrieve(url15, 'c:/Users/'+a+'/01/Nessa_Barrett_jxdn_-_la_di_die.mp3')
    print('     Файл Nessa, Barrett jxdn - la di die скачан\n')
else:
    print('     Файл Nessa, Barrett jxdn - la di die уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Parah_Dice_-_Hot.mp3')
if path.exists() == False:                           
    url16 = 'https://moa.hotmo.org/get/music/20190904/Parah_Dice_-_Hot_66419964.mp3'
    urllib.request.urlretrieve(url16, 'c:/Users/'+a+'/01/Parah_Dice_-_Hot.mp3')
    print('     Файл Parah Dice - Hot скачан\n')
else:
    print('     Файл Parah Dice - Hot уже скачан\n')    
    
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Steve_Aoki_Alan_Walker_Isak_-_Are_You_Lonely.mp3')
if path.exists() == False:                           
    url17 = 'https://moa.hotmo.org/get/music/20190223/Steve_Aoki_Alan_Walker_Isak_-_Are_You_Lonely_62321994.mp3'
    urllib.request.urlretrieve(url17, 'c:/Users/'+a+'/01/Steve_Aoki_Alan_Walker_Isak_-_Are_You_Lonely.mp3')
    print('     Файл Steve Aoki, Alan_Walker, Isak - Are You Lonely скачан\n')
else:
    print('     Файл Steve Aoki, Alan_Walker, Isak - Are You Lonely уже скачан\n')   
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/TOMYGONE_Amvis_-_What_More.mp3')
if path.exists() == False:                           
    url18 = 'https://moa.hotmo.org/get/music/20190321/TOMYGONE_Amvis_-_What_More_62936027.mp3'
    urllib.request.urlretrieve(url18, 'c:/Users/'+a+'/01/TOMYGONE_Amvis_-_What_More.mp3')
    print('     Файл TOMYGONE Amvis - What More скачан\n')
else:
    print('     Файл TOMYGONE Amvis - What More уже скачан\n') 

             
path = pathlib.Path('C:/Users/'+ a +'/01/Оксимирон - Цунами.mp3')
if path.exists() == False:                           
    url19 = 'https://zamp3.net/uploads/music/2021/11/oksimiron-cunami-mp3.mp3'
    urllib.request.urlretrieve(url19, 'c:/Users/'+a+'/01/Оксимирон - Цунами.mp3')
    print('     Файл Оксимирон - Цунами скачан\n')
else:
    print('     Файл Оксимирон - Цунами  уже скачан\n') 

path = pathlib.Path('C:/Users/'+ a +'/01/Annodomini - Никто не Нужен.mp3')
if path.exists() == False:                           
    url20 = 'https://moa.hotmo.org/get/music/20200218/Annodomini_-_Nikto_ne_nuzhen_2020_68445685.mp3'
    urllib.request.urlretrieve(url20, 'c:/Users/'+a+'/01/Annodomini - Никто не Нужен.mp3')
    print('     Файл Annodomini - Никто не Нужен скачан\n')
else:
    print('     Файл Annodomini - Никто не Нужен уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - WAR MACHINE.mp3')
if path.exists() == False:                           
    url21 = 'https://moa.hotmo.org/get/music/20170830/ACDC_-_War_Machine_47830058.mp3'
    urllib.request.urlretrieve(url21, 'c:/Users/'+a+'/01/AC_DC - WAR MACHINE.mp3')
    print('     Файл AC_DC - WAR MACHINE скачан\n')
else:
    print('     Файл AC_DC - WAR MACHINE уже скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - T_N_T.mp3')
if path.exists() == False:                           
    url22 = 'https://moa.hotmo.org/get/music/20170830/ACDC_-_TNT_47830049.mp3'
    urllib.request.urlretrieve(url22, 'c:/Users/'+a+'/01/AC_DC - T_N_T.mp3')
    print('     Файл AC_DC - T.N.T скачан\n')
else:
    print('     Файл AC_DC - T.N.T уже скачан\n')

path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - Thunderstruck.mp3')
if path.exists() == False:                           
    url23 = 'https://moa.hotmo.org/get/music/20170830/ACDC_-_Thunderstruck_47830044.mp3'
    urllib.request.urlretrieve(url23, 'c:/Users/'+a+'/01/AC_DC - Thunderstruck.mp3')
    print('     Файл AC_DC - Thunderstruck скачан\n')
else:
    print('     Файл AC_DC - Thunderstruck уже скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - Highway to Hell.mp3')
if path.exists() == False:                           
    url24 = 'https://moa.hotmo.org/get/music/20170830/ACDC_-_Highway_to_Hell_47830059.mp3'
    urllib.request.urlretrieve(url24, 'c:/Users/'+a+'/01/AC_DC - Highway to Hell.mp3')
    print('     Файл AC_DC - Highway to Hell скачан\n')
else:
    print('     Файл AC_DC - Highway to Hell уже скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/AC_DC - Back in Black.mp3')
if path.exists() == False:                           
    url25 = 'https://moa.hotmo.org/get/music/20170830/ACDC_-_Back_In_Black_47830042.mp3'
    urllib.request.urlretrieve(url25, 'c:/Users/'+a+'/01/AC_DC - Back in Black.mp3')
    print('     Файл AC_DC - Back in Black скачан\n')
else:
    print('     Файл AC_DC - Back in Black уже скачан\n')


path = pathlib.Path('C:/Users/'+ a +'/01/Ghostemane - Fed Up.mp3')
if path.exists() == False:                           
    url26 = 'https://moa.hotmo.org/get/music/20201022/Ghostemane_-_Fed_Up_71339681.mp3'
    urllib.request.urlretrieve(url26, 'c:/Users/'+a+'/01/Ghostemane - Fed Up.mp3')
    print('     Файл Ghostemane - Fed Up скачан\n')
else:
    print('     Файл Ghostemane - Fed Up уже скачан\n')
    

path = pathlib.Path('C:/Users/'+ a +'/01/Ghostemane - Venom.mp3')
if path.exists() == False:                           
    url27 = 'https://moa.hotmo.org/get/music/20180217/Ghostemane_-_Venom_53899755.mp3'
    urllib.request.urlretrieve(url27, 'c:/Users/'+a+'/01/Ghostemane - Venom.mp3')
    print('     Файл Ghostemane - Venom скачан\n')
else:
    print('     Файл Ghostemane - Venom уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/uicedeboy - LTE.mp3')
if path.exists() == False:                           
    url28 = 'https://moa.hotmo.org/get/music/20191218/uicedeboy_-_LTE_67663629.mp3'
    urllib.request.urlretrieve(url28, 'c:/Users/'+a+'/01/uicedeboy - LTE.mp3')
    print('     Файл uicedeboy - LTE скачан\n')
else:
    print('     Файл uicedeboy - LTE уже скачан\n')    
 
 
 
path = pathlib.Path('C:/Users/'+ a +'/01/uicideboy - Paris.mp3')
if path.exists() == False:                           
    url29 = 'https://moa.hotmo.org/get/music/20170902/uicideboy_-_Paris_47965273.mp3'
    urllib.request.urlretrieve(url29, 'c:/Users/'+a+'/01/uicideboy - Paris.mp3')
    print('     Файл uicideboy - Paris скачан\n')
else:
    print('     Файл uicideboy - Paris уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Lil Peep - Star Shopping.mp3')
if path.exists() == False:                           
    url30 = 'https://moa.hotmo.org/get/music/20190523/Lil_Peep_-_Star_Shopping_64429583.mp3'
    urllib.request.urlretrieve(url30, 'c:/Users/'+a+'/01/Lil Peep - Star Shopping.mp3')
    print('     Файл Lil Peep - Star Shopping скачан\n')
else:
    print('     Файл Lil Peep - Star Shopping уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Король и Шут - Лесник.mp3')
if path.exists() == False:                           
    url31 = 'https://moa.hotmo.org/get/music/20170905/Korol_i_SHut_-_Lesnik_48190491.mp3'
    urllib.request.urlretrieve(url31, 'c:/Users/'+a+'/01/Король и Шут - Лесник.mp3')
    print('     Файл Король и Шут - Лесник скачан\n')
else:
    print('     Файл Король и Шут - Лесник уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Lost Frequencies - Reality.mp3')
if path.exists() == False:                           
    url32 = 'https://moa.hotmo.org/get/music/20170905/Lost_Frequencies_-_Reality_48241226.mp3'
    urllib.request.urlretrieve(url32, 'c:/Users/'+a+'/01/Lost Frequencies - Reality.mp3')
    print('     Файл Lost Frequencies - Reality скачан\n')
else:
    print('     Файл Lost Frequencies - Reality уже скачан\n')
    
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/The Score - Head Up.mp3')
if path.exists() == False:                           
    url33 = 'https://moa.hotmo.org/get/music/20210925/The_Score_-_Head_Up_73172695.mp3'
    urllib.request.urlretrieve(url33, 'c:/Users/'+a+'/01/The Score - Head Up.mp3')
    print('     Файл The Score - Head Up скачан\n')
else:
    print('     Файл The Score - Head Up уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Disturbed - Old Friend.mp3')
if path.exists() == False:                           
    url34 = 'https://moa.hotmo.org/get/music/20170906/Disturbed_-_Old_Friend_48270873.mp3'
    urllib.request.urlretrieve(url34, 'c:/Users/'+a+'/01/Disturbed - Old Friend.mp3')
    print('     Файл Disturbed - Old Friend скачан\n')
else:
    print('     Файл Disturbed - Old Friend уже скачан\n') 



path = pathlib.Path('C:/Users/'+ a +'/01/Король и Шут - Кукла колдуна.mp3')
if path.exists() == False:                           
    url35 = 'https://moa.hotmo.org/get/music/20190305/Korol_i_SHut_-_Kukla_kolduna_62570545.mp3'
    urllib.request.urlretrieve(url35, 'c:/Users/'+a+'/01/Король и Шут - Кукла колдуна.mp3')
    print('     Файл Король и Шут - Кукла колдуна скачан\n')
else:
    print('     Файл Король и Шут - Кукла колдуна уже скачан\n')
    

path = pathlib.Path('C:/Users/'+ a +'/01/БИ-2, oxxxymiron - Пора возвращаться домой.mp3')
if path.exists() == False:                           
    url36 = 'https://moa.hotmo.org/get/music/20170929/Bi-2_-_Pora_vozvrashhatsya_domojj_49018611.mp3'
    urllib.request.urlretrieve(url36, 'c:/Users/'+a+'/01/БИ-2, oxxxymiron - Пора возвращаться домой.mp3')
    print('     Файл БИ-2, oxxxymiron - Пора возвращаться домой скачан\n')
else:
    print('     Файл БИ-2, oxxxymiron - Пора возвращаться домой уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Blues Saraceno - Dogs of War.mp3')
if path.exists() == False:                           
    url37 = 'https://moa.hotmo.org/get/music/20190323/Blues_Saraceno_-_Dogs_of_War_62987608.mp3'
    urllib.request.urlretrieve(url37, 'c:/Users/'+a+'/01/Blues Saraceno - Dogs of War.mp3')
    print('     Файл  Blues Saraceno - Dogs of War скачан\n')
else:
    print('     Файл Blues Saraceno - Dogs of War уже скачан\n')
    
path = pathlib.Path('C:/Users/'+ a +'/01/БИ-2 - Большие города.mp3')
if path.exists() == False:                           
    url38 = 'https://moa.hotmo.org/get/music/20110924/Bi-2_-_Bolshie_goroda_1447463.mp3'
    urllib.request.urlretrieve(url38, 'c:/Users/'+a+'/01/БИ-2 - Большие города.mp3')
    print('     Файл БИ-2 - Большие города скачан\n')
else:
    print('     Файл БИ-2 - Большие города уже скачан\n')
    
    
path = pathlib.Path('C:/Users/'+ a +'/01/Thousand Foot Krutch - Take It Out On Me.mp3')
if path.exists() == False:                           
    url39 = 'https://moa.hotmo.org/get/music/20190202/Thousand_Foot_Krutch_-_Take_It_Out_On_Me_61822012.mp3'
    urllib.request.urlretrieve(url39, 'c:/Users/'+a+'/01/Thousand Foot Krutch - Take It Out On Me.mp3')
    print('     Файл Thousand Foot Krutch - Take It Out On Me \n')
else:
    print('     Файл Thousand Foot Krutch - Take It Out On Me уже скачан\n') 

time.sleep(3)
os.system('cls')
