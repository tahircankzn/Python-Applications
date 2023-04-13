class car:
    var1 = 2

    def __init__(self,oil,speed,name):
        self.oil = oil
        self.speed = speed
        self.name = name

    def spoi(self):
        
        return self.oil/self.speed
    
    def features(self):

        print(self.name,self.oil,self.speed)
    def __str__(self):
        print("s")

class sportcar(car):
    def __init__(self, oil, speed, name,engine):
        super().__init__(oil, speed, name)
        #car.__init__(self,oil, speed,name)
        self.engine = engine



car1 = car(100,90,"car1")
car2 = car(10,10,"car2")
car3 = sportcar(6000,400,"sport1","engine 3")
#del car1.oil # obje silme

car1.features()


print(car1.var1)
car1.var1 = 10
print(car1.var1)

print(car3.engine)

#%%

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print(self):
        print(self.name,self.age)