import random


class öğrenci:
    def __init__(self,isim,tc,sınıf,şifre):
        self.şifre = şifre
        self.isim = isim
        self.tc = tc
        self.sınıf = sınıf
        self.notlar = {
            #      vize final
            "mat" : [0 , 0],
            "fen" : [0 , 0],
        }

    def ortalama(self):
        mat = self.notlar["mat"]
        fen = self.notlar["fen"]
        return (mat[0]+mat[1])/2 , (fen[0]+fen[1])/2

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
            "123" : müdür("ali","fen","ali123"),
            "1234" : öğretmen("ali","fen","ali123")

        }


sınıflar = {
    "sınıf1" : sınıfListesi(),
    "sınıf2" : sınıfListesi()
}


kadro = akademikKadro()
öğrenciler = {"123":öğrenci("Tahir Can Kozan",56144230822,1,1234)}

sınıflar["sınıf1"].liste.append(öğrenciler)
sınıflar["sınıf2"].liste.append({"1234":öğrenci("Ali",123456789,1,1234)})



while True:

    print("1 öğreci giriş , 2 öğretmen giriş")

    a = int(input("> "))

    if a == 1: # 1 öğreci giriş
        öğrenciNo = (input("> Öğrenci NO : "))
        şifre = (input("> şifre : "))

        if öğrenciler[öğrenciNo].şifre == şifre:
            print("giriş oldu")
        öğrenci1 = öğrenciler[öğrenciNo]
        while True:
            print("1 not bak ,2 not hesapla")
            k = input(">")

            if k == "1":
                print(öğrenci1.notlar)

            elif k == "2":
                print("1 ortalamarı hesapla ,2 elle hesapla")
                l = input(">")

                if l ==  "1":
                    mat , fen = öğrenci1.ortalama()
                    print(mat,fen)

                elif l ==  "2":
                    not1 = float(input(">1. not : "))
                    not2 = float(input(">2. not : "))
                    print(f"ortalama { (not1+not2)/2}")

    elif a ==2: # 2 öğretmen giriş
        doğrulama = 0
        for i in range(3):

            giriş = input("Öğretmen No : ")
            şifre = input("şifre : ")
            print(i)
            
            try:
                if kadro.liste[giriş].şifre == şifre:
                    doğrulama = 1
                    break
                
                    
            except KeyError:
                print("Öğretmen No hatalı !!")

            if i==2:
                    print("giriş sayısı aşıldı")
                    
        
        if doğrulama == 1:
            

            print("1 öğrenci işlemleri,2 sınav işlemleri")

            s = input("> ")

            if s =="1":

                print("1 öğrenci ekle , 2 öğrenci sil, 3 sınav notu gir, 4 sınıf listesi düzenle")

                r = input("> ")

                if r == "1":
                    y = input("> isim - tc - sınıf")
                    liste1 = list(y.split(" "))
                    öğrenciNo = None
                    while True:
                        öğrenciNo = random.randint(1,100)
                        if öğrenciNo not in öğrenciler.keys():
                            break
                    öğrenciler[str(öğrenciNo)] = öğrenci(liste1[0],liste1[1],liste1[2],liste1[1][0:5])
                    print(öğrenciNo,liste1[1][0:5])
                    
                    
                    
                elif r == "2":
                    s = input("silmek istediğniz öğrenci no :")
                    del öğrenciler[s]

                    for i in sınıflar:
                        if s in sınıflar[i].liste:
                            del sınıflar[i].liste[s]    ############


                elif r == "3":
                    for i in öğrenciler:
                        print(öğrenciler[i].isim,i)
                        mat1 = input("> mat vize")
                        mat2 = input("> mat final")

                        fen1 = input("> fen vize")
                        fen2 = input("> fen final")

                        öğrenciler[i].notlar["mat"] = [mat1,mat2]
                        öğrenciler[i].notlar["fen"] = [fen1,fen2]

                elif r == "4":
                    for i in sınıflar:
                        print(f"{i} :")
                        for a in sınıflar[i].liste:
                            [print(x) for x in a.keys()]

                    print("Sınıf değişikliği için öğrenci no ve sınıf seçiniz.")

                    öğrenciNo = input("> Öğrenci No : ")
                    ilkSınıf = input("> nerden : ")
                    ikinciSınıf = input("> nereye : ")

                    öğrenci_değişim = sınıflar[ilkSınıf]

                    del sınıflar[ilkSınıf].liste[0][öğrenciNo]

                    sınıflar[ikinciSınıf].liste[0][öğrenciNo] = öğrenci_değişim
                    print(sınıflar["sınıf1"].liste[0])
                    print(sınıflar["sınıf2"].liste[0])


