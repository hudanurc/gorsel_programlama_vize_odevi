#input ile değer alıyoruz komut değişkenine aktarıyoruz
komut = input("Değer giriniz : ")

#komut değerini parçalayıp dizi formatına çeviriyoruz
komutlar = komut.split("\\n")

#bu fonksiyonda girilen değere göre cihaza çeviriyoruz
def cihaz(deger):
    deger = int(deger)
    if deger == 1:
        return "Televizyon"
    elif deger == 2:
        return "Çamaşır makinesi"
    elif deger == 3:
        return "buzdolabı"
    elif deger == 4:
        return "Fırın"
    else :
        return "Geçersiz"

#fonksiyona parametre gönderiyoruz paremetre sonucunda cihaz durumunu hakkında bilgi alıyoruz
def durum(deger):
    deger = int(deger)
    if deger == 0:
        return "Off"
    elif deger == 1:
        return "On"
    else:
        return "Geçersiz"

#girilen değer sonucunda sinyal bilgisini alıyoruz
def sinyal(deger):
    deger = int(deger)
    if deger >= 0 and deger <= 50:
        return "Çok zayıf sinyal"
    elif deger >= 51 and deger <= 100:
        return "Zayıf sinyal"
    elif deger >= 101 and deger <= 150:
        return "Orta Sinyal"
    elif deger >= 151 and deger <= 200:
        return "Güçlü Sinyal"
    elif deger >= 201 and deger <= 205:
        return "Çok güçlü sinyal"

#verilen değer sonucunda cihazın bilgi isteyip istemediğini hesaplıyoruz
def cevap(deger):
    deger = int(deger)
    if deger == 0:
        return "Cevap istenmiyor"
    elif deger == 1:
        return "Cevap isteniyor"
    else:
        return "Geçersiz"

#parçalanan komutları for ile tarıyoruz
for kod in range(len(komutlar)-1):

    #gelen komuttaki parametreleri parçalıyoruz
    parametre = komutlar[kod].split('-')

    #eğer birinci paremetre send ise
    if parametre[0] == "send":
        #eğer parametre sayısı 5 ise
        if len(parametre) == 5:
            #eğer sinyal değeri geçersiz ise
            if sinyal(parametre[1]) == "Geçersiz":
                #hata versin
                print("ikinci bolum hatali")
                #cihaz bilgisi geçersiz ise
            elif cihaz(parametre[2]) == "Geçersiz":
                #hata versin
                print("ucuncu bolum hatali")
                #cihaz durum bilgisi gerçersiz ise
            elif durum(parametre[3]) == "Geçersiz":
                #hata versin
                print("dorduncu bolum hatali")
                #cihaz cevap bilgisi geçersiz ise
            elif cevap(parametre[4]) == "Geçersiz":
                #hata versin
                print("besinci bolum hatali")
            #eğer hata yok ise
            else:
                #tüm değerleri yazsın
                print("Kod Tipi : send - Giden")
                print("Sinyal Gucu : " + parametre[1] +" - "+ sinyal(parametre[1]))
                print("Cihaz : " + parametre[2] + " - " + cihaz(parametre[2]))
                print("Durumu : " + parametre[3] + " - " + durum(parametre[3]))
                print("Cevap : " + parametre[4] + " - " + cevap(parametre[4]))
        #eğer parametre 5 değil ise
        else:
            print("ikinci bölüm hatalı")

    #eğer birinci parametre değeri receive ise
    elif parametre[0] == "receive":
        #eğer parametre sayısı 4 ise
        if len(parametre) == 4:
            #eğer sinyal değeri geçersiz ise
            if sinyal(parametre[1]) == "Geçersiz":
                #hata versin
                print("ikinci bolum hatali")
            #eğer cihaz durumu geçersiz ise
            elif cihaz(parametre[2]) == "Geçersiz":
                #hata versin
                print("ucuncu bolum hatali")
            #eğer durum değeri gerçersiz ise
            elif durum(parametre[3]) == "Geçersiz":
                #hata versin
                print("dorduncu bolum hatali")
            #eğer hata yok ise
            else:
                #tüm değerleri yazsın
                print("Kod Tipi : receive - Gelen")
                print("Sinyal Gucu : " + parametre[1] + " - " + sinyal(parametre[1]))
                print("Cihaz : " + parametre[2] + " - " + cihaz(parametre[2]))
                print("Durumu : " + parametre[3] + " - " + durum(parametre[3]))
        else:
            #parametre sayısı 4 değilse
            print("ikinci bölüm hatalı")
    #eğer parametre send ya da receive değil ise
    else:
        #hatayı yazsın
        print("send ya da receive içermiyor")
    #her döngü sonunda bir ayraç eklesin
    print("-----")