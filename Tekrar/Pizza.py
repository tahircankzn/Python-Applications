import pandas as pd
from IPython.display import display

class Menu:
    def __init__(self):
        self.menu = {}
        
    def add_menu(self,ürün,fiyat):
        self.menu[ürün] = fiyat
    
    def menü_göster(self):
        print("-------- Menü -------")
        print("> 0 : Çıkış")
        counter = 1
        for ürün , fiyat in self.menu.items():
            
            print(f"> {counter} : {ürün} - {fiyat}")
            counter+=1

class sipariş():
    def __init__(self,isim):
        
        self.isim = isim
        
        self.sipariş = {}

    def alım(self,ürün,adet,menu):
        self.menu = menu
        self.ürün = ürün
        self.adet = adet
        
        self.sipariş[self.ürün] = [self.adet]

    def sipariş_tamamla(self):
        total = 0
        for isim , adet in self.sipariş.items():
            total += self.menu[isim]*adet[0]
        return total 
        
        
class sepet:
    def __init__(self) -> None:
        pass   

menü = Menu()
menü.add_menu("Sosisli Pizza",65)
menü.add_menu("Suçuklu Pizza",75)
menü.add_menu("Karışık Pizza",80)
menü.add_menu("Ananaslı Pizza",60)
menü.add_menu("Vejeteryan Pizza",50)
menü.add_menu("Hamburger Pizza",75)
menü.add_menu("Büyük Boy Patates Kızartması",30)
menü.add_menu("Küçük Boy Kızartması",20)
menü.add_menu("Limonlu İce Tea",15)
menü.add_menu("Ayran",10)
menü.add_menu("Su",5)


def satın_alım1(ürün_adı,adet):
    user.sipariş[ürün_adı][0] +=adet

def satın_alım(ürün_adı,adet,menü):
    user.alım(ürün_adı,adet,menü)





siparişler = {

    "müşteri_no" : [],
    "kullanıcı" : [],
    "user" : [],
    "ücret" : []

}


müşteri_no = 0

print("--------- İyi Pizza Güzel Pizza --------")

while True:
    müşteri_no+=1

    print("> sipariş al : 1\n> siparişler : 2")
    seçim1 = input("> ")


    if seçim1 == "2":

        df = pd.DataFrame(siparişler)
        df = df.drop(['user'], axis=1)
        display(df)

    elif seçim1 == "1":

        kullanıcı = input("> isim : ")
        user = sipariş(kullanıcı)
        user_pack = [müşteri_no,kullanıcı,user]####


        siparişler["müşteri_no"].append(müşteri_no)
        siparişler["kullanıcı"].append(kullanıcı)
        siparişler["user"].append(user)

        #liste.append([müşteri_no,kullanıcı,user])
        
        print(menü.menü_göster())
        while True:
            
            while True:
                seçim = input("> Ürün no : ")
                if int(seçim) <=11 and int(seçim) >=0:
                    break
            

            # Sosisli Pizza
            if seçim == "1": 
                if "Sosisli Pizza" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Sosisli Pizza",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Sosisli Pizza",adet,menü.menu)

            # Suçuklu Pizza
            if seçim == "2": 
                if "Suçuklu Pizza" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Suçuklu Pizza",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Suçuklu Pizza",adet,menü.menu)

            # Karışık Pizza
            if seçim == "3": 
                if "Karışık Pizza" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Karışık Pizza",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Karışık Pizza",adet,menü.menu)
                    satın_alım("Karışık Pizza",adet,menü.menu)

            # Ananaslı Pizza
            if seçim == "4": 
                if "Ananaslı Pizza" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Ananaslı Pizza",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Ananaslı Pizza",adet,menü.menu)

            #Vejeteryan Pizza        
            if seçim == "5": 
                if "Vejeteryan Pizza" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Vejeteryan Pizza",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Vejeteryan Pizza",adet,menü.menu)

            # Hamburger Pizza
            if seçim == "6": 
                if "Hamburger Pizza" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Hamburger Pizza",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Hamburger Pizza",adet,menü.menu)

            # Büyük Boy Patates Kızartması
            if seçim == "7": 
                if "Büyük Boy Patates Kızartması" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Büyük Boy Patates Kızartması",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Büyük Boy Patates Kızartması",adet,menü.menu)

            # Küçük Boy Kızartması
            if seçim == "8": 
                if "Küçük Boy Kızartması" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Küçük Boy Kızartması",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Küçük Boy Kızartması",adet,menü.menu)
            
            # Limonlu İce Tea
            if seçim == "9": 
                if "Limonlu İce Tea" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Limonlu İce Tea",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Limonlu İce Tea",adet,menü.menu)

            # Ayran
            if seçim == "10": 
                if "Ayran" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Ayran",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Ayran",adet,menü.menu)

            # Su
            if seçim == "11": 
                if "Su" in list(user.sipariş):
                    adet = int(input("> Adet : "))
                    satın_alım1("Su",adet)
                    #user.sipariş["Pizza"][0] +=adet

                else:
                    adet = int(input("> Adet : "))
                    #user.alım("Sosisli Pizza",adet,menü.menu)
                    satın_alım("Su",adet,menü.menu)
                    


            elif seçim == "0":
                print(user.sipariş_tamamla())
                
                user_pack.append(user.sipariş_tamamla())
                siparişler["ücret"].append(user.sipariş_tamamla())

                break
