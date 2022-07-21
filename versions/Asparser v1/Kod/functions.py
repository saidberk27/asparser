#C.SAID BERK TARAFINDAN ASPAR ENERJI ICIN GELISTIRILMISTIR.
#DEVELOPED BY C.SAID BERK FOR ASPAR ENERGY INC.

# https://www.geeksforgeeks.org/how-to-add-text-on-an-image-using-pillow-in-python/
#https://note.nkmk.me/en/python-pillow-paste/#:~:text=Call%20the%20paste()%20method,left)%20of%20the%20base%20image.

#TO -DO ters_son2 ters_son ve temel fonksiyonları icin eger klasor yoksa try-excepti yok ,yaz .TEMP Dosyalar uzerine calis.Calisitrmadan lasorleri acmayi unutma.
#TO-DO DORTLUYAP FONKSIYONU S TYPE ELDIVENLER ICIN CALISMIYOR,AYARLA.S TYPE DOSYA ADI YAZIMINI DEGISTIR.
from datetime import datetime
import qrcode as qrcode
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os
import png
import shutil

#klasorleri bosaltmak icin superior fonksiyon
def klasorTemizle(klasor_path):
    shutil.rmtree('{}'.format(klasor_path))

def klasorYoksaAc(klasor_path):
    isExist = os.path.exists(klasor_path)

    if (isExist):
        print("Klasor Mevcut")

    else:
        os.system("mkdir {}".format(klasor_path))

#seri no kayit icin superior fonksiyon
def seriNoKayıt():
    fr = open("seri_numaralari.txt", "r")
    if(len(fr.read()) != 0): #EGER DOSYA BOS DEGILSE
        simdi = datetime.now().strftime("%d_%m_%Y__%H%M%S") #SUANIN TARIHI VE SANIYESI ILE ESKI KLASORE AT
        print(simdi)

        qrPaperPath = os.path.abspath(os.getcwd()) + '/qrpapers'


        klasorYoksaAc('old_serial_numbers')
        klasorYoksaAc('qrpapers')

        os.system("copy seri_numaralari.txt /old_serial_numbers")
        os.system("rename old_serial_numbers\seri_numaralari.txt {}.txt".format(simdi))


        os.system("mkdir old_serial_numbers")
        os.system("copy seri_numaralari.txt old_serial_numbers")
        os.system("rename old_serial_numbers\seri_numaralari.txt {}.txt".format(simdi))

def seriNoOlustur(ulke,partiNo,sinif,partiEleman,sizeEleman,saEleman):
    seriNoKayıt()

    seriEndemik = 0 #SON 3 HANE ICIN OLUSTURULDU

    partiNoUygun = str(partiNo).zfill(3) #AY DATASI CEKILDI

    sinifUygun = "C" + str(sinif)

    sizeUygun = "S" + sizeEleman.zfill(2)

    f = open("seri_numaralari.txt", "w")
    for i in range(partiEleman):
        seriNoFinal = ulke + partiNoUygun + sinifUygun + sizeUygun + str(seriEndemik).zfill(3) + saEleman #SERI NO DIZILIMI
        print(seriNoFinal)
        f.write(seriNoFinal + "\n") #FILE'A BAS.
        seriEndemik = seriEndemik + 1# SON 3 HANEYI DEGISTIR.


