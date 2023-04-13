######################  PYTHON TEKRAR ######################
######################     NOTLARI    ######################
# @author: Tahir Can Kozan

x = y = z = 5

x,y,z = 1,2,3

#%%
###############################################################################


liste = [1,2,3]

number1,number2,number3 = liste

#%%
###############################################################################


text1 = "Tahir"
text2 = "Can"
text3 = "Kozan"

print(text1 , text2, text3) # Tahir Can Kozan
print(text1 + text2 + text3) # TahirCanKozan
print("{}{}{}".format(text1 , text2, text3 )) # TahirCanKozan
print("{} {} {}".format(text1 , text2, text3 )) # Tahir Can Kozan

#%%
###############################################################################


text4 = "tahir"
number4 = 3
print(number4 , text4) # 3 tahir
print(str(number4) + text4) # 3tahir


###############################################################################
# GLOBAL DEĞİŞKENLER
#%%

variables1 = "tahir" # fonksiyon dışında olan bir değişken , bütün fonksiyonlar buna ulaşabilir

def tahir():
    print("ben " + variables1)

tahir()


###############################################################################
#%%

class student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = student("tahir",22)
print("ad : {} , yaş : {}".format(student1.name,student1.age))


###############################################################################
#%%

variables2 = 2 # global değişken

def deneme():
    variables2 = 3 # globali değiştirmez
    print(variables2) # global olan variables2  değer değil, fonksiyon içindeki variables2

deneme() # 3

print(variables2) # 2  , global 


###############################################################################
#%%

variables3 = 1

print(variables3) # global

def deneme1():
    global variables3 
    variables3 = 0     # global değeri değiştirildi

    print(variables3) # 0

deneme1() 

print(variables3) # 0


###############################################################################
#%%

def deneme2():
    global variables4   # fonksiyon içinde global değişken oluşturuldu
                        # yani fonksiyon kullanımı bitse bile artık bu değişken global olduğu için heryerden ulaşılabilir oldu
    variables4 = 2

    print(variables4)

deneme2()

print(variables4)


###############################################################################
#%%

x = "Hello World" # str
x = 20	# int	
x = 20.5	# float	
x = 1j	# complex	
x = ["apple", "banana", "cherry"]	# list	
x = ("apple", "banana", "cherry")	# tuple	
x = range(6)	# range	
x = {"name" : "John", "age" : 36}	# dict	
x = {"apple", "banana", "cherry"}	# set	
x = frozenset({"apple", "banana", "cherry"})	# frozenset	
x = True	# bool	
x = b"Hello"	# bytes	
x = bytearray(5)	# bytearray	
x = memoryview(bytes(5))	# memoryview	
x = None
print(type(x)) # type() tipini gösterir


###############################################################################
#%%

variables5 = 4

print(variables5.as_integer_ratio()) # kesirli halini varir


###############################################################################
#%%

variables6 = 35e3 # 35 x 10 üzeri 3
variables7 = 35E3 # 35 x 10 üzeri 3
variables8 = -87E10 # -87 x 10 üzeri 10


###############################################################################
#%%

variables8 = "5"
print(variables8 , type(variables8))
variables8 = int(variables8)
print(variables8 , type(variables8))
variables8 = float(variables8)
print(variables8 , type(variables8))


###############################################################################
#%%

liste1 = [1,2,3,4]

print(liste1[0]) # 1

string1 = "tahir can kozan"
print(string1[0]) # t


###############################################################################
#%%

string2 = "tahir can kozan"

for i in string2:
    print(i)

for i in "tahir can kozan":
    print(i)
                    # len() int ve floatlarda çalışmaz
print(len(string2)) # string2 değişkenin kaç karakterli olduğu
print(string2.__len__()) # stringlerin bağlı oldu class dan gelen özellikler
                         # python nesne tabanlı olmasını burdan anlarız


###############################################################################
#%%

string3 = "tahir can kozan"

print("tahir" in string3) # True

print("tahir","can" in string3) # tahir True
                                # virgüller değişkenleri ayırır
                                # tahir yazıcak sonra can str içindeyse ona göre bool çıktı yazdırır

liste2 = ["tahir","can" ,"kozan"]
print("tahir" in liste2) # True


###############################################################################
#%%

print("tahir" in liste2) # True

print("tahir21" in liste2) # False


###############################################################################


# t a h i r   c a n   k  o  z  a  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
#            ...         -4 -3 -2 -1
                                  
