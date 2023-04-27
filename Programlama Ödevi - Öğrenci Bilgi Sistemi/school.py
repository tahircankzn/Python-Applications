import random


class öğrenci:
    def __init__(self,isim,tc,sınıf,şifre):
        self.şifre = şifre
        self.isim = isim
        self.tc = tc
        self.sınıf = sınıf
        self.notlar = {
            #      vize final
            "matematik" : [0 , 0],
            "Elektrik Devre Temelleri" : [0 , 0],
            "Bilgisayar Programlama" : [0 , 0],
            "Derin Öğrenme" : [0 , 0],
            "Optimizasyon Yöntemleri" : [0 , 0],
            
        }

    def ortalama(self):
        mat = self.notlar["matematik"]
        edt = self.notlar["Elektrik Devre Temelleri"]
        bp = self.notlar["Bilgisayar Programlama"]
        dö = self.notlar["Derin Öğrenme"]
        oy = self.notlar["Optimizasyon Yöntemleri"]
        
        return (mat[0]+mat[1])/2 , (edt[0]+edt[1])/2 , (bp[0]+bp[1])/2, (dö[0]+dö[1])/2, (oy[0]+oy[1])/2

class öğretmen:
    def __init__(self,isim,branş,şifre):
        self.şifre = şifre
        self.isim = isim
        self.branş = branş
        pass



class müdür(öğretmen):
    def __init__(self, isim, branş, şifre):
        super().__init__(isim, branş, şifre)
    


class sınıfListesi:
    def __init__(self):
        self.liste = []
        
class akademikKadro:
    def __init__(self):
        
        self.liste = {
            "123" : müdür("ali","Müdür","ali123"),
            "1234" : öğretmen("ali","matematik","ali123")

        }


sınıflar = {
    "sınıf1" : sınıfListesi()
}


kadro = akademikKadro()
öğrenciler = {"123":öğrenci("Tahir Can Kozan",56144230822,1,56144),
              "1234":öğrenci("Ali",123456789,1,12345)}

sınıflar["sınıf1"].liste.append(öğrenciler)


def sınıfListeleri(sınıflar):
    for i in sınıflar:
        print(f"{i}     Öğrenci No     İsim:\n")
        #print("Öğrenci No     İsim\n")
        for a in sınıflar[i].liste[0].keys():
            print(f"              {a}         {sınıflar[i].liste[0][a].isim}")
        print("\n")


