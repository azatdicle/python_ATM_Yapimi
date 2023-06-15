#-*- encode:utf-8 -*-
#Azat Dicle
#Hedefler
#Kartın bir şifresi vardır
#Kartın başlangıçta 500 Tl si vardır
#ATM'nin işlem menüsünde para yatırma para çekme vardır
#Bakiye sorgulama vardır
import sys
from time import sleep
kartsifre=12345
bakiye=500
hak=3
hata=""
while True:
        sys.stdout.write("\033[2J\033[H")
        print("""
________________________________
|                              |
|    Bankamıza Hoş Geldiniz    |
|    #kart şifresi 12345       | 
|______________________________|
""")
        sifre=int(input("   Kartın Şifresini Giriniz:\n   :"))
        if kartsifre==sifre:
            while True:
                sys.stdout.write("\033[2J\033[H")
                print("***********************************")
                print("Hoşgeldiniz:\n Para Çekmek için       #1 \n Para Yatiırmak için    #2 \n Bakiye Sorgulamak için #3 \n Kart iade için         #0 \n Basınız")
                print("***********************************")
                islem=int(input("Lutfen isleminzi seciniz:"))
                print("***********************************")
                if islem==0:
                    
                    sys.stdout.write("\033[2J\033[H")
                    print("""
 _______________________________________________
|                                               |
|          KARTINIZ İADE EDİLİYOR               | 
| Bizi Tercih Etiğiniz için Teşekür Ederiz. :)  |
|_______________________________________________|
""")
                    sleep(2)
                    print("Ana Ekrana Dönülüyor....")
                    for x in range(10,100,10):
                        print("{}%.....Sistemden Çıkılıyor".format(x))
                        sleep(1)
                    
                    exit()
                elif islem==1:
                    sys.stdout.write('\033[2J\033[H')
                    sys.stdout.write("\033[1m")
                    print("""
________________________________________
|                                       |
| Çekeceğiniz Nakit Miktarınız Giriniz: |
|_______________________________________|
""")
                    paraCekme=int(input("           :"))
                    sys.stdout.write("\033[0m")                    
                    sys.stdout.flush()
                    if paraCekme>bakiye:
                        sys.stdout.write("\033[2J\033[H")
                        print("***********************************")
                        sys.stdout.write("\033[1m")
                        sys.stdout.write("\033[41m")
                        print("""
____________________________________________
|                                          |
|    Kartınızda Sadece {} TL Mevcutur     |
|__________________________________________|
""".format(bakiye))     
                        sys.stdout.write("\033[0m")
                        paracekmeislemhatasi=input("Ana Menu için herhangi bir yere basınız:")
                        sys.stdout.flush()
                    elif paraCekme<0:
                        sys.stdout.write("\033[2J\033[H")
                        sys.stdout.write("\033[1m")
                        sys.stdout.write("\033[41m")
                        print("""
________________________________
|                               |
| Girdiğiniz Değeri Çekemsiniz. |
|_______________________________|
""")                    
                        sys.stdout.write("\033[0m")
                        paracekmegirdihatasi=input("Ana Menu için herhangi bir yere basınız:")
                        continue
                    else:
                        bakiye-=paraCekme
                        continue
                elif islem==2:
                    sys.stdout.write("\033[2J\033[H")
                    print("""
________________________________________________
|                                               |
| Lütfen Yatıracağınız Nakit Miktarını Giriniz. |
|_______________________________________________|                                                 
""")
                    ParaYatirma=int(input("                 :"))
                    if ParaYatirma<0:
                        sys.stdout.write("\033[2J\033[H")
                        sys.stdout.write("\033[41m")
                        print("""
_________________________
|                       |
| HATALI TUTAR GİRDİSİ  |
|_______________________|
""")                    
                        sys.stdout.write("\033[0m")
                        parayatirmahatasi=input("Ana Menu için herhangi bir yere basınız:")
                        continue
                    else:
                        bakiye+=ParaYatirma
                        continue
                elif islem==3:
                    sys.stdout.write('\033[2J\033[H')
                    print("""
  __________________________________
  |                                |
  |     Mevcut Bakiyeniz {} TL     |
  |________________________________|
                          """.format(bakiye))
                    bakiyeislem=input("Ana Menu için herhangi bir yere basınız")
                    sys.stdout.flush()
                    continue
                else:
                    sys.stdout.write("\033[2J\033[H")
                    sys.stdout.write("\033[41m")
                    sys.stdout.write("\033[1m")
                    print("""
__________________________
|                        |
|    HATALI TUŞLAMA      |
|________________________|
                          """)
                    sys.stdout.write("\033[0m")
                    hataislem=input("Ana Menu için herhangi bir yere basınız:")
                    sys.stdout.flush()
                    continue
        elif hak==0:
            sys.stdout.write('\033[2J\033[H')
            sys.stdout.write("\033[41m")
            sys.stdout.write("\033[1m")    
            print("""
___________UYARI_____________
|                           |
| Bu kart bloke edilmistir. |
|          :(               |
|___________________________|""")         
            sys.stdout.write("\033[0m")
            sys.stdout.flush()
            kart=0
            break
        else:
            sys.stdout.write("\033[2J\033[H")
            sys.stdout.write("\033[41m")
            sys.stdout.write("\033[1m")
            print("""
_____________________UYARI________________________
|              Şifreniz yanlış.                  |
| Tekrar girmek için herhangi bir tuşa basınız.  |
|            Kart İade için "0" Basınız.         |
|________________________________________________|
""")
            sys.stdout.write("\033[0m")
            sys.stdout.flush()
            hata=input(":")
        if hata!="0":
            sys.stdout.write("\033[2J\033[H")
            sys.stdout.write("\033[41m")
            print("""
________________________________________________________ 
|                                                       |
|             Kalan Deneme Hakınız {}                    |
| Deneme Hakınız Bitik'den Sonra Kartınız Bloke Edilir  |
|_______________________________________________________|
""".format(hak))
            sys.stdout.write("\033[0m")
            denemhaki=input("       Devam Etmek için herhangi bir yere basınız:")
            hak-=1
            continue
        elif hata=="0":
            sys.stdout.write("\033[2J\033[H")
            print("""
 _______________________________________________
|                                               | 
| Bizi Tercih Etiğiniz için Teşekür Ederiz. :)  |
|_______________________________________________|
                  """)
            sleep(2)
            print("Ana Ekrana Dönülüyor....")
            for x in range(10,100,10):
                print("{}%.....Yükleniyor".format(x))
                sleep(1)
        else:
            print("Hata yanlis islem secildi")
            continue