print(string3[0:3]) # tah  , 0. dan 2. index e kadar

print(string3[:3]) # tah   ,0. dan 2. index e kadar

print(string3[2:]) # hir can kozan   ,2. den sonuna kadar kadar

print(string3[0:3:2]) # th   ,0. dan 2. index e kadar 2 şer adımlarla ilerler

print(string3[-1]) # n    ,son karakter

print(string3[-2:-5:-1]) # -2 -3 -4 değerler yazılır

print(string3[-2:-5]) # boş çıkar çünkü -2 den başlayınca otomatik
                      # soldan sağ gider ama -5 -2nin solunda


# [-3:-4] dersek
#  t  a  h  i   r      yön belirmedikce soldan sağa gider
# -5 -4 -3 -2  -1
#        |------->   sona geldik bitti , yön belirmedikce soldan sağa gider
#                    bu yüzden boş çıktı verir

# [-3:-4:-1] dersek
#  t  a  h  i   r   
# -5 -4 -3 -2  -1      h çıktısı verir 
#     <--|             


###############################################################################

print(string3.upper()) # TAHIR CAN KOZAN
print(string3.lower()) # tahir can kozan

print(string3.strip()) # baştaki ve sondaki boşlukları siler varsa

print(string3.replace("h", "H")) # h karakterini çıkardı H karakterini koydu
                                 # değiştirdi

print(string3.split("a")) # ['t', 'hir c', 'n koz', 'n']   , a harfleri çıkarılır ve ayrılır

items1 = string3.split("a")   # ['t', 'hir c', 'n koz', 'n']
print(items1[1])  # "hir c"       0       1        2     3


###############################################################################
#%%
variables9 = "tahir"
variables10 = "can"
print(variables9 + " " + variables10)
variables11 = variables9 + " " + variables10


###############################################################################
#%%

# string ile int toplanamaz , verileri dönüştümeliyiz


variables12 = "can"
number5 = 3
print(variables12,str(number5)) # can 3


print("{} {}".format(variables12,number5)) # can 3
print("{0} {1}".format(variables12,number5)) # can 3
print("{1} {0}".format(variables12,number5)) # 3 can


variables13 = "{} {}"
print(variables13.format(variables12,number5)) # can 3

print(f"{variables12} {number5}") # can 3


###############################################################################
#%%

x = 5
y= 10
z = x/y


print(z.__floor__()) # tam sayıya yuvarlar

###############################################################################


"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""


###############################################################################
#%%

x = 5
print(id(x))
y = 6
print(id(y))
#print(x is z) # false
x=y
print(id(x))
print(id(y))
#print(x is z) # true



a = 4
b = 4
print(id(a))   # 2 swğişkende aynı olunca adresleri aynı olur
print(id(b))
#print(a==b)


###############################################################################
#%%

liste = ["tahir","can"]
liste1 = ["tahir","can"]

print(id(liste))    # 2 listede aynı olsa bile farklı adreste tutuluyorlar
print(id(liste1))


###############################################################################

