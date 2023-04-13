#%%

class ex1:
    id = 100
    def __init__(self,id):
        self.id = id
        id = 800
        id = id + self.id


EX = ex1(123)

print(EX.id) # 123

print(ex1.id) # 100


##################################################################
#%%

class ex2:
    id = 100
    def __init__(self,id):
        self.id = self.id
        id = 800
        id = id + self.id


EX2 = ex2(123)

print(EX2.id) # 100
print(ex2.id) # 100

ex2.id = 500 # artık sonradan oluşturulacak tüm objelerde 500 olucak

print(EX2.id) # 100   # EX2 oluşturulurken 100 dü sonradan değiştirilmedi
print(ex2.id) # 500

##################################################################
#%%

class ex3:
    id = 100
    def __init__(self,id):
        self.id = id
        id = 800
        id = id + self.id

    def func(self):
        self.id = self.id + 200
        print(self.id)


EX3 = ex3(123)

print(EX3.id) # 123
print(ex3.id) # 100

EX3.func() # 323

print(EX3.id) # 323
print(ex3.id) # 100

ex3.id = 400 # sadece bu şekilde classın id si değiştirilir
# bundan sonra oluşturulacak objelerinki 400 olucak

# %%
