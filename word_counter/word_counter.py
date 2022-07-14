from re import A
from tracemalloc import stop
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
##############################
Window.clearcolor = (174/255.0, 174/255.0, 174/255.0,1)
##############################
class kelime_sayacı(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint=(1,1)#(0.6,1)
        self.window.pos_hint={"center_x": 0.5 ,"center_y": 0.5 }    
##############################
        self.greeting0 = Label(text="Kelime Sayısı : 0",font_size= 60,color="#010202")
        self.window.add_widget(self.greeting0)
##############################
        #self.greeting = Label(text="Kelime Sayacı",font_size= 50,color="#010202")
        #self.window.add_widget(self.greeting) 
##############################
        #self.greeting = Label(text="Metin : ",font_size= 60,color="#010202")
        #self.window.add_widget(self.greeting)  
########## metin yazma yeri
        self.userLSEX2 = TextInput(multiline=True,padding_y=(30,30),size_hint=(1,1),text="",font_size=70,readonly=False)
        
    
        self.window.add_widget(self.userLSEX2)  
##############################
        
 
##############################
        self.button = Button(text="Hesapla", on_press=lambda a:self.hesapla(),background_color='#08FF0C')
        self.window.add_widget(self.button) 
##############################
        self.button = Button(text="Yenile", on_press=lambda a:self.reset())
        self.window.add_widget(self.button) ##############################
        return self.window  
##############################
    def reset(self):
        self.userLSEX2.text=''
        self.greeting0.text="Kelime Sayısı : 0"
        pass
##############################
    def hesapla(self):
        text=self.userLSEX2.text
        text_list=text.split()
        text_list2=list(text_list)
        text_leng=len(text_list2)
        
        spot=('.',',','?','!')      
        for i in spot:
            if i in text:
                text=text.replace(i,' ')
                ##text_list2.remove(i)
            
            text1 = text.split()
            text2 = list(text1)
            text_leng=len(text2)
        
            
            
            self.greeting0.text="Kelime Sayısı : {}".format(text_leng)
        else:
            self.greeting0.text="Kelime Sayısı : {}".format(text_leng)
        pass
##############################
if __name__ == "__main__":
    kelime_sayacı().run()