"""
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""

###############################################################################
#%%

print(3<<2) # 3 ün binary değerini 2 bit sola kaydırır
print(8>>2) # 8 ün binary değerini 2 bit sağa kaydırır


###############################################################################
#%%

# if den sonra tek satırlık kodumuz varsa yan yana yazılabilir
a=5
b=3

if a > b: print("a is greater than b")


if a > b:
    print("a is greater than b")


###############################################################################
#%%

# if ve else için tek satırlık kodumuz varsa hepsi tek satırda yazılabilir
a = 2
b = 330
print("A") if a > b else print("B")


###############################################################################
#%%

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

if a > b:
    print("A")
else:
    if a == b:
        print("=")
    else:
        print("B")

###############################################################################
#%%

# değişkenler True değerdöndürür
if 2:
    print("True")

# değişken sıfırsa false

if 0: # çalışmaz
    print("FALSE")


###############################################################################
#%%

liste = ["tahir","can","kozan"]

liste.insert(1,"22")   # 0 ile 1 indeklserin arasına "22"
                       # koydu 
print(liste) # ['tahir', '22', 'can', 'kozan']


###############################################################################
#%%

liste = ["tahir","can","kozan"]
liste2 = [22,23,24]

liste.extend(liste2)
print(liste)    # ['tahir', 'can', 'kozan', 22, 23, 24]

###############################################################################
#%%

liste = ["tahir","can","kozan"]
liste.remove("can") # "can" nı siler

liste = ["tahir","can","kozan"]
liste.pop(1) # 1. indeksi siler
liste.pop() # sondakini siler



liste = ["tahir","can","kozan"]
del liste[0] # 0. indeksi siler
del liste # kompile siler


liste = ["tahir","can","kozan"]
liste.clear() # liste içini siler

liste = ["tahir","can","kozan"]
liste.append("22") # listenin sonuna ekleme yapar
print(liste) 

###############################################################################
#%%

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) # ['apple', 'banana', 'mango']



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) # ['apple', 'banana', 'mango']

###############################################################################
#%%

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist) # ['apple', 'orange', 'cherry', 'kiwi', 'mango']


###############################################################################
#%%

liste3 = [1,2,3,4,5,6,7,8,9,10]
newlist2 = [x for x in liste3 if x%2==0 and x != 4]
print(newlist2) # [2, 6, 8, 10]


###############################################################################
#%%

liste4 = [*range(6)]
print(liste4)

###############################################################################
#%%

liste4 = [*range(1,6,2)]
print(liste4) # [1, 3, 5]

###############################################################################
#%%

liste5 = [i for i in range(10)]
print(liste5)

###############################################################################
#%%

liste6 = [ i for i in range(10) if i > 5]
print(liste6)

###############################################################################
#%%

liste7 = ["apple", "banana", "cherry", "kiwi", "mango"]

liste8 = [liste7[i].upper() for i in range(5)]

print(liste8) # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


###############################################################################
#%%
liste7 = ["apple", "banana", "cherry", "kiwi", "mango"]
liste7.sort()
print(liste7) # ['apple', 'banana', 'cherry', 'kiwi', 'mango']


###############################################################################
#%%

liste10 = [x for x in range(20) if x%2 != 0 and x !=1]
print(liste10) # [3, 5, 7, 9, 11, 13, 15, 17, 19]

###############################################################################
#%%

liste9 = [1,3,2,4,5,8,7,6,9]
liste9.sort() # reverse = False 
print(liste9) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

liste9.sort(reverse = True)
print(liste9) # [9, 8, 7, 6, 5, 4, 3, 2, 1]


###############################################################################
#%%

def func(x):
    return abs(x-2) # abs() mutlak değer , absolute

liste9 = [1,3,2,4,5,8,7,6,9]
liste9.sort(key = func) 
print(liste9) # [2, 1, 3, 4, 5, 6, 7, 8, 9] 
              # [0, 1, 1, 2, 3, 4, 5, 6, 7]  fonksiyondan gelen veri

###############################################################################
#%%

liste7 = ["Apple", "banana", "Cherry", "kiwi", "mango"]
liste7.sort() # ASCII tablosunda büyük harflerin sayısal değeri daha büyük
print(liste7) # ['Apple', 'Cherry', 'banana', 'kiwi', 'mango']

###############################################################################
#%%

liste7 = ["Apple", "banana", "Cherry", "kiwi", "mango"]
liste7.sort(key = str.lower) # liste verilerini küçük harfe çevirir ve ona göre sıralar
print(liste7) # ['Apple', 'banana', 'Cherry', 'kiwi', 'mango']

###############################################################################
#%%

liste7 = ["Apple", "banana", "Cherry", "kiwi", "mango"]
liste6 = liste7.copy()
liste6.sort(key = str.__len__) # karakter sayısına göre sıralandı
print(liste6) # ['kiwi', 'Apple', 'mango', 'banana', 'Cherry']
print(liste7) # ['Apple', 'banana', 'Cherry', 'kiwi', 'mango']

###############################################################################
#%%

liste7 = ["Apple", "banana", "Cherry", "kiwi", "mango"]
liste6 = liste7
liste6.sort(key = str.__len__) # karakter sayısına göre sıralandı
print(liste6) # ['kiwi', 'Apple', 'mango', 'banana', 'Cherry']
print(liste7) # ['kiwi', 'Apple', 'mango', 'banana', 'Cherry']
# listemizi kopyalamadığmız için 2 listede aynı şekilde değişti

###############################################################################
#%%

liste7 = ["Apple", "banana", "Cherry", "kiwi", "mango"]
liste6 = list(liste7)
liste6.sort(key = str.__len__) # karakter sayısına göre sıralandı
print(liste6) # ['kiwi', 'Apple', 'mango', 'banana', 'Cherry']
print(liste7) # ['Apple', 'banana', 'Cherry', 'kiwi', 'mango']
# listemizi atarken tekrar liste yaptığmız için ilk listemiz korunmuş oldu

# budurumların sebebi bir listeyi başka bir listeye atarsak iki listede aynı 
# adreste tutuluyor ve ikside değişiyor , id(liste5) ile adresleri görebiliriz
# bunun önüne geçmek için .copy() ile yada list(liste7) ile atarsak sorun çözülür



###############################################################################
#%%

liste = [1,2,3]
liste2 = ["a","b","c"]
print(liste + liste2) # [1, 2, 3, "a", "b", "c"]

###############################################################################
#%%

liste = [1,2,3]
liste2 = ["a","b","c"]
liste.extend(liste2) # ilk listenin sonuna 2. liste eklenir

print(liste) # [1, 2, 3, "a", "b", "c"]

###############################################################################
#%%

def kare(x):
    return f"{x}'in karesi {x**2}"

liste = [kare(i) for i in range(1,10)]

[print(i) for i in liste]

"""
1'in karesi 1
2'in karesi 4
3'in karesi 9
4'in karesi 16
5'in karesi 25
6'in karesi 36
7'in karesi 49
8'in karesi 64
9'in karesi 81
"""

###############################################################################
#%%

# kids parametresi bir tuple
def func(*kids): # birden fazla veri gelebilirse başına * konur
    [print(x) for x in kids]

func("a","1","2")

###############################################################################
#%%

def name(name,lastName,age):
    print(f"my name is {name} {lastName} and I am {age}")

name("Tahir Can","Kozan",22) # my name is Tahir Can Kozan and I am 22
name(lastName="Kozan",name="Tahir Can",age=22) # my name is Tahir Can Kozan and I am 22


###############################################################################
#%%

# burdaki kids bir dictionary olmuş oldu çünkü keyler var
def func(**kids): # key sayısı fazla ise 
    print(kids["lname"])

func(fname = "tahir can",lname = "kozan") # kozan

dict = {

    "fname" : "tahir can",
    "lname" : "kozan"

}

###############################################################################
#%%

def func(name,country = "Turkey"):
    print(f"{name} is from {country}")

func("Tahir Can Kozan") # Tahir Can Kozan is from Turkey
func("Tahir Can Kozan","Canada") # Tahir Can Kozan is from Canada

###############################################################################
#%%

def func(liste):
    [print(x) for x in liste]
liste1 = [1,2,3,4,5,6]
func(liste1)

###############################################################################
#%%

def func(variable):
    return variable

print(func("sa"))

###############################################################################
#%%

def üçgen(*açı):
    for i in açı:
        if i < 90 and i>0:
            print(f"{i} dar açı")
        elif i == 90:
            print(f"{i} dik açı")
        elif i>90:
            print(f"{i} geniş açı")
        else:
            print(f"{i} yanlış açı")

üçgen(30,45,60,90,180,360,-2)

"""
30 dar açı
45 dar açı
60 dar açı
90 dik açı
180 geniş açı
360 geniş açı
-2 yanlış açı

