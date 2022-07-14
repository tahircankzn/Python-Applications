#from re import A
from tracemalloc import stop
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random
from kivy.clock import Clock

##############################
Window.clearcolor = (174/255.0, 174/255.0, 174/255.0,1)
##############################
########## AÇILIŞ EKRANI ########
class aç(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint=(1,1)#(0.6,1)
        self.window.pos_hint={"center_x": 0.5 ,"center_y": 0.5 }    
        
        
        self.greetingname = Label(text="      \n\n\n\n  Taş\n Kağıt\nMakas\n",font_size= 120,color="#0C0F03")
        self.window.add_widget(self.greetingname)
        
        self.greetingmy= Label(text="Powered by Tahir Can Kozan",font_size= 60,color="#2345CC")
        self.window.add_widget(self.greetingmy)
               
        Clock.schedule_once(self.stop,5) # belirlenen süre bitince class durur
        return self.window
  
########## OYUN BÖLÜMÜ ########
           
class tkm_oyunu(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 3
        self.window.size_hint=(1,1)#(0.6,1)
        self.window.pos_hint={"center_x": 0.5 ,"center_y": 0.5 }    
        
        
        self.greeting0 = Label(text="Jarvis",font_size= 60,color="#010202")
        self.window.add_widget(self.greeting0)
##############################
        
        self.greeting = Label(text="- / -",font_size= 90,color="#010202")
        self.window.add_widget(self.greeting) 
##############################
        self.greeting1 = Label(text="Player",font_size= 60,color="#010202")
        self.window.add_widget(self.greeting1)  
###############
        self.greeting2 = Label(text="-",font_size= 60,color="#010202")
        self.window.add_widget(self.greeting2)
##############################
        self.greeting3 = Label(text="VS",font_size= 100,color="#010202")
        self.window.add_widget(self.greeting3) 
##############################
        self.greeting4 = Label(text="-",font_size= 60,color="#010202")
        self.window.add_widget(self.greeting4)  
        
 ############################          
        self.button = Button(text="Taş", on_press=lambda a:self.taş())
        self.window.add_widget(self.button) 
##############################
        self.button1 = Button(text="Kağıt", on_press=lambda a:self.kağıt())
        self.window.add_widget(self.button1)
       
        self.button2 = Button(text="Makas", on_press=lambda a:self.makas())
        self.window.add_widget(self.button2)
               
        while self.greeting.text[0]=="3" or self.greeting.text[4]=="3":
                        
            self.greeting.text="- / -"
            self.greeting2.text="-"
            self.greeting4.text="-"
                        
        return self.window
        
######### Fonksiyonlar ###########
   
    def taş(self):
       self.greeting4.text="Taş"
       liste=['taş','kağıt','makas']
       jarvis = random.choice(liste)
       #########
       if jarvis == 'makas':
           self.greeting2.text="Makas"   
           harf=list(self.greeting.text)
                
           if harf[4] =="1":
               harf[4]='2'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
           elif harf[4]=='2':
               harf[4]='3'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
               if harf[4]=='3':
                   self.greeting.text="- / -"
                   self.greeting2.text="-"
                   self.greeting4.text="-"
                   self.greeting1.color='#F20A0E'
           elif harf[4]=='-':
               self.greeting1.color='#080000'
               self.greeting0.color='#080000'
               harf[4]='1'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text 
       elif jarvis == 'kağıt':
           self.greeting2.text="Kağıt"
           harf=list(self.greeting.text)
            
           if harf[0] =="1":
               harf[0]='2'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
           elif harf[0]=='2':
               harf[0]='3'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
               if harf[0]=='3':
                   self.greeting.text="- / -"
                   self.greeting2.text="-"
                   self.greeting4.text="-"
                   self.greeting0.color='#F20A0E'
           elif harf[0]=='-':
               self.greeting1.color='#080000'
               self.greeting0.color='#080000'
               harf[0]='1'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text

       ##########
       
       else:
           self.greeting1.color='#080000'
           self.greeting0.color='#080000'
           self.greeting2.text="Taş"
           self.greeting4.text="Taş"
                         
    def makas(self):
        self.greeting4.text="Makas"
        liste=['taş','kağıt','makas']
        jarvis = random.choice(liste)
       #########
        if jarvis == 'kağıt':
            self.greeting2.text="Kağıt"
            harf=list(self.greeting.text)
            
                              
            if harf[4] =="1":
                harf[4]='2'
                text=harf[0]+" / "+harf[4]
                self.greeting.text=text
            elif harf[4]=='2':
                harf[4]='3'
                text=harf[0]+" / "+harf[4]
                self.greeting.text=text
                if harf[4]=='3':
                    self.greeting.text="- / -"
                    self.greeting2.text="-"
                    self.greeting4.text="-"
                    self.greeting1.color='#F20A0E'
            elif harf[4]=='-':
                self.greeting1.color='#080000'
                self.greeting0.color='#080000'
                harf[4]='1'
                text=harf[0]+" / "+harf[4]
                self.greeting.text=text
                  
        elif jarvis == "taş":
            self.greeting2.text="Taş"
            harf=list(self.greeting.text)
             
            if harf[0] =="1":
                harf[0]='2'
                text=harf[0]+" / "+harf[4]
                self.greeting.text=text
            elif harf[0]=='2':
                harf[0]='3'
                text=harf[0]+" / "+harf[4]
                self.greeting.text=text
                if harf[0]=='3':
                    self.greeting.text="- / -"
                    self.greeting2.text="-"
                    self.greeting4.text="-"
                    self.greeting0.color='#F20A0E'
            elif harf[0]=='-':
                self.greeting1.color='#080000'
                self.greeting0.color='#080000'
                harf[0]='1'
                text=harf[0]+" / "+harf[4]
                self.greeting.text=text                
        else:
           self.greeting1.color='#080000'
           self.greeting0.color='#080000'
           self.greeting2.text="Makas"
           self.greeting4.text="Makas"
                            
    def kağıt(self):
        self.greeting4.text="kağıt"
        liste=['taş','kağıt','makas']
        jarvis = random.choice(liste)      
        if jarvis == "taş":
            self.greeting2.text="Taş"
            harf=list(self.greeting.text)
            
                              
            if harf[4] =="1":
               harf[4]='2'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
            elif harf[4]=='2':
               harf[4]='3'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
               if harf[4]=='3':
                   self.greeting.text="- / -"
                   self.greeting2.text="-"
                   self.greeting4.text="-"
                   self.greeting1.color='#F20A0E'
            elif harf[4]=='-':
               self.greeting1.color='#080000'
               self.greeting0.color='#080000'
               harf[4]='1'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
       
        elif jarvis == "makas":
           self.greeting2.text="Makas"
           harf=list(self.greeting.text)
           
                            
           if harf[0] =="1":
               harf[0]='2'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
           elif harf[0]=='2':
               harf[0]='3'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text    
               if harf[0]=='3':
                   self.greeting.text="- / -"
                   self.greeting2.text="-"
                   self.greeting4.text="-"
                   self.greeting0.color='#F20A0E' 
           elif harf[0]=='-':
               self.greeting1.color='#080000'
               self.greeting0.color='#080000'
               harf[0]='1'
               text=harf[0]+" / "+harf[4]
               self.greeting.text=text
               
        else:
           self.greeting1.color='#080000'
           self.greeting0.color='#080000'
           self.greeting2.text="Kağıt"
           self.greeting4.text="Kağıt"

#             
if __name__ == "__main__":
    #aç().run()
    tkm_oyunu().run()