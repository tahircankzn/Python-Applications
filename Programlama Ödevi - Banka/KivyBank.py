"""
@author: Tahir Can Kozan - 21406601051

"""

"""
UYGULAMA ÖZELLİKLERİ :

1 - ÜYE OLMA
2 - PARA ÇEKME VE YATIRMA
3 - HESAPLAR ARASI PARA TRANSFERİ
4 - SON 10 HESAP GEŞMİŞİ - TARİH BİLGİLERİ İLE
5 - HESAP SİLME - BORÇ VARSA SİLMEYE İZİN VERMEZ
6 - BORÇ ALMA - BAKİYE EKSİYE DÜŞEBİLİR
7 - ŞİFRE DEĞİŞİKLİ

"""

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import random
import time


Window.clearcolor = (231/255.0, 179/255.0, 0/255.0,1) 

# BANKA İÇİN CLASS'LAR OLUŞTURULDU
class işlemler:
    
        

    def para_yatırma(self,tutar):
        self.tutar = tutar
        self.bakiye += self.tutar

    def para_çekme(self,tutar):
        self.tutar = tutar
        self.bakiye -= tutar
    
    


class user(işlemler):
    def __init__(self, hesapNo, isim,şifre, bakiye=0):
        super().__init__()
        self.bakiye = bakiye
        self.hesapNo = hesapNo
        self.isim = isim
        self.şifre = şifre
        self.hesapGeçmişi = []
    
    def şifre_değişim(self,yeni_şifre):
        self.şifre = yeni_şifre



# DENEME İÇİN KULLANICI EKLENDİ
users = {"2140660001":user(123,"tahir",123)}
hesapno = []
Kullanıcı = None # GİRİŞ YAPAN KULLANICININ ANLIK OLARAK TUTULMASI SAĞLANDI , GLOABAL OLARAK ULAŞILIYOR

########################  ARAYÜZ PENCERELERİ İÇİN CLASS'LAR ############################################
    
class MainWindow(Screen):
    
    def giriş(self):
        try:
            TC = self.ids.TC_input.text
            Password = int(self.ids.Password_input.text)
        

            try:
                if users[TC].şifre == Password:
                    global Kullanıcı
                    Kullanıcı = users[TC]
                    self.manager.transition.direction = "left"
                    self.manager.current = "second"
                else:
                    self.ids.feedback.text = "Hatalı Giriş"

            except:
                self.ids.feedback.text = "TC Hatalı"
        except:
            pass

    
     
        


class SecondWindow(Screen):  # HESABA GİRİŞ YAPTIKTAN SONRA AÇILAN SAYFA
    def exit(self):
        global Kullanıcı
        Kullanıcı = None
    
    
class TransferWindow(Screen): # HESAPLAR ARASI PARA TRANSFERİ PENCERESİ
    def on_enter(self):
        self.ids.bakiye3.text = str(Kullanıcı.bakiye)
    
    def restart(self):
        self.ids.bakiye3.text = ""
        self.ids.alici_input.text = ""
        self.ids.miktar2_input.text = ""
        self.ids.transfer_bilgiler.text = "Bakiye"

    def send(self):

        try:
            global Kullanıcı

            alıcı = int(self.ids.alici_input.text)
            miktar = int(self.ids.miktar2_input.text)

            if Kullanıcı.bakiye >= miktar:
                

                for i in users.keys():
                    
                    if alıcı == users[i].hesapNo:
                        Kullanıcı.para_çekme(miktar)
                        users[i].para_yatırma(miktar)
                        break
                self.ids.bakiye3.text = str(Kullanıcı.bakiye)


                Kullanıcı.hesapGeçmişi.append(f"{time.ctime()} | ->{miktar}") # HESAP GEÇMİŞİNE TARİH BİLGİSİ İLE EKLENMESİ SAĞLANDI

            else:
                self.ids.transfer_bilgiler.text = "Yetersiz Bakiye"
                pass
        except:
            pass

    


class UyeWindow(Screen): # ÜYE OLMA PENCERESİ

    def üyrOl(self):

        
        try:
            TC = self.ids.TC1_input.text
            Password = self.ids.Password1_input.text
            isim = self.ids.Name_input.text

            if len(TC) == 0 or len(Password) == 0 or len(isim) == 0:
                raise ArithmeticError
                

            for i in TC:
                if i not in ["0","1","2","3","4","5","6","7","8","9"]:
                    raise ZeroDivisionError  # GİRİLEN TC İÇİNDE RAKAM HARİCİ KARAKTER BULUNUYORSA GERİ BİLDİRİM VERMEK İÇİN RASGELE BİR HATA VERİLMESİ SAĞLANDI

            if TC not in users.keys():
                hesapNo = None
                while True:
                    hesapNo = random.randint(100,300) # RASGELE HESAP NUMARASI OLUŞTURULDU
                    if hesapNo not in hesapno: # DAHA ÖNCE KULLANILMAYAN NUMARANIN OLUŞTURULMASI İÇİN KARAR YAPISI
                        break
                
                users[TC] = user(hesapNo,isim,int(Password))
                global Kullanıcı
                Kullanıcı = users[TC]
                self.manager.transition.direction = "left" # SAYFA GEÇİŞİNİN SOLA DOĞRU KAYARAK YAPILMASI
                self.manager.current = "second" # second  İD'Lİ SAYFAYA GEÇİLMESİ
            
            else:
                self.ids.bilgi.text = "TC kullanılmış"
        except ValueError:
            self.ids.bilgi.font_size = 30
            self.ids.bilgi.text = "Şifre rakamlardan\noluşmalı"
        except ZeroDivisionError:
            self.ids.bilgi.font_size = 50
            self.ids.bilgi.text = "Hatalı TC"
        except ArithmeticError:
            self.ids.bilgi.font_size = 30
            self.ids.bilgi.text = "Bilgiler Boş Bırakılamaz"