"""

###############################################################################
#%%

# geri dönüşlü fonk

def faktöriyel(x):
    if x > 1:
        return x*faktöriyel(x-1)
    else:
        return 1
    
def toplam(x):
    if x > 1:
        return x+toplam(x-1)
    else:
        return 1

print(faktöriyel(5)) # 120
print(toplam(5)) # toplam

###############################################################################
#%%

# lambda fonksiyonu
# bu fomksiyon bir değişkene atanır

x = lambda a : a + 10

print(x(5))
[print(i) if i != 4 else print("___") for i in range(5)]

y = lambda t,y : t*y

print(y(5,2))


t = lambda : 10
print(t()) # 10

###############################################################################
#%%

def func(n):
    return lambda a : a * n

mydoubler = func(2) # a değerinin yerine geçti
mytripler = func(3) # a değerinin yerine geçti

print(mydoubler(11)) # a değeri 2 o yüzden 2*11
print(mytripler(11)) # a değeri 3 o yüzden 3*11

###############################################################################
#%%


while True:
    break

a= 1
while a<10:
    print(f"{a}")
    if a == 4:
        break
    a+=1
print("--")

a= 0
while a<10:
    
    a+=1
    if a == 4:
        continue
    print(f"{a}")


###############################################################################
#%%


a = 0
while a<6:
    print("a")
    a+=1
else:
    print("bitti") 


###############################################################################
#%%

# enumarate

x =("a","b","c")

y = enumerate(x)

print(list(y)) # [(0, 'a'), (1, 'b'), (2, 'c')]

for number , item in enumerate(x): # list(y) yada y şeklide verilmez
                                   # fonksiyon yazılmalı
    print(f"{number}-{item}")


###############################################################################
#%%

# bu daha yavaş 

import time

times = time.time()
liste = []
for i in range(10**7):
    liste.append(i)
print(time.time()-times)



###############################################################################
#%%

# bu daha hızlı
import time

times = time.time()
liste = [i for i in range(10**7)]

print(time.time()-times)


###############################################################################
#%%
import time

print(time.ctime(0))
print(time.ctime())


###############################################################################
#%%



def slow(n):
    liste = []
    for i in range(n**2):
        liste.append(i)
    return liste

def fast(n):
    return [i for i in range(n**2)]

start = time.time()
print(slow(2))
print(time.time()- start)
start = time.time()
print(fast(2))
print(time.time()- start)

###############################################################################
#%%


import time
start = time.time()
matris = []

for i in range(10):
    matris.append([])

    for a in range(10):
        matris[i].append(a)
print(matris)       
print(time.time()- start)


###############################################################################
#%%


import time
start = time.time()
liste = [[a for a in range(10)] for i in range(10)]
print(liste)
print(time.time()- start)


###############################################################################
#%%
# ????????? çam ağçı
b = 10
b1 = b-4
c = b-b/2

"""
b = 6
b1 = 4
c = b-3
"""

liste = [[f"{i}" if a>c-i and a < c+i else "-" for a in range(1,b)] for i in range(1,b1)]
[print(i) for i in liste]

###############################################################################
#%%
# polidrom

kelime = "adanada"

kelime_n = ""

for i in range(-1,-(kelime.__len__()+1),-1):
    kelime_n += kelime[i]

if kelime == kelime_n:
    print("polidrom")
else:
    print("polidrom değil")


###############################################################################
#%%
# liste elemanı ayıklama

def delete(liste,num):

    liste.sort()
    liste_c = liste.copy()

    for i in range(num):
        
        liste_c.remove(liste_c[i])
        
    for i in range(-1,-(num+1),-1):
        liste_c.remove(liste_c[i])

    return liste_c

liste = [1,6,4,5,3,7]
 
print(delete(liste,1))

###############################################################################
#%%
# liste elemanı ayıklama

def delete(liste,num):
    liste = sorted(liste)

    for i in range(num):
        liste.pop()
        liste.pop(0)

    
    return liste

liste = [1,6,4,5,3,7]
 
print(delete(liste,1))


###############################################################################
#%%
# faktoriyel hesabı 


def faktoriyel(num):
    result = 1
    if num > 0:
        for i in range(1,num+1):
            result *= i
        print(result)
    else:
        print("tanımsız değer")

print("çıkış yapmak için 0")
while True:
    num = int(input("> "))
    if num == 0:
        break
    else:
        faktoriyel(num)


###############################################################################
#%%
# lambda

liste = [1,2,3,4,5,6,7,8,9]

tekler = list(filter(lambda x : x%2 == 1 , liste))

print(tekler)

###############################################################################
#%%
# lambda

liste = [1,2,3,4,5,6,7,8,9]

kare = list(map(lambda x : x**2 , liste))

print(kare)

###############################################################################
#%%

liste = [1,2,3,1,4,5]

liste1 = [6,7,8,9]

liste.extend(liste1)  # liste + liste1
# [1,2,3,1,4,5,6,7,8,9]
liste.remove(1) # 1 elemanı silindi   # birden fazla ise ilki silinir   [1,2,1] --> [2,1]  
# [2,3,1,4,5,6,7,8,9]                                                    #
liste.pop(2) # 2. indeksdeki eleman silindi
# [2,3,4,5,6,7,8,9]
del liste[-1] # -1. indeks silindi
# [2,3,4,5,6,7,8]
liste.append(2) # liste sonuna 2 elemanı eklendi
# [2,3,4,5,6,7,8,2]
print(liste)


###############################################################################
#%%



###############################################################################
#%%



###############################################################################
#%%



###############################################################################
#%%



###############################################################################
#%%




###############################################################################
#%%



###############################################################################
#%%



###############################################################################
#%%