def qrCodeOlustur(sinifInput,saEleman):

    qrPath = os.path.abspath(os.getcwd()) + '\qrcodes'  #QR CODES KLASORUNE EVRENSEL ERISIM

    f = open("seri_numaralari.txt","r")
    seriNoListe = f.readlines() # SERI NO LISTESI CEKILDI

    uretimTarih = datetime.now().strftime("%d/%m/%Y")
    qrMetinTemel = 'Safeline ASP-EI{} {} {} {} {} www.asparenerji .com'



    if(saEleman == 's' or saEleman == 'S'): #Eldiven (standart/arc) belirlenmesi
        eldivenType = ''
    elif(saEleman == 'a' or saEleman == 'A'):
        eldivenType = 'A'


    if(sinifInput == "00"):
        testkv = "2.5kV" #TEST KV SADECE QR CODDA
        maxUseVoltage = "500V" #MAX USE VOLTAGE SADECE ETIKETTE

    elif(sinifInput == "0"):
        testkv = "5kV"
        maxUseVoltage = "1000V"

    elif(sinifInput == "4"):
        testkv = "40kV"
        maxUseVoltage = "36.000V"

    try:
        klasorTemizle(qrPath)
    except FileNotFoundError:
        print("dosya zaten yok")


    for i in seriNoListe:
        print(i)
        qr = qrcode.QRCode(version=1, box_size=7, border=1)
        qrmetinson = qrMetinTemel.format(eldivenType,sinifInput,i,uretimTarih,testkv)
        qr.add_data(qrmetinson)
        qr.make(fit=True)
        try:
            img = qr.make_image(fill='black', back_color='white')
            img = img.resize((375,273)) #Gergin basım oldupu için eni boyundan biraz fazla olmalı
            img.save("{}/{}.png".format(qrPath,i[-5:-1])) #QRCODE jpg'YE BASILDI.NUMERIK ISIM VERILDI.# -5 KISMI COK ONEMLI.yoksa liste basa donup override ediyor.
        except FileNotFoundError:
            klasorYoksaAc('qrcodes')
            img = qr.make_image(fill='black', back_color='white')#dosya yoksa qrcodes dosyası aciyor.
            img = img.resize((375, 273))#Gergin basım oldupu için eni boyundan biraz fazla olmalı
            img.save("{}/{}.png".format(qrPath, i[-5:-1]))#INDEX KAYMASI OLMAMASI ICIN (ILK ADIMI ATLAMAMASI ICIN, BURAYA DA EKLEME KODU EKLIYORUZ.)



def qrCodeEkle():
    temelTaslak = Image.open('etiketyeni.jpg')#TEMEL TASLAK ACILDI
    qrCodePath = os.path.abspath(os.getcwd()) + '/qrcodes'
    qrCodePathContents = os.listdir(qrCodePath)

    qrPaperPath = os.path.abspath(os.getcwd()) + '/qrpapers'#QR PAPER = QR CODE EKLENMIS TASLAK


    try:
        klasorTemizle(qrPaperPath)
    except FileNotFoundError:
        print("dosya zaten yok")
#MUTLAKA OKU -- KLASOR TEMIZLE FONKSIYONU KLASORU TEMIZLIYOR,ASAGIDAKI KOD (FOR ICINDEKI TRY -EXCEPT) AYNI ISIMDE AYNI KLASORU ( BOS SEKILDE ELBETTE) TEKRAR OLUSTURUYOR.KLASOR TEMIZLENDI BIRAZ ILUZYON AMA CALISIYOR.

    for imgIndex in qrCodePathContents: #QR CODE'LAR ICINDE FOR ACILDI
        print(imgIndex)
        qrCode = Image.open('{}'.format(qrCodePath + "/{}".format(imgIndex))) #QR CODE'LARA ERISIM
        temelTaslak.paste(qrCode, (630, 200)) #BIRLESIM

        try:
            temelTaslak.save('{}'.format(qrPaperPath) +'/P{}'.format(imgIndex), quality=4000) # KAYIT,BURASI IKI KERE CALISIRSA .PNG.JPG BIRLESIK UZANTI OLUSUYOR.
        except FileNotFoundError:
            os.system("mkdir qrpapers")
            temelTaslak.save('{}'.format(qrPaperPath) + '/P{}'.format(imgIndex), quality=4000) #INDEX KAYMASI OLMAMASI ICIN (ILK ADIMI ATLAMAMASI ICIN, BURAYA DA EKLEME KODU EKLIYORUZ.)