while True:

    print("1 -> Öğrenci giriş\n2 -> Öğretmen giriş")
    while True:
        try:
            a = int(input("> "))
            break
        except:
            print("\nGeçersiz İşlem !\n")

    if a == 1: # 1 öğreci giriş

        
        doğrulama = 0
        for i in range(3):

            öğrenciNo = (input("> Öğrenci NO : "))
            şifre = int(input("> Şifre : "))
            
            
            try:
                if öğrenciler[öğrenciNo].şifre == şifre:
                    
                    doğrulama = 1
                    öğrenci1 = öğrenciler[öğrenciNo]
                    
                    break
                
                    
            except KeyError:
                print("Öğrenci No hatalı !!")

            if i==2:
                    print("giriş sayısı aşıldı")



        while doğrulama:
            print("1 -> Notlarım\n2 -> Not hesaplama\n3- > Çıkış")
            k = input(">")

            if k == "1":
                print(öğrenci1.notlar)

            elif k == "2":
                print("1 -> Ortalamarı hesapla\n2 -> Elle hesapla")
                l = input(">")

                if l ==  "1":
                    mat , edt , bp , dö , oy = öğrenci1.ortalama()
                    print(f"Matematik -> {mat}\nElektrik Devre Temelleri -> {edt}")
                    print(f"Bilgisayar Programlama -> {bp}\nDerin Öğrenme -> {dö}")
                    print(f"Optimizasyon Yöntemleri -> {oy}")



                elif l ==  "2":
                    not1 = float(input(">1. not : "))
                    not2 = float(input(">2. not : "))
                    print(f"ortalama { (not1+not2)/2}")
            elif k == "3":
                break



    elif a ==2: # 2 öğretmen giriş
        doğrulama = 0
        Müdür = 0
        Öğretmen_branşı = None
        for i in range(3):

            giriş = input("Öğretmen No : ")
            şifre = input("Şifre : ")
            
            
            try:
                if kadro.liste[giriş].şifre == şifre:
                    if kadro.liste[giriş].branş == "Müdür":
                        Müdür = 1
                    doğrulama = 1
                    Öğretmen_branşı = kadro.liste[giriş].branş
                    
                    break
                
                    
            except KeyError:
                print("Öğretmen No hatalı !!")

            if i==2:
                    print("giriş sayısı aşıldı")
                    
        
        if doğrulama == 1:




            if Müdür == 0: # öğretmen
                while True:
                    print("1 -> Sınav notu gir\n2 -> Sınıf listesi düzenle\n3 -> Sınıf Listeleri\n4 -> Çıkış")
                    while True:
                        r = input("> ")
                        if r in ["1","2","3","4"]:
                            break
                        else:
                            print("Geçersiz Seçim")

                    if r == "1":
                        for i in öğrenciler:
                            print(öğrenciler[i].isim,i)

                            

                            Not1 = input(f"> {Öğretmen_branşı} vize -> ")
                            Not2 = input(f"> {Öğretmen_branşı} final -> ")
                            
                            öğrenciler[i].notlar[Öğretmen_branşı] = [Not1,Not2]
                        




                    elif r == "2":
                        if len(sınıflar) > 1:
                            for i in sınıflar:
                                print(f"{i} öğrencileri :")
                                for a in sınıflar[i].liste:
                                    [print(x) for x in a.keys()]

                            print("Sınıf değişikliği için öğrenci no ve sınıf seçiniz.")

                            while True:
                                öğrenciNo = input("> Öğrenci No : ")
                                ilkSınıf = input("> Bulunduğu Sınıf : ")
                                ikinciSınıf = input("> Gideceği Sınıf : ")
                                try:
                                    öğrenci_değişim = sınıflar[ilkSınıf]
                                    del sınıflar[ilkSınıf].liste[0][öğrenciNo]
                                    sınıflar[ikinciSınıf].liste[0][öğrenciNo] = öğrenci_değişim
                                    for i in sınıflar:
                                        print(f"{i} öğrencileri :")
                                        for a in sınıflar[i].liste:
                                            [print(x) for x in a.keys()]
                                    break
                                except:
                                    print("Geçersiz İşlem")
                        else:
                            print("\nSınıf Sayısı 1\nYeterli Sınıf Yok\n")
                            

                    elif r == "3":
                        sınıfListeleri(sınıflar)


                    elif r == "4":
                        break





            else: # müdür
                # öğretmen ekle sil , sınıf aç sil
                starter1 = 1
                while starter1:
                    print("1 -> Öğrenci ekle\n2 -> Öğrenci sil\n3 -> Sınıf Listeleri\n4 -> Öğretmen Ekle\n5 -> Öğretmen Sil\n6 -> Sınıf Aç\n7 -> Sınıf Sil\n8 -> Çıkış")


                    while True:
                        r = input("> ")
                        if r in ["1","2","3","4","5","6","7","8"]:
                            break
                        else:
                            print("Geçersiz Seçim")



                    if r == "1":
                        
                        while True:
                            print("\nSINIFLAR :")
                            [print(x) for x in sınıflar.keys()]
                            try:
                                y = input("> isim - tc - sınıf\n")
                                liste1 = list(y.split(" "))
                                öğrenciNo = None

                                while True:
                                    öğrenciNo = random.randint(1,100)
                                    if öğrenciNo not in öğrenciler.keys():
                                        break
                                öğrenciler[str(öğrenciNo)] = öğrenci(liste1[0],liste1[1],liste1[2],liste1[1][0:5])

                                # liste1[2] bu sınıfa eklenmeli
                                try:
                                    sınıflar[liste1[2]].liste[0][str(öğrenciNo)] = öğrenciler[str(öğrenciNo)]
                                    break
                                except:
                                    print("Yanlış Sınıf ismi !")
                            except:
                                print("Hatalı İşlem")



                        print(f"Öğrenci No : {öğrenciNo}\nŞifre : {liste1[1][0:5]}")
                    
                    
                    
                    elif r == "2":
                        
                        for i in öğrenciler:
                            print(öğrenciler[i].isim,i)

                        try:
                            print("Çıkış yapmak için herhangi bir harfe basın !")
                            s = input("Silmek istediğniz öğrenci no :")
                            del öğrenciler[s]
                            for i in sınıflar:
                                if s in sınıflar[i].liste:
                                    del sınıflar[i].liste[s]    
                        except:
                            print("Geçersiz İşlem\n")
                        
                    
                    elif r == "3":
                        sınıfListeleri(sınıflar)

                    elif r == "4":

                        branşlar = ["matematik",
                                   "Elektrik Devre Temelleri", 
                                   "Bilgisayar Programlama",
                                   "Derin Öğrenme", 
                                   "Optimizasyon Yöntemleri"]

                        while True:
                            [print(f"{i+1} - {branşlar[i]}") for i in range(len(branşlar))]
                            try:
                                isim = input("> Öğretmen İsmi :")
                                branşNo = input("> Öğretmen Branş No :")
                                şifre = input("> Öğretmen Şifresi :")

                                if int(branşNo) in list(range(len(branşlar))):
                                    break
                                else:
                                    print("Geçersiz Branş")
                            except:
                                pass

                        branş = branşlar[int(branşNo)-1]
                        


                        ÖğretmenNo = None

                        while True:
                            no = random.randint(100,200)
                            if no not in kadro.liste.keys():
                                ÖğretmenNo = no
                                break
                            #kadro.liste[giriş].şifre
                        kadro.liste[str(ÖğretmenNo)] = öğretmen(isim,branş,şifre)
                        print(f"Öğretmen No : {str(ÖğretmenNo)}\nÖğretmen Şifresi : {şifre}")

                        # "1234" : öğretmen("ali","matematik","ali123")

                    elif r == "5":
                        starter = 1
                        while starter:
                            try:
                                print("\nÖğretmenler :")
                                for i in kadro.liste.keys():
                                    print(f"{i} {kadro.liste[i].isim} {kadro.liste[i].branş}")
                                a = input("\nÇIKIŞ YAPMAK İÇİN 0 GİRİN!!\nSilmek İstediğniz Öğretmen No : ")

                                if a == "0":
                                    break

                                if kadro.liste[a].branş == "Müdür":
                                    print("Müdürü Silme İstiyorsunuz !!\nDevam Etmek istiyorsanız Yeni Müdür bilgilerini eklemelisiniz !!")
                                    işlem = input("\n1 -> Çıkış\n2 - > Devam")

                                    if işlem == "1":
                                        break
                                    elif işlem == "2":
                                        ÖğretmenNo = None

                                        while True:
                                            no = random.randint(100,200)
                                            if no not in kadro.liste.keys():
                                                ÖğretmenNo = no
                                                break
                                        isim = input("Yeni Müdür İsimi : ")
                                        şifre = input("Yeni Müdür Şifresi : ")
                                        print(f"Müdür No : {ÖğretmenNo}")
                                        kadro.liste[str(ÖğretmenNo)] = öğretmen(isim,"Müdür",şifre)
                                        starter1 = 0
                                    else:
                                        print("Hata !")




                                
                                
                                del kadro.liste[a]
                                while True:
                                    exit = input("Öğretmen Silme işlemine devam etmek istiyormusunuz [y] [n] -> ")
                                    if exit == "n":
                                        starter = 0
                                        break
                                    elif exit == "y":
                                        break
                                    else:
                                        print("Geçersiz İşlem !")
                            except:
                                print("Öğrentmen No Hatası !")


                    elif r == "6":
                        sınıf = input("Sınıf isimini girin : ")

                        sınıflar[sınıf] = sınıfListesi()


                    elif r == "7":
                        print("Sınıf silmek için önce yeni bir sınıf açın")

                        sınıf = input("Yeni sınıf isimini girin : ")

                        

                        del_Sınıf = input("Silmek isdediğniz sınıf ismini girin : ")


                        sınıflar[sınıf] = sınıflar[del_Sınıf]


                    elif r == "8":
                        break


