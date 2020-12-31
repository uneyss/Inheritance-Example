class Bilgisayar():
    def __init__(self,bilgisayar_durum = "Kapalı",bilgisayar_ekran = "HD",bilgisayar_ram = 16,bilgisayar_fan = 2):
        self.bilgisayar_durumu = bilgisayar_durum
        self.bilgisayar_ekran = bilgisayar_ekran
        self.bilgisayar_ram = bilgisayar_ram
        self.bilgisayar_fan = bilgisayar_fan

    def pc_ac(self):
        if(self.bilgisayar_durumu == "Açık"):
            print("Bilgisayar Zaten Açık...")
        else:
            self.bilgisayar_durumu = "Açık"
            print("Bilgisayar Açılıyor")

    def pc_kapat(self):
        if(self.bilgisayar_durumu == "Kapalı"):
            print("Bilgisayar Zaten Kapalı...")
        else:
            self.bilgisayar_durumu = "Kapalı"
            print("Bilgisayar Kapanıyor")

    def pc_ekran(self):
        while True:
            deger = input("Ekran Kalitesini Seçiniz :\n1. HD\n2. FULL HD\n3. 2k\n")

            if(deger == 'q'):
                print("Ekran Ayarlarından Çıkılıyor...")
                break
            elif(deger == "1"):
                self.bilgisayar_ekran = "HD"
                print("Ekran Kaliteniz : ",self.bilgisayar_ekran,"Olarak ayarlandı")
            elif(deger == "2"):
                self.bilgisayar_ekran = "FULL HD"
                print("Ekran Kaliteniz : ",self.bilgisayar_ekran,"Olarak ayarlandı")
            elif(deger == "3"):
                self.bilgisayar_ekran = "2k"
                print("Ekran Kaliteniz : ",self.bilgisayar_ekran,"Olarak ayarlandı")
            elif(deger == "4"):
                self.bilgisayar_ekran = "4k"
                print("Ekran Kaliteniz : ",self.bilgisayar_ekran,"Olarak ayarlandı")
            else:
                print("Yanlış Bir Tuşa Bastınız...")
    def pc_ram(self):
        while True:
            sayı = input("Yapmak İstediğiniz İşlemi Seçiniz\nÇıkış Yapmak İçin 'q' ya basınız...\n1. Ram Arttır\n 2. Ram Düşür\n")

            if(sayı == "q"):
                print("Çıkış Yapılıyor...")
            elif(sayı == "1"):
                if(self.bilgisayar_ram != 0):
                    self.bilgisayar_ram += 1
                    print("Bilgisayar rami arttırılıyor...",self.bilgisayar_ram)
            elif(sayı =="2"):
                if(self.bilgisayar_ram != 0):
                    self.bilgisayar_ram -=1
                    print("Ram Düşürülüyor...",self.bilgisayar_ram)
            else:
                print("Bilgisayar Ram'i Güncellendi :",self.bilgisayar_ram)
                break
    def pc_fan(self):
        while True:
            sayı = input("Yapmak İstediğiniz İşlemi Seçiniz\nÇıkış Yapmak İçin 'q' ya basınız...\n1. Fan Arttır\n 2. Fan Düşür\n")

            if(sayı == "q"):
                print("Çıkış Yapılıyor...")
            elif(sayı == "1"):
                if(self.bilgisayar_fan != 0):
                    self.bilgisayar_fan += 1
                    print("Bilgisayar rami arttırılıyor...",self.bilgisayar_fan)
            elif(sayı =="2"):
                if(self.bilgisayar_fan!= 0):
                    self.bilgisayar_fan -=1
                    print("Ram Düşürülüyor...",self.bilgisayar_fan)
            else:
                print("Bilgisayar Ram'i Güncellendi :",self.bilgisayar_fan)
                break
    def __str__(self):
        return "Bilgisayar Durumu:{}\nBilgisayar Ekranı:{}\nBilgisayar Ram'i:{}\nBilgisayar Fan'ı:{}\n".format(self.bilgisayar_durumu,self.bilgisayar_ekran,self.bilgisayar_ram,self.bilgisayar_fan)

bilgisayar = Bilgisayar()


print("""

Bilgisayar Ekranına Hoşgeldiniz

Çıkış Yapmak İçin 'q' ya basınız

1. PC Aç

2. PC Kapat

3. Ekran Ayarlarına Git

4. Bilgisayar Ram Ayarlarına Git

5. Bilgisayar Fan Ayarlarına Git

6. Bilgisayar Bilgilerini Göster 
""")

while True:
    işlem = input("İşlem Seçiniz:")
    if(işlem == 'q'):
        print("Çıkış Yapılıyor...")
        break
    elif(işlem == "1"):
        bilgisayar.pc_ac()
    elif(işlem == "2"):
        bilgisayar.pc_kapat()
    elif(işlem == "3"):
        bilgisayar.pc_ekran()
    elif(işlem == "4"):
        bilgisayar.pc_ram()
    elif(işlem == "5"):
        bilgisayar.pc_fan()
    elif(işlem == "6"):
        print(bilgisayar)
    else:
        print("Geçersiz İşlem...")