def yaziResimBirlesme(classType,size,lotNo,saEleman):
    qrPaperPath = os.path.abspath(os.getcwd()) + '/qrpapers'
    qrPaperPathContents = os.listdir(qrPaperPath) #QR PAPER PATH ERISIM

    sonPath = os.path.abspath(os.getcwd()) + '/son'#ISLEM BITINCE BASILACAK PATH
    seriNoDosya = open("seri_numaralari.txt","r")
    seriNoListe = seriNoDosya.readlines()

    yil = datetime.today().strftime('%Y')
    yilUygun = yil[2:4] #YIL DATASI

    ayUygun = datetime.today().strftime('%m') #AY DATASI

    mainFont = ImageFont.truetype('ariblk.ttf', 34)
    maxUseVoltageFont = ImageFont.truetype('ariblk.ttf', 30)
    testFont = ImageFont.truetype('ariblk.ttf', 36)

    if (saEleman == 's' or saEleman == 'S'):  # Eldiven (standart/arc) belirlenmesi
        eldivenTurUygun = 'ASP-Eİ'
    elif (saEleman == 'a' or saEleman == 'A'):
        eldivenTurUygun = 'ASP-EİA'
#-----------------------------------------------------------------------------
    if (classType == "00"): #classType = sinifInput
        maxUseVoltage = "Max. Use Voltage 500V AC"  # MAX USE VOLTAGE SADECE ETIKETTE
        testInfo = "2.5 kV AC/60 sec"

    elif (classType == "0"):
        maxUseVoltage = "Max. Use Voltage 1000V AC"
        testInfo = "5 kV AC/60 sec"

    elif (classType == "4"):
        maxUseVoltage = "Max. Use Voltage 36000V AC"
        testInfo = "40 kV AC/60 sec"

    klasorYoksaAc('son')
    klasorTemizle(sonPath)

    i = 0
    for paperContent in qrPaperPathContents:
        print(paperContent)
        print(seriNoListe[i])
        img = Image.open('qrpapers/{}'.format(paperContent)) #HAZIRLANMIS QR PAPERLARA ERISIM

        eldivenTurEtiket = ImageDraw.Draw(img)
        eldivenTurEtiket.text((50, 150), "{}".format(eldivenTurUygun), font=mainFont, fill=(0, 0, 0))

        sinifEtiket = ImageDraw.Draw(img) #USTUNE YAZACAGIMIZ ICIN DRAW FONKSIYONU
        sinifEtiket.text((588, 281), "{}".format(classType), font=mainFont, fill=(0, 0, 0))#POZISYON,FONT VE RENK AYARLAMALARI

        tarihEtiket = ImageDraw.Draw(img)
        tarihEtiket.text((480, 373), "{}/{}".format(ayUygun,yilUygun), font=mainFont, fill=(0, 0, 0))#USTTEN BOSLUK-SOLDAN BOSLUK

        lotNoEtiket = ImageDraw.Draw(img)
        lotNoEtiket.text((625, 558), "{}".format(lotNo), font=mainFont, fill=(0, 0, 0))

        sizeEtiket = ImageDraw.Draw(img)
        sizeEtiket.text((700, 614), "{}".format(size), font=mainFont, fill=(0, 0, 0)) #SOLBOSLUK,USTBOSLUK

        maxUseVoltageEtiket = ImageDraw.Draw(img)
        maxUseVoltageEtiket.text((280, 845), "{}".format(maxUseVoltage), font=maxUseVoltageFont, fill=(0, 0, 0))

        testedEtiket = ImageDraw.Draw(img)
        testedEtiket.text((600, 670), "{}".format("TESTED"), font=testFont, fill=(255, 0, 0))

        testinfoEtiket = ImageDraw.Draw(img)
        testinfoEtiket.text((520, 720), "{}".format(testInfo), font=testFont, fill=(255, 0, 0))

        imgson = img.convert('RGB')

        try:
            imgson.save('{}'.format(sonPath) +'/SON{}.jpg'.format(paperContent[:-5]))

        except FileNotFoundError:
            os.system("mkdir son") #INDEX KAYMASI OLMAMASI ICIN (ILK ADIMI ATLAMAMASI ICIN, BURAYA DA EKLEME KODU EKLIYORUZ.)
            imgson.save('{}'.format(sonPath) + '/SON{}.jpg'.format(paperContent[:-5]))
        i = i + 1

