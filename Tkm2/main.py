from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.label import Label
#from kivy.uix.image import Image
#from kivy.uix.button import Button
#from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.lang import Builder
#from kivy.clock import Clock
from kivy.uix.widget import Widget
import random



Window.clearcolor = (174/255.0, 174/255.0, 174/255.0,1)

Builder.load_file("deneme.kv")
dosya = open("dm.txt","w")
dosya.write("0")
dosya.close()
class MainWindow(Widget):
    def ulti_dolum(self):   ######################################################################################################################################
        if int(self.ids.scor.text[4]) > 3:
            pass
        elif self.ids.scor.text[4] == "1":
            self.ids.healt1.source = "green.png"       ## def on_enter()  fonksiyonu sürekli çalışır
        elif self.ids.scor.text[4] == "2":
            self.ids.healt2.source = "yesil orta.png"
        elif self.ids.scor.text[4] == "3":
            self.ids.healt3.source = "yesil can son.png"

        #dosya = open("dm.txt","r")

        #if dosya.read() == "1":
            #self.ids.healt1.source = "yeşil can baş.png"
            #dosya.close()
        #elif dosya.read() == "2":
            #self.ids.healt2.source = "yesil orta.png"
            #dosya.close()
        #elif dosya.read() == "3":
            #self.ids.healt3.source = "yesil can son.png"
            #dosya.close()
        #else:
            #dosya.close()

        
        pass

    def atak(self):
        dosya = open("dm.txt","r")
        if dosya.read() == "3":
            self.ids.healt1.source = "beyaz can bas.png"
            self.ids.healt2.source = "beyaz orta.png"
            self.ids.healt3.source = "beyaz can son.png"
            dosya.close()
            self.ids.scor.text = self.ids.scor.text[0:4] + str(int(self.ids.scor.text[4])+2)
            if self.ids.scor.text[4] == "6":
                self.ids.scor.text = "0 / 0"
                self.ids.jarvisimg.source = "backgroundcard.png"
                self.ids.playerimg.source = "backgroundcard.png"
                self.ids.healt1.source = "beyaz can bas.png"
                self.ids.healt2.source = "beyaz orta.png"
                self.ids.healt3.source = "beyaz can son.png"
                dosya = open("dm.txt","w")
                dosya.write("0")
                dosya.close()

                self.ids.playerisim.color = "#FF0000" 
                   
                # self.ids.playerisim.color = "#FFFFFF" beyaz




        else:
            dosya.close()
    def kılıç(self):
        
        self.ids.playerimg.source = "sword.png"
        liste=['kılıç','kalkan','adam']
        jarvis = random.choice(liste)
        if jarvis == "adam":
            self.ids.jarvisimg.source = "adam.png"
            harf=list(self.ids.scor.text)
            
            ###############################################
            dosya = open("dm.txt","r")
            sayı = dosya.read()
            
            if sayı != "3":
                dosya.close()
                dosya1 = open("dm.txt","w")
                sayı1 = str(int(sayı) + 1)
                dosya1.write(sayı1)
                dosya1.close()
                
            elif sayı == "3":
                dosya.close()
            ###############################################
            
            if harf[4] =="1":
                harf[4]='2'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='2':
                harf[4]='3'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='3':
                harf[4]='4'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='4':
                harf[4]='5'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text

            elif harf[4]=='5':
                harf[4]='6'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                if harf[4]=='6':
                    self.ids.scor.text = "0 / 0"
                    self.ids.jarvisimg.source = "backgroundcard.png"
                    self.ids.playerimg.source = "backgroundcard.png"
                    self.ids.healt1.source = "beyaz can bas.png"
                    self.ids.healt2.source = "beyaz orta.png"
                    self.ids.healt3.source = "beyaz can son.png"
                    dosya = open("dm.txt","w")
                    dosya.write("0")
                    dosya.close()
                    self.ids.playerisim.color = "#FF0000" 

            elif harf[4]=='0':
                harf[4]='1'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                self.ids.playerisim.color = "#FFFFFF"
                self.ids.jarvisisim.color = "#FFFFFF"


        elif jarvis == "kalkan":
            self.ids.jarvisimg.source = "kalkan.png"
            harf=list(self.ids.scor.text)
            if harf[0] =="1":
                harf[0]='2'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='2':
                harf[0]='3'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='3':
                harf[0]='4'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='4':
                harf[0]='5'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text

            elif harf[0]=='5':
                harf[0]='6'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                if harf[0]=='6':
                    self.ids.scor.text = "0 / 0"
                    self.ids.jarvisimg.source = "backgroundcard.png"
                    self.ids.playerimg.source = "backgroundcard.png"
                    self.ids.healt1.source = "beyaz can bas.png"
                    self.ids.healt2.source = "beyaz orta.png"
                    self.ids.healt3.source = "beyaz can son.png"
                    dosya = open("dm.txt","w")
                    dosya.write("0")
                    dosya.close()
                    self.ids.jarvisisim.color = "#FF0000" 
                    
            elif harf[0]=='0':
                harf[0]='1'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                self.ids.jarvisisim.color = "#FFFFFF"
                self.ids.playerisim.color = "#FFFFFF"

        else:
            self.ids.jarvisimg.source = "sword.png"

    def kalkan(self):
        self.ids.playerimg.source = "kalkan.png"
        liste=['kılıç','kalkan','adam']
        jarvis = random.choice(liste)                
        if jarvis == "sword":
            
            self.ids.jarvisimg.source = "sword.png"
            harf=list(self.ids.scor.text)

            ###############################################
            dosya = open("dm.txt","r")
            sayı = dosya.read()
            
            if sayı != "3":
                dosya.close()
                dosya1 = open("dm.txt","w")
                sayı1 = str(int(sayı) + 1)
                dosya1.write(sayı1)
                dosya1.close()
                
            elif sayı == "3":
                dosya.close()
            ###############################################
            
            if harf[4] =="1":
                harf[4]='2'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='2':
                harf[4]='3'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='3':
                harf[4]='4'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='4':
                harf[4]='5'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text

            elif harf[4]=='5':
                harf[4]='6'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                if harf[4]=='6':
                    self.ids.scor.text = "0 / 0"
                    self.ids.jarvisimg.source = "backgroundcardcard.png"
                    self.ids.playerimg.source = "backgroundcardcard.png"
                    self.ids.healt1.source = "beyaz can bas.png"
                    self.ids.healt2.source = "beyaz orta.png"
                    self.ids.healt3.source = "beyaz can son.png"
                    dosya = open("dm.txt","w")
                    dosya.write("0")
                    dosya.close()
                    self.ids.playerisim.color = "#FF0000" 
        
            elif harf[4]=='0':
                harf[4]='1'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                self.ids.playerisim.color = "#FFFFFF"
                self.ids.jarvisisim.color = "#FFFFFF"


        elif jarvis == "adam":
            self.ids.jarvisimg.source = "adam.png"
            harf=list(self.ids.scor.text)
            if harf[0] =="1":
                harf[0]='2'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='2':
                harf[0]='3'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='3':
                harf[0]='4'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='4':
                harf[0]='5'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text

            elif harf[0]=='5':
                harf[0]='6'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                if harf[0]=='6':
                    self.ids.scor.text = "0 / 0"
                    self.ids.jarvisimg.source = "backgroundcard.png"
                    self.ids.playerimg.source = "backgroundcard.png"
                    self.ids.healt1.source = "beyaz can bas.png"
                    self.ids.healt2.source = "beyaz orta.png"
                    self.ids.healt3.source = "beyaz can son.png"
                    dosya = open("dm.txt","w")
                    dosya.write("0")
                    dosya.close()
                    self.ids.jarvisisim.color = "#FF0000" 

            elif harf[0]=='0':
                harf[0]='1'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                self.ids.jarvisisim.color = "#FFFFFF"
                self.ids.playerisim.color = "#FFFFFF"
        else:
            self.ids.jarvisimg.source = "kalkan.png"

    def adam(self):
        self.ids.playerimg.source = "adam.png"
        liste=['kılıç','kalkan','adam']
        jarvis = random.choice(liste)   
        if jarvis == "kalkan":
            
            self.ids.jarvisimg.source = "kalkan.png"
            harf=list(self.ids.scor.text)

            ###############################################
            dosya = open("dm.txt","r")
            sayı = dosya.read()
            
            if sayı != "3":
                dosya.close()
                dosya1 = open("dm.txt","w")
                sayı1 = str(int(sayı) + 1)
                dosya1.write(sayı1)
                dosya1.close()
                
            elif sayı == "3":
                dosya.close()
            ###############################################


            if harf[4] =="1":
                harf[4]='2'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='2':
                harf[4]='3'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='3':
                harf[4]='4'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[4]=='4':
                harf[4]='5'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text

            elif harf[4]=='5':
                harf[4]='6'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                if harf[4]=='6':
                    self.ids.scor.text = "0 / 0"
                    self.ids.jarvisimg.source = "backgroundcard.png"
                    self.ids.playerimg.source = "backgroundcard.png"
                    self.ids.healt1.source = "beyaz can bas.png"
                    self.ids.healt2.source = "beyaz orta.png"
                    self.ids.healt3.source = "beyaz can son.png"
                    dosya = open("dm.txt","w")
                    dosya.write("0")
                    dosya.close()
                    self.ids.playerisim.color = "#FF0000" 
                    

                    
                    
            elif harf[4]=='0':
                harf[4]='1'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                self.ids.playerisim.color = "#FFFFFF"
                self.ids.jarvisisim.color = "#FFFFFF"

        elif jarvis == "kılıç":
            self.ids.jarvisimg.source = "sword.png"
            harf=list(self.ids.scor.text)
            if harf[0] =="1":
                harf[0]='2'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='2':
                harf[0]='3'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='3':
                harf[0]='4'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
            elif harf[0]=='4':
                harf[0]='5'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text

            elif harf[0]=='5':
                harf[0]='6'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                if harf[0]=='6':
                    self.ids.scor.text = "0 / 0"
                    self.ids.jarvisimg.source = "backgroundcard.png"
                    self.ids.playerimg.source = "backgroundcard.png"
                    self.ids.healt1.source = "beyaz can bas.png"
                    self.ids.healt2.source = "beyaz orta.png"
                    self.ids.healt3.source = "beyaz can son.png"
                    dosya = open("dm.txt","w")
                    dosya.write("0")
                    dosya.close()
                    self.ids.jarvisisim.color = "#FF0000" 
                    
            elif harf[0]=='0':
                harf[0]='1'
                text=harf[0]+" / "+harf[4]
                self.ids.scor.text=text
                self.ids.jarvisisim.color = "#FFFFFF"
                self.ids.playerisim.color = "#FFFFFF"
        else:
            self.ids.jarvisimg.source = "adam.png"
    pass

class MyMainApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MyMainApp().run()