class Hesapislemleri(Screen): # HESAP SİLME VE ŞİFRE DEĞİŞİKLİĞİ  SAYFALARINA GEÇİŞ  SAYFASI
    pass


class SifreDegisim(Screen): # ŞİFRE DEĞİŞTİRME SAYFASI
    def change(self):
        try:
            eski = self.ids.PasswordOld_input.text
            yeni = self.ids.PasswordNew_input.text
            if eski == str(Kullanıcı.şifre):
                Kullanıcı.şifre = int(yeni)
                print(eski,yeni)
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            self.ids.passwordError.font_size = 40
            self.ids.passwordError.text = "Hatalı Şifre"
        except ValueError:
            self.ids.passwordError.font_size = 30
            self.ids.passwordError.text = "Şifre rakamlardan\noluşmalı"
    
    def rest(self):
        self.ids.PasswordOld_input.text = ""
        self.ids.PasswordNew_input.text = ""
        self.ids.passwordError.text = ""
      


class HesapSil(Screen):   # HESAP SİLME SAYFASI
    def hesapSil(self):
        
        global Kullanıcı
        try:

            if self.ids.Password4_input.text == str(Kullanıcı.şifre):
                for i in users.keys():
                    if users[i] == Kullanıcı:
                        del users[i]
                        self.manager.transition.direction = "left"
                        self.manager.current = "main"
                        Kullanıcı = None
                        break
        
        except:
            pass

    def rest(self):
        self.ids.Password4_input.text = ""
        

class HesabimWindow(Screen): # HESABIM SAYFASI
    
    def on_enter(self):

        self.ids.hesap.text = f"{Kullanıcı.isim}\nHesap No :{Kullanıcı.hesapNo}"
        self.ids.hesapBakiye.text = f"Bakiye : {Kullanıcı.bakiye}"
    
    

    

class BakiyeWindow(Screen): # PARA ÇEKME VE YATIRMA İŞLEMLERİNİN YAPILDIĞI SAYFA

    def on_enter(self):
        self.ids.transferBakiye.text = f"Bakiye : {str(Kullanıcı.bakiye)}"
        
    def restart(self):
        self.ids.transferBakiye.text = ""
        self.ids.Miktar_input.text = ""
        self.ids.transferBilgi.text = ""


        
    def ParaCek(self):
        try:
            miktar = int(self.ids.Miktar_input.text)
            global Kullanıcı
            if miktar < 0:
                miktar = -miktar
            if miktar > Kullanıcı.bakiye:
                self.ids.transferBilgi.text = "Bakiye Yetersiz"
            else:
                
                Kullanıcı.para_çekme(miktar)
                self.ids.transferBakiye.text = str(Kullanıcı.bakiye)
                self.ids.transferBakiye.text = f"Bakiye : {str(Kullanıcı.bakiye)}"
                Kullanıcı.hesapGeçmişi.append(f"{time.ctime()} | -{miktar}") # HESAP GEÇMİŞİNE TARİH BİLGİSİ İLE EKLENMESİ SAĞLANDI
        except:
            pass

    def ParaYatir(self):
        try:
            global Kullanıcı
            miktar = int(self.ids.Miktar_input.text)
            if miktar < 0:
                self.ids.transferBilgi.text = "Tanımsız Miktar"
            else:
                
                Kullanıcı.para_yatırma(miktar)
                self.ids.transferBakiye.text = str(Kullanıcı.bakiye)
                self.ids.transferBakiye.text = f"Bakiye : {str(Kullanıcı.bakiye)}"
                Kullanıcı.hesapGeçmişi.append(f"{time.ctime()} | +{miktar}") # HESAP GEÇMİŞİNE TARİH BİLGİSİ İLE EKLENMESİ SAĞLANDI
        except:
            pass
        
    def BorcAl(self):
        
        try:
            miktar = int(self.ids.Miktar_input.text)
            global Kullanıcı
            
            if miktar <=0:
                self.ids.transferBilgi.text = "Tanımsız Miktar"
            else:
                
                Kullanıcı.para_çekme(miktar)
                self.ids.transferBakiye.text = str(Kullanıcı.bakiye)
                self.ids.transferBakiye.text = f"Bakiye : {str(Kullanıcı.bakiye)}"
                Kullanıcı.hesapGeçmişi.append(f"{time.ctime()} | ={miktar}") # HESAP GEÇMİŞİNE TARİH BİLGİSİ İLE EKLENMESİ SAĞLANDI
        except:
            pass
        
        
    
    

class HesapGecmisiWindow(Screen): # HESAP GEÇMİŞİ SAYFASI
    def on_enter(self):
        
        geçmiş = Kullanıcı.hesapGeçmişi
        

        
        while len(geçmiş) < 10: # SON 10 İŞLEMİN GÖSTERİLMESİ
            geçmiş.append(" ")
            

        self.ids.gecmis1.text = f"{geçmiş[0]}\n{geçmiş[1]}"
        self.ids.gecmis2.text = f"{geçmiş[2]}\n{geçmiş[3]}"
        self.ids.gecmis3.text = f"{geçmiş[4]}\n{geçmiş[5]}"
        self.ids.gecmis4.text = f"{geçmiş[6]}\n{geçmiş[7]}"
        self.ids.gecmis5.text = f"{geçmiş[8]}\n{geçmiş[9]}"
        



class WindowManager(ScreenManager): # PENCERELER ARASI GEÇİŞ YAPMAYA SAĞLAYAN ÖZEL KİVY SINIFI
    pass

kv = Builder.load_file("KivyBank.kv")


class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    
    MyMainApp().run()
