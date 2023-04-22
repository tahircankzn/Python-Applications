
"""
Para transferi işlemleri ekleyebilirsiniz. Kullanıcılar arasında para transferi yapılabilmesi için bir fonksiyon ekleyebilirsiniz.

Kullanıcıların hesap bilgilerini güncelleyebilecekleri bir seçenek ekleyebilirsiniz. Örneğin, kullanıcıların şifrelerini veya kişisel bilgilerini değiştirebilmelerini sağlayabilirsiniz.

Hesap özetini e-posta veya SMS gibi bir yöntemle kullanıcılara gönderebilirsiniz.

Kullanıcıların bakiyelerini ve hesap geçmişlerini daha iyi takip edebilmeniz için bir veritabanı kullanabilirsiniz.

Birden fazla hesap sahibi olan kullanıcılar için bir hesap yönetim sistemi ekleyebilirsiniz. Bu, kullanıcıların birden fazla hesap açabilmelerini ve her hesap için ayrı ayrı bakiye takip edebilmelerini sağlayabilir.
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
    
    def hesap_silme(self):
        pass


class user(işlemler):
    def __init__(self, hesapNo, şifre, bakiye=0):
        super().__init__()
        self.bakiye = bakiye
        self.hesapNo = hesapNo
        self.şifre = şifre
        self.hesapGeçmişi = []



    
        

#user1 = user(2,2)

users = {"112":user(21406601051,1234)}
hesapno = []




while True:
    kullanıcı = None
    print("hesap açkam için 1 , varsa 2")

    zaman_aşımı = 0
    for i in range(3):
        girdi = input("> ")
        if girdi in ["1","2"]:
            break
        if i == 2:
            zaman_aşımı = 1
    


    while zaman_aşımı == 0:
        if girdi == "1":
            tc = input("tc no : ")
            şifre = input("şifre")
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
                    tc = input("tc no : ")
                if şifre2 == None:
                    şifre = int(input("şifre"))
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
                    print("tc ve şifre yanlış")
                elif counter.__len__() == 1:
                    if counter[0] == 1:
                        print("tc yanlış")
                        
                    else :
                        print("şifre yanlış")
                        
                else:
                    kullanıcı = users[tc]
                    
                    break
            
        
        
        while True:
            hesapKapma = 0
            print("1 para çek ,2 para yatır,3 çıkış,4 hesap tutarı,5 hesap geçmişi,6 hesap silme")
            while True:
                b = int(input("> "))
                if b in [1,2,3,4,5,6]:
                    break
            if b == 1:
                f = int(input("> tutar :"))
                kullanıcı.para_çekme(f)
                kullanıcı.hesapGeçmişi.append(f"[{time.ctime()} : {f} TL para çekme , bakiye : {kullanıcı.bakiye}]")
                print(kullanıcı.bakiye)
            elif b == 2:
                f = int(input("> tutar :"))
                kullanıcı.para_yatırma(f)
                kullanıcı.hesapGeçmişi.append(f"[{time.ctime()} : {f} TL para yatırma , bakiye : {kullanıcı.bakiye}]")
                print(kullanıcı.bakiye)
            elif b == 3:
                break
            elif b == 4:
                print(kullanıcı.bakiye)
            elif b == 5:
                for i in range(10):
                    print(kullanıcı.hesapGeçmişi[i])

            elif b == 6:
                
                if kullanıcı.bakiye < 0:
                    print("bankamıza borçunuz nedeniyle hesabınızı kapatamıyoruz\nlütfen borçunuzu kapattıktan sonra tekrar deneyiniz")
                elif kullanıcı.bakiye > 0:
                    print("hesabınızı kapatmak istediğnize eminmisiniz ? [y] [n]")

                    while True:

                        s = input("> ")
                        s.lower()
                        if s in ["n","y"]:
                            break
                    
                    if s == "y":
                        print("hesabınız kapatılıyor...\nbekiyenizi aktarmamız için iban giriniz :")
                        t = input("> ")
                        del users[tc]
                        hesapKapma=1
                        
                elif kullanıcı.bakiye == 0:
                    print("hesabınızı kapatmak istediğnize eminmisiniz ? [y] [n]")

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

