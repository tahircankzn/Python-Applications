import cv2
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from kivy.uix.button import Button
from threading import Thread
from queue import Queue
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
import numpy as np
import time



Window.clearcolor = (174/255.0, 174/255.0, 174/255.0,1)

class MyLayout(Widget):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        self.frame_queue = Queue(maxsize=1)
        self.capture_thread = None
        self.capture = None
        

    
        
    def start_camera(self, instance):
        if self.capture_thread is None:
            Clock.schedule_interval(self.update, 1.0 / 30.0)
            self.capture_thread = Thread(target=self.capture_frames, daemon=True)
            self.capture_thread.start()

    def capture_frames(self): 
        self.capture = cv2.VideoCapture(0)  
        while True:
            ret, frame = self.capture.read()
            if not ret:             
                continue
            if not self.frame_queue.full():
                self.frame_queue.put(frame)

    def update(self, dt):

        
        
        if not self.frame_queue.empty():
            frame = self.frame_queue.get()

            height,width,chanel = frame.shape
            

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            self.ids.img1.texture = texture

    def on_stop(self):
        if self.capture:
            self.capture.release()

kv = Builder.load_file("v7.kv")
class Poyraz(App):
    def build(self):
        return kv

    def on_start(self):
        self.root.start_camera(None)

if __name__ == '__main__':
    Poyraz().run()



