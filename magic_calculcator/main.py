from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


#Window.size = (1080, 2032)
Window.clearcolor = (174/255.0, 174/255.0, 174/255.0,1)
class MainWindow(Screen):
    f = open("magictest.txt", "w")
    f.write("1")
    f.close()

    fdeletewrite = open("delete.txt", "w")
    fdeletewrite.write("1")
    fdeletewrite.close()
    

    def button_press(self,Button):
        listSignal = ["X","+","-","/","%"]
        if self.ids.result.text == "0":
            self.ids.result.text =  str(Button)
        elif self.ids.result.text[-1] in listSignal and Button in listSignal:
            self.ids.result.text = self.ids.result.text[0:-1] + str(Button) 
               
        else :
            self.ids.result.text =  self.ids.result.text + str(Button)

        
            
            pass
    def reset(self):
        self.ids.result.text = "0"
        f = open("magictest.txt", "w")
        f.write("1")
        f.close()
    
    def delete(self):
        fdelete = open("delete.txt", "r")
        if fdelete.read() == "2":
            fdelete.close()
            self.ids.result.text = "0"
            fdeletewrite = open("delete.txt", "w")
            fdeletewrite.write("1")
            fdeletewrite.close()
        elif self.ids.result.text != "0" :
            self.ids.result.text = self.ids.result.text[0:-1]
            if len(self.ids.result.text) == 0:
                self.ids.result.text = "0"

            
        elif len(self.ids.result.text) == 0:
            self.ids.result.text = "0"
        
    def  negativepositive(self):
        if self.ids.result.text[0] != "-" and self.ids.result.text[0] != "0":
            self.ids.result.text = "-"+self.ids.result.text
        elif self.ids.result.text[0] == "-" and self.ids.result.text[0] != "0":
            self.ids.result.text = self.ids.result.text[1:]


        pass
            
            
    def calculate(self):
        
        f = open("magictest.txt", "r")
        try :
            if self.ids.result.text == "5555%":
                self.manager.current = 'second'
                self.ids.result.text = "0"

                pass

            elif f.read() == "1" and "X" in self.ids.result.text:
                fmagic = open("magic.txt", "r")
                self.ids.result.text = fmagic.read()
                f.close()

                f = open("magictest.txt", "w")
                f.write("2")
                f.close()


                fdelete = open("delete.txt", "w")
                fdelete.write("2")
                fdelete.close()


                pass


            elif "%" in self.ids.result.text :
                list = self.ids.result.text.split("%")
                firstPoint = list[0]
                if "X" in firstPoint:
                    Xresult = firstPoint.replace("X","*")
                    self.ids.result.text = str(float(eval(Xresult))/100)[0:7]
                elif "-" in firstPoint:
                    self.ids.result.text = str(float(eval(firstPoint))/100)[0:7]
                elif "+" in firstPoint:
                    self.ids.result.text = str(float(eval(firstPoint))/100)[0:7]
                elif "/" in firstPoint:
                    self.ids.result.text = str(float(eval(firstPoint))/100)[0:7]
                else :
                    self.ids.result.text = str(int(firstPoint)/100)
                fdeletewrite = open("delete.txt", "w")
                fdeletewrite.write("2")
                fdeletewrite.close()
            

                pass
            elif "X" in self.ids.result.text  : 
                Xresult = self.ids.result.text.replace("X","*")

                self.ids.result.text = str(float(eval(Xresult)))

                fdeletewrite = open("delete.txt", "w")
                fdeletewrite.write("2")
                fdeletewrite.close()
            
            else:
                #self.ids.result.text = str(eval(str(self.ids.result.text)))
                a = str(float(eval(self.ids.result.text)))
                if "." in a:
                    
                    spot = a.index(".")
                    self.ids.result.text = a[0:(spot+6)]
                else :
                    self.ids.result.text = a

                fdeletewrite = open("delete.txt", "w")
                fdeletewrite.write("2")
                fdeletewrite.close()

                pass
            pass
        except SyntaxError :
            pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
class OptionsWindow(Screen):
    def on_enter(self):
        f = open("magic.txt", "r")
        self.ids.value.text = f.read()

    def magic(self):
        f = open("magic.txt", "w")
        my_value = self.ids.value.text
        
        f.write(my_value)
        f.close()

        

        pass
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("magic.kv")


class MagicApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
  
    MagicApp().run()