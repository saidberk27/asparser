# C.SAID BERK TARAFINDAN ASPAR ENERJI ICIN GELISTIRILMISTIR.
# DEVELOPED BY C.SAID BERK FOR ASPAR ENERGY INC.

# https://www.geeksforgeeks.org/how-to-add-text-on-an-image-using-pillow-in-python/
# https://note.nkmk.me/en/python-pillow-paste/#:~:text=Call%20the%20paste()%20method,left)%20of%20the%20base%20image.

# TO -DO ters_son2 ters_son ve temel fonksiyonları icin eger klasor yoksa try-excepti yok ,yaz .TEMP Dosyalar uzerine calis.Calisitrmadan lasorleri acmayi unutma.
# TO-DO DORTLUYAP FONKSIYONU S TYPE ELDIVENLER ICIN CALISMIYOR,AYARLA.S TYPE DOSYA ADI YAZIMINI DEGISTIR.
from datetime import datetime
import qrcode as qrcode
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os
import shutil

class Functions:
# klasorleri bosaltmak icin superior fonksiyon

    def __init__(self, ulkekodu=None, partiNo=None, classNo=None, sizeNo=None, lotNo=None, partidekiEldivenSayisi=None, aciklama=None,  isStandart=None, isSample=False, isBoxTest=False, isDoubleColor=False, verticalSpace=None):
        self.ulkeKodu = ulkekodu
        self.partiNo = partiNo
        self.classNo = classNo
        self.sizeNo = sizeNo
        self.lotNo = lotNo
        self.partidekiEldivenSayisi = partidekiEldivenSayisi
        self.aciklama = aciklama
        self.isStandart = isStandart
        self.isSample = isSample
        self.isBoxTest = isBoxTest
        self.isDoubleColor = isDoubleColor
        self.verticalSpace = verticalSpace
    def klasorTemizle(self, klasor_path):
        shutil.rmtree('{}'.format(klasor_path))

    def klasorYoksaAc(self, klasor_path):
        isExist = os.path.exists(klasor_path)

        if (isExist):
            print("Klasor Mevcut")

        else:
            os.system("mkdir {}".format(klasor_path))


    # seri no kayit icin superior fonksiyon
    def seriNoKayıt(self):
        fr = open("seri_numaralari.txt", "r")
        if (len(fr.read()) != 0):  # EGER DOSYA BOS DEGILSE
            simdi = datetime.now().strftime("%d_%m_%Y__%H%M%S")  # SUANIN TARIHI VE SANIYESI ILE ESKI KLASORE AT
            print(simdi)

            qrPaperPath = os.path.abspath(os.getcwd()) + '/qrpapers'

            self.klasorYoksaAc('old_serial_numbers')
            self.klasorYoksaAc('qrpapers')

            os.system("copy seri_numaralari.txt /old_serial_numbers")
            os.system("rename old_serial_numbers\seri_numaralari.txt {}.txt".format(simdi))

            os.system("mkdir old_serial_numbers")
            os.system("copy seri_numaralari.txt old_serial_numbers")
            os.system("rename old_serial_numbers\seri_numaralari.txt {}.txt".format(simdi))


    def seriNoOlustur(self):
        self.seriNoKayıt()

        seriEndemik = 1  # SON 3 HANE ICIN OLUSTURULDU
        partiNoUygun = str(self.partiNo).zfill(3)  # AY DATASI CEKILDI

        sinifUygun = "C" + str(self.classNo)

        sizeUygun = "S" + self.sizeNo.zfill(2)

        f = open("seri_numaralari.txt", "w")
        for i in range(self.partidekiEldivenSayisi):
            seriNoFinal = self.ulkeKodu + partiNoUygun + sinifUygun + sizeUygun + str(seriEndemik).zfill(3) + self.isStandart  # SERI NO DIZILIMI
            print(seriNoFinal)
            f.write(seriNoFinal + "\n")  # FILE'A BAS.
            seriEndemik = seriEndemik + 1  # SON 3 HANEYI DEGISTIR.


    def qrCodeOlustur(self, testkv=None):
        qrPath = os.path.abspath(os.getcwd()) + '\qrcodes'  # QR CODES KLASORUNE EVRENSEL ERISIM

        f = open("seri_numaralari.txt", "r")
        seriNoListe = f.readlines()  # SERI NO LISTESI CEKILDI

        uretimTarih = datetime.now().strftime("%d/%m/%Y")

        if (self.isSample):
            qrMetinTemel = 'This Product is Sample.{} Safeline ASP-EI{} {} {} {} {} www.asparenerji.com'
        else:
            qrMetinTemel = '{} Safeline ASP-EI{} {} {} {} {} www.asparenerji.com'

        if (self.isStandart == 's' or self.isStandart == 'S'):  # Eldiven (standart/arc) belirlenmesi
            eldivenType = ''
        elif (self.isStandart == 'a' or self.isStandart == 'A'):
            eldivenType = 'A'

        if (self.classNo == "00"):
            testkv = "2.5kV"  # TEST KV SADECE QR CODDA

        elif (self.classNo == "0"):
            testkv = "5kV"

        elif (self.classNo == "1"):
            testkv = "10kV"

        elif (self.classNo == "4"):
            testkv = "40kV"

        try:
            self.klasorTemizle(qrPath)
        except FileNotFoundError:
            print("dosya zaten yok")

        for i in seriNoListe:
            print(i)
            qr = qrcode.QRCode(version=1, box_size=7, border=1)
            qrmetinson = qrMetinTemel.format(self.aciklama, eldivenType, self.classNo, i, uretimTarih, testkv)
            qr.add_data(qrmetinson)
            qr.make(fit=True)
            try:
                img = qr.make_image(fill='black', back_color='white')
                img = img.resize((375, 273))  # Gergin basım oldupu için eni boyundan biraz fazla olmalı
                img.save("{}/{}.png".format(qrPath, i[
                                                    -5:-1]))  # QRCODE jpg'YE BASILDI.NUMERIK ISIM VERILDI.# -5 KISMI COK ONEMLI.yoksa liste basa donup override ediyor.
            except FileNotFoundError:
                self.klasorYoksaAc('qrcodes')
                img = qr.make_image(fill='black', back_color='white')  # dosya yoksa qrcodes dosyası aciyor.
                img = img.resize((375, 273))  # Gergin basım oldupu için eni boyundan biraz fazla olmalı
                img.save("{}/{}.png".format(qrPath, i[
                                                    -5:-1]))  # INDEX KAYMASI OLMAMASI ICIN (ILK ADIMI ATLAMAMASI ICIN, BURAYA DA EKLEME KODU EKLIYORUZ.)


    def qrCodeEkle(self):
        if (self.isStandart == "s" or self.isStandart == "S"):
            temelTaslak = Image.open('etiket-standart.jpg')  # TEMEL TASLAK ACILDI

        elif (self.isStandart == "a" or self.isStandart == "A"):
            temelTaslak = Image.open('etiket-arc.jpg')  # TEMEL TASLAK ACILDI

        qrCodePath = os.path.abspath(os.getcwd()) + '/qrcodes'
        qrCodePathContents = os.listdir(qrCodePath)

        qrPaperPath = os.path.abspath(os.getcwd()) + '/qrpapers'  # QR PAPER = QR CODE EKLENMIS TASLAK

        try:
            self.klasorTemizle(qrPaperPath)
        except FileNotFoundError:
            print("dosya zaten yok")
        # MUTLAKA OKU -- KLASOR TEMIZLE FONKSIYONU KLASORU TEMIZLIYOR,ASAGIDAKI KOD (FOR ICINDEKI TRY -EXCEPT) AYNI ISIMDE AYNI KLASORU ( BOS SEKILDE ELBETTE) TEKRAR OLUSTURUYOR.KLASOR TEMIZLENDI BIRAZ ILUZYON AMA CALISIYOR.

        for imgIndex in qrCodePathContents:  # QR CODE'LAR ICINDE FOR ACILDI
            print(imgIndex)
            qrCode = Image.open('{}'.format(qrCodePath + "/{}".format(imgIndex)))  # QR CODE'LARA ERISIM
            temelTaslak.paste(qrCode, (630, 200))  # BIRLESIM

            try:
                temelTaslak.save('{}'.format(qrPaperPath) + '/P{}'.format(imgIndex),
                                 quality=4000)  # KAYIT,BURASI IKI KERE CALISIRSA .PNG.JPG BIRLESIK UZANTI OLUSUYOR.
            except FileNotFoundError:
                os.system("mkdir qrpapers")
                temelTaslak.save('{}'.format(qrPaperPath) + '/P{}'.format(imgIndex),
                                 quality=4000)  # INDEX KAYMASI OLMAMASI ICIN (ILK ADIMI ATLAMAMASI ICIN, BURAYA DA EKLEME KODU EKLIYORUZ.)


    def yaziResimBirlesme(self):
        qrPaperPath = os.path.abspath(os.getcwd()) + '/qrpapers'
        qrPaperPathContents = os.listdir(qrPaperPath)  # QR PAPER PATH ERISIM

        sonPath = os.path.abspath(os.getcwd()) + '/son'  # ISLEM BITINCE BASILACAK PATH
        seriNoDosya = open("seri_numaralari.txt", "r")
        seriNoListe = seriNoDosya.readlines()

        yil = datetime.today().strftime('%Y')
        yilUygun = yil[2:4]  # YIL DATASI

        ayUygun = datetime.today().strftime('%m')  # AY DATASI

        mainFont = ImageFont.truetype('ariblk.ttf', 34)
        arcDetayFont = ImageFont.truetype('HUBlackout Black.ttf', 34)
        maxUseVoltageFont = ImageFont.truetype('ariblk.ttf', 30)
        testFont = ImageFont.truetype('ariblk.ttf', 36)

        def standartYaziEkle():
            eldivenTurUygun = 'ASP-Eİ'

            self.klasorYoksaAc('son')
            self.klasorTemizle(sonPath)

            i = 0
            for paperContent in qrPaperPathContents:
                print(paperContent)
                print(seriNoListe[i])
                img = Image.open('qrpapers/{}'.format(paperContent))  # HAZIRLANMIS QR PAPERLARA ERISIM

                eldivenTurEtiket = ImageDraw.Draw(img)
                eldivenTurEtiket.text((50, 150), "{}".format(eldivenTurUygun), font=mainFont, fill=(0, 0, 0))

                sinifEtiket = ImageDraw.Draw(img)  # USTUNE YAZACAGIMIZ ICIN DRAW FONKSIYONU
                sinifEtiket.text((545, 281), "{}".format(self.classNo), font=mainFont,
                                 fill=(0, 0, 0))  # POZISYON,FONT VE RENK AYARLAMALARI

                tarihEtiket = ImageDraw.Draw(img)
                tarihEtiket.text((432, 373), "{}/{}".format(ayUygun, yilUygun), font=mainFont,
                                 fill=(0, 0, 0))  # USTTEN BOSLUK-SOLDAN BOSLUK

                lotNoEtiket = ImageDraw.Draw(img)
                lotNoEtiket.text((625, 558), "{}".format(self.lotNo), font=mainFont, fill=(0, 0, 0))

                sizeEtiket = ImageDraw.Draw(img)
                sizeEtiket.text((700, 614), "{}".format(self.sizeNo), font=mainFont, fill=(0, 0, 0))  # SOLBOSLUK,USTBOSLUK

                testedEtiket = ImageDraw.Draw(img)
                testedEtiket.text((600, 650), "{}".format("TESTED"), font=testFont, fill=(255, 0, 0))

                testinfoEtiket = ImageDraw.Draw(img)
                testinfoEtiket.text((520, 700), "{}".format(testInfo), font=testFont, fill=(255, 0, 0))

                maxUseVoltageEtiket = ImageDraw.Draw(img)
                maxUseVoltageEtiket.text((280, 845), "{}".format(maxUseVoltage), font=maxUseVoltageFont, fill=(0, 0, 0))

                imgson = img.convert('RGB')

                try:
                    imgson.save('{}'.format(sonPath) + '/SON{}.jpg'.format(paperContent[:-5]))

                except FileNotFoundError:
                    os.system(
                        "mkdir son")  # INDEX KAYMASI OLMAMASI ICIN (ILK ADIMI ATLAMAMASI ICIN, BURAYA DA EKLEME KODU EKLIYORUZ.)
                    imgson.save('{}'.format(sonPath) + '/SON{}.jpg'.format(paperContent[:-5]))
                i = i + 1

        def arcYaziEkle():
            self.klasorYoksaAc('son')
            self.klasorTemizle(sonPath)

            i = 0
            for paperContent in qrPaperPathContents:
                if (self.classNo == "4"):
                    eldivenTurUygun = '         ASP-EİA-C4\narc flash protection'
                    calVeri = '111'  # ASTM F2675:APTV 111 cal cm^3
                else:
                    eldivenTurUygun = '         ASP-EİA-C0\narc flash protection'
                    calVeri = '30'  # ASTM F2675:APTV 30 cal cm^3

                img = Image.open('qrpapers/{}'.format(paperContent))  # HAZIRLANMIS QR PAPERLARA ERISIM

                eldivenTurEtiket = ImageDraw.Draw(img)
                eldivenTurEtiket.text((615, 120), "{}".format(eldivenTurUygun), font=mainFont, fill=(0, 0, 0))

                sinifEtiket = ImageDraw.Draw(img)  # USTUNE YAZACAGIMIZ ICIN DRAW FONKSIYONU
                sinifEtiket.text((545, 281), "{}".format(self.classNo), font=mainFont,
                                 fill=(0, 0, 0))  # POZISYON,FONT VE RENK AYARLAMALARI

                tarihEtiket = ImageDraw.Draw(img)
                tarihEtiket.text((432, 373), "{}/{}".format(ayUygun, yilUygun), font=mainFont,
                                 fill=(0, 0, 0))  # USTTEN BOSLUK-SOLDAN BOSLUK

                lotNoEtiket = ImageDraw.Draw(img)
                lotNoEtiket.text((615, 496), "{}".format(self.lotNo), font=mainFont, fill=(0, 0, 0))  # SOLBOSLUK,USTBOSLUK

                sizeEtiket = ImageDraw.Draw(img)
                sizeEtiket.text((705, 537), "{}".format(self.sizeNo), font=mainFont, fill=(0, 0, 0))  # SOLBOSLUK,USTBOSLUK

                testedEtiket = ImageDraw.Draw(img)
                testedEtiket.text((600, 590), "{}".format("TESTED"), font=testFont, fill=(255, 0, 0))  # SOLBOSLUK,USTBOSLUK

                testinfoEtiket = ImageDraw.Draw(img)
                testinfoEtiket.text((520, 640), "{}".format(testInfo), font=testFont,
                                    fill=(255, 0, 0))  # SOLBOSLUK,USTBOSLUK

                if (self.isBoxTest):  # box test checkbox'u işaretlendiyse burası true oluyor.
                    arcDetay = "  IEC 61482-1-2 : 2014 Class 2 Box Test 7 kA\n\t\t\t\t\t\t\t\tASTM F2675:APTV {} cal/cm²".format(
                        calVeri)
                    arcDetayEtiket = ImageDraw.Draw(img)
                    arcDetayEtiket.text((90, 810), "{}".format(arcDetay), font=arcDetayFont,
                                        fill=(0, 0, 0))  # SOLBOSLUK,USTBOSLUK

                else:
                    arcDetay = "  IEC 61482-1-2:APC CLASS 2\nASTM F2675:APTV {} cal/cm²".format(calVeri)
                    arcDetayEtiket = ImageDraw.Draw(img)
                    arcDetayEtiket.text((220, 810), "{}".format(arcDetay), font=arcDetayFont,
                                        fill=(0, 0, 0))

                maxUseVoltageEtiket = ImageDraw.Draw(img)
                maxUseVoltageEtiket.text((450, 685), "{}".format(maxUseVoltage), font=maxUseVoltageFont,
                                         fill=(0, 0, 0))  # SOLBOSLUK,USTBOSLUK

                imgson = img.convert('RGB')

                try:
                    imgson.save('{}'.format(sonPath) + '/SON{}.jpg'.format(paperContent[:-5]))

                except FileNotFoundError:
                    os.system(
                        "mkdir son")  # INDEX KAYMASI OLMAMASI ICIN (ILK ADIMI ATLAMAMASI ICIN, BURAYA DA EKLEME KODU EKLIYORUZ.)
                    imgson.save('{}'.format(sonPath) + '/SON{}.jpg'.format(paperContent[:-5]))
                i = i + 1

        # -----------------------------------------------------------------------------
        if (self.classNo == "00"):  # self.classNo = sinifInput
            maxUseVoltage = "Max. Use Voltage 500 V AC"  # MAX USE VOLTAGE SADECE ETIKETTE
            testInfo = "2.5 kV AC/60 sec"

        elif (self.classNo == "0"):
            maxUseVoltage = "Max. Use Voltage 1000 V AC"
            testInfo = "5 kV AC/60 sec"

        elif (self.classNo == "1"):
            maxUseVoltage = "Max. Use Voltage 7500 V AC"
            testInfo = "10 kV AC/60 sec"

        elif (self.classNo == "4"):
            maxUseVoltage = "Max. Use Voltage 36000 V AC"
            testInfo = "40 kV AC/60 sec"

        if (self.isStandart == "s" or self.isStandart == "S"):
            standartYaziEkle()
        if (self.isStandart == "a" or self.isStandart == "A"):
            arcYaziEkle()


    def sampleMod(self):
        samplePath = os.path.abspath(os.getcwd()) + '/sample'
        self.klasorYoksaAc('sample')
        self.klasorTemizle(samplePath)

        sampleFont = ImageFont.truetype('ariblk.ttf', 200)

        sonEtiketPath = os.path.abspath(os.getcwd()) + '/son'
        sonEtiketFolderContents = os.listdir(sonEtiketPath)
        i = 0

        for sonEtiketHam in sonEtiketFolderContents:
            with Image.open('son/{}'.format(sonEtiketHam)).convert("RGBA") as base:
                txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
                d = ImageDraw.Draw(txt)

                d.text((70, 450), "SAMPLE", font=sampleFont, fill=(255, 0, 0, 150))
                # draw text, full opacity

                sampleLabel = Image.alpha_composite(base, txt)
            try:
                sampleLabel.save('{}'.format(samplePath) + '/sample{}.png'.format(i))

            except FileNotFoundError:
                os.system(
                    "mkdir sample")  # INDEX KAYMASI OLMAMASI ICIN (ILK ADIMI ATLAMAMASI ICIN, BURAYA DA EKLEME KODU EKLIYORUZ.)
                sampleLabel.save('{}'.format(samplePath) + '/sample{}.png'.format(i))

            i = i + 1


    def doubleColorMod(self):
        doubleColorPath = os.path.abspath(os.getcwd()) + '/double_color'
        self.klasorTemizle(doubleColorPath)
        self.klasorYoksaAc('double_color')
        mainFont = ImageFont.truetype('ariblk.ttf', 34)
        sonEtiketPath = os.path.abspath(os.getcwd()) + '/son'

        sonEtiketFolderContents = os.listdir(sonEtiketPath)
        i = 1
        for sonEtiketHam in sonEtiketFolderContents:
            img = Image.open('son/{}'.format(sonEtiketHam))
            doubleColorEtiket = ImageDraw.Draw(img)
            doubleColorEtiket.text((660, 130), "{}".format("DOUBLE COLOR"), font=mainFont, fill=(0, 0, 0))
            img.save('{}'.format(doubleColorPath) + '/DOUBLECOLOR{}.jpg'.format(i))
            i = i + 1


    def ikiliYap(self):
        temelPath = os.path.abspath(os.getcwd()) + '/ikilison'
        tersPath = os.path.abspath(os.getcwd()) + '/ters_son'
        tersPath2 = os.path.abspath(os.getcwd()) + '/ters_son2'

        sonPath = os.path.abspath(os.getcwd()) + '/son'

        try:
            self.klasorTemizle(tersPath)
            self.klasorTemizle(tersPath2)
            self.klasorTemizle(temelPath)

            self.klasorYoksaAc('ters_son')
            self.klasorYoksaAc('ters_son2')
            self.klasorYoksaAc('ikilison')
        except:
            self.klasorYoksaAc('ters_son')
            self.klasorYoksaAc('ters_son2')
            self.klasorYoksaAc('ikilison')

        path, dirs, files = next(os.walk(sonPath))
        elemanSayisi = len(files)

        temel = Image.open('temelikili.jpg')

        if (self.isSample):
            try:
                for i in range(0, (
                        elemanSayisi + 1)):  # i = 0.belggeden baslayarak tum belgeleri tarayacak. FOR'UN ICI NE ANLATIYOR?INDEXLER IKISER IKISER ATLANIYOR.ELEMAN SAYISI +1 SON ELEMAN CIFT SAYIYSA ONUN DA ALINMASI ICIN.
                    # SON ELEMAN CIFT SAYIYSA INDEX OUT OF RANGE HATASI VERECEK DUZELT.
                    seriNoBelge = Image.open("sample/sample{}.png".format(i))
                    seriNoBelgeTers = seriNoBelge.rotate(180)
                    seriNoBelgeTers.save('ters_son/TERSSON{}.png'.format(i))

                    temel.paste(seriNoBelgeTers, (0, 0))
                    temel.paste(seriNoBelgeTers, (self.verticalSpace, 0))

                    temel.save('ikilison/SIZE{}_{}.png'.format(str(self.sizeNo), i))
            except FileNotFoundError:
                print("Cift Sayi Asimi")

        elif(self.isDoubleColor):
            print("Double Color")
            birdenBasla = 1
            try:
                for i in range(0, (elemanSayisi + 1)):  # i = 0.belggeden baslayarak tum belgeleri tarayacak. FOR'UN ICI NE ANLATIYOR?INDEXLER IKISER IKISER ATLANIYOR.ELEMAN SAYISI +1 SON ELEMAN CIFT SAYIYSA ONUN DA ALINMASI ICIN.
                    # SON ELEMAN CIFT SAYIYSA INDEX OUT OF RANGE HATASI VERECEK DUZELT.
                    seriNoBelge = Image.open("double_color/DOUBLECOLOR{}.jpg".format(birdenBasla))
                    seriNoBelgeTers = seriNoBelge.rotate(180)
                    seriNoBelgeTers.save('ters_son/TERSSON{}.png'.format(birdenBasla))

                    temel.paste(seriNoBelgeTers, (0, 0))
                    temel.paste(seriNoBelgeTers, (self.verticalSpace, 0))

                    temel.save('ikilison/SIZE{}_{}.png'.format(str(self.sizeNo), birdenBasla))
                    birdenBasla = birdenBasla + 1
            except FileNotFoundError:
                print("Cift Sayi Asimi")

        else:
            birdenBasla = 1
            try:
                for i in range(0, (elemanSayisi + 1)):  # i = 0.belggeden baslayarak tum belgeleri tarayacak. FOR'UN ICI NE ANLATIYOR?INDEXLER IKISER IKISER ATLANIYOR.ELEMAN SAYISI +1 SON ELEMAN CIFT SAYIYSA ONUN DA ALINMASI ICIN.
                    # SON ELEMAN CIFT SAYIYSA INDEX OUT OF RANGE HATASI VERECEK DUZELT.
                    seriNoBelge = Image.open("son/SONP{}.jpg".format(str(birdenBasla).zfill(3)))
                    seriNoBelgeTers = seriNoBelge.rotate(180)
                    seriNoBelgeTers.save('ters_son/TERSSON{}.jpg'.format(str(birdenBasla).zfill(3)))

                    temel.paste(seriNoBelgeTers, (0, 0))
                    temel.paste(seriNoBelgeTers, (self.verticalSpace, 0))

                    temel.save('ikilison/SIZE{}_{}.png'.format(str(self.sizeNo), birdenBasla))
                    birdenBasla = birdenBasla + 1
            except FileNotFoundError:
                print("Cift Sayi Asimi")
