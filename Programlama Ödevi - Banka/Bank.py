
"""
Kullanıcıların hesap bilgilerini güncelleyebilecekleri bir seçenek ekleyebilirsiniz. Örneğin, kullanıcıların şifrelerini veya kişisel bilgilerini değiştirebilmelerini sağlayabilirsiniz.
"""


import random
import time

class işlemler:
    
        

    def para_yatırma(self,tutar):
        self.tutar = tutar
        self.bakiye += self.tutar

    def para_çekme(self,tutar):
        self.tutar = tutar
        self.bakiye -= tutar



class user(işlemler):
    def __init__(self, hesapNo, şifre, bakiye=0):
        super().__init__()
        self.bakiye = bakiye
        self.hesapNo = hesapNo
        self.şifre = şifre
        self.hesapGeçmişi = []




users = {"112":user(21406601051,1234)}
hesapno = []




while True:
    kullanıcı = None
    print("1 -> Hesap aç\n2 -> Giriş")

    zaman_aşımı = 0
    for i in range(3):
        girdi = input("> ")
        if girdi in ["1","2"]:
            break
        if i == 2:
            zaman_aşımı = 1
    


    while zaman_aşımı == 0:
        if girdi == "1":
            tc = input("Tc No : ")
            şifre = input("Şifre : ")
            x = 0
            while True:
                y = random.randint(1,100)
                if y not in hesapno:
                    x = y
                    break

            users[tc] = user(x,şifre)
            kullanıcı = user(x,şifre)


        elif girdi == "2":
            tc2 = None
            şifre2 = None

            while True:

                if tc2 == None:
                    tc = input("Tc No : ")
                if şifre2 == None:
                    şifre = int(input("Şifre : "))
                counter = []

                if tc2 == None: 
                    if tc in users.keys():
                        pass
                    else:
                        counter.append(1)
                if şifre2 == None:
                    try:
                        if şifre == users[tc].şifre:
                            pass
                        else:
                            counter.append(2)
                    except KeyError:
                        counter.append(2)
                
                if counter.__len__() == 2:
                    print("TC ve Şifre yanlış")
                elif counter.__len__() == 1:
                    if counter[0] == 1:
                        print("TC yanlış")
                        
                    else :
                        print("Şifre yanlış")
                        
                else:
                    kullanıcı = users[tc]
                    
                    break
            
        
        
        while True:
            hesapKapma = 0
            print("1 -> Para çek\n2 -> Para yatır\n3 -> Çıkış\n4 -> Hesap tutarı\n5 -> Hesap geçmişi\n6 -> Hesap sil")
            while True:
                b = int(input("> "))
                if b in [1,2,3,4,5,6]:
                    break
            if b == 1:
                f = int(input("> Tutar :"))
                kullanıcı.para_çekme(f)
                kullanıcı.hesapGeçmişi.append(f"[{time.ctime()} : {f} TL para çekme , bakiye : {kullanıcı.bakiye}]")
                print(kullanıcı.bakiye)
            elif b == 2:
                f = int(input("> Tutar :"))
                kullanıcı.para_yatırma(f)
                kullanıcı.hesapGeçmişi.append(f"[{time.ctime()} : {f} TL para yatırma , bakiye : {kullanıcı.bakiye}]")
                print(kullanıcı.bakiye)
            elif b == 3:
                break
            elif b == 4:
                print(kullanıcı.bakiye)
            elif b == 5:
                try:
                    for i in range(10):
                        print(kullanıcı.hesapGeçmişi[i])
                except:
                    pass

            elif b == 6:
                
                if kullanıcı.bakiye < 0:
                    print("Bankamıza borçunuz nedeniyle hesabınızı kapatamıyoruz\nlütfen borçunuzu kapattıktan sonra tekrar deneyiniz")
                elif kullanıcı.bakiye > 0:
                    print("Hesabınızı kapatmak istediğnize eminmisiniz ? [y] [n]")

                    while True:

                        s = input("> ")
                        s.lower()
                        if s in ["n","y"]:
                            break
                    
                    if s == "y":
                        print("Hesabınız kapatılıyor...\nbekiyenizi aktarmamız için iban giriniz :")
                        t = input("> ")
                        del users[tc]
                        hesapKapma=1
                        break
                        
                elif kullanıcı.bakiye == 0:
                    print("Hesabınızı kapatmak istediğnize eminmisiniz ? [y] [n]")

                    while True:

                        s = input("> ")
                        s.lower()
                        if s in ["n","y"]:
                            break
                    
                    if s == "y":
                        
                        del users[tc]
                        hesapKapma=1


            elif hesapKapma == 1:
                break            

        break