def ikiliYap(yatayBosluk):
    temelPath = os.path.abspath(os.getcwd()) + '/ikilison'
    tersPath = os.path.abspath(os.getcwd()) + '/ters_son'
    tersPath2 = os.path.abspath(os.getcwd()) + '/ters_son2'
    sonPath = os.path.abspath(os.getcwd()) + '/son'


    try:
        klasorTemizle(tersPath)
        klasorTemizle(tersPath2)
        klasorTemizle(temelPath)

        klasorYoksaAc('ters_son')
        klasorYoksaAc('ters_son2')
        klasorYoksaAc('ikilison')
    except:
        klasorYoksaAc('ters_son')
        klasorYoksaAc('ters_son2')
        klasorYoksaAc('ikilison')

    path, dirs, files = next(os.walk(sonPath))
    elemanSayisi = len(files)


    temel = Image.open('temelikili.jpg')

    try:
        for i in range(0, (elemanSayisi + 1)): #i = 0.belggeden baslayarak tum belgeleri tarayacak. FOR'UN ICI NE ANLATIYOR?INDEXLER IKISER IKISER ATLANIYOR.ELEMAN SAYISI +1 SON ELEMAN CIFT SAYIYSA ONUN DA ALINMASI ICIN.
    #SON ELEMAN CIFT SAYIYSA INDEX OUT OF RANGE HATASI VERECEK DUZELT.
            seriNoBelge = Image.open("son/SONP{}.jpg".format(str(i).zfill(3)))
            seriNoBelgeTers = seriNoBelge.rotate(180)
            seriNoBelgeTers.save('ters_son/TERSSON{}.jpg'.format(str(i).zfill(3)))

            temel.paste(seriNoBelgeTers,(0,0))
            temel.paste(seriNoBelgeTers,(yatayBosluk,0))

            temel.save('ikilison/ikilison{}.png'.format(i))
    except FileNotFoundError:
        print("Cift Sayi Asimi")


def dortluYap(dikeyBosluk,yatayBosluk):
    tersPath = os.path.abspath(os.getcwd()) + '/ters_son'
    tersPath2 = os.path.abspath(os.getcwd()) + '/ters_son2'
    dortPath = os.path.abspath(os.getcwd()) + '/dortluson'
    sonPath = os.path.abspath(os.getcwd()) + '/son'

    try:
        klasorTemizle(tersPath)
        klasorTemizle(tersPath2)
        klasorTemizle(temelPath)

        klasorYoksaAc('ters_son')
        klasorYoksaAc('ters_son2')
        klasorYoksaAc('dortluson')
    except:
        klasorYoksaAc('ters_son')
        klasorYoksaAc('ters_son2')
        klasorYoksaAc('dortluson')

    path, dirs, files = next(os.walk(sonPath))
    elemanSayisi = len(files)


    temel = Image.open('temeldortlu.jpg')

    try:
        for i in range(0, (elemanSayisi + 1), 2): #i = 0.belggeden baslayarak tum belgeleri tarayacak. FOR'UN ICI NE ANLATIYOR?INDEXLER IKISER IKISER ATLANIYOR.ELEMAN SAYISI +1 SON ELEMAN CIFT SAYIYSA ONUN DA ALINMASI ICIN.
    #SON ELEMAN CIFT SAYIYSA INDEX OUT OF RANGE HATASI VERECEK DUZELT.
            seriNoBelge = Image.open("son/SONP{}.jpg".format(str(i).zfill(3)))
            seriNoBelgeTers = seriNoBelge.rotate(180)
            seriNoBelgeTers.save('ters_son/TERSSON{}.jpg'.format(str(i).zfill(3)))

            sonrakiBelgeIndex = i + 1

            seriNoBelge2 = Image.open("son/SONP{}.jpg".format(str(sonrakiBelgeIndex).zfill(3)))
            seriNoBelgeTers2 = seriNoBelge2.rotate(180)
            seriNoBelgeTers2.save('ters_son2/TERSSON{}.jpg'.format(str(sonrakiBelgeIndex).zfill(3)))

            temel.paste(seriNoBelge,(0,dikeyBosluk))
            temel.paste(seriNoBelgeTers,(0,0))

            temel.paste(seriNoBelge2,(yatayBosluk,dikeyBosluk))
            temel.paste(seriNoBelgeTers2,(yatayBosluk,0))

            temel.save('dortluson/dortluson{}.jpg'.format(i))
    except FileNotFoundError:
        print("Cift Sayi Asimi")

