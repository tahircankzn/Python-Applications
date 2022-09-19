#liste = ["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]

#liste2 = ["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l","ş","i","z","x","c","v","b","n","m","ö","ç"]



#secret = ["a","t","m","e","i","d"]
#secret2 = ["q","w","e","r","t","y"]


şifreleme_sırası = ""

newtext = ""

textindex = ""

kontrol_text = ""

def createtext(text,newtext,şifreleme_sırası,textindex,kontrol_text):
    for i in text:
        if i in secret:
            index = secret.index(i)
            değişen = secret2[index]
            newtext = newtext + değişen
            jarvis = "{}{}".format(secret2[index],index)  # anahtar kullanım indexsi
            şifreleme_sırası = şifreleme_sırası + jarvis
            kontrol_text = kontrol_text + i
            

            textindex = textindex + str(len(kontrol_text) - 1) + "-"

        else:
            newtext = newtext + str(i)
            kontrol_text = kontrol_text + i

    #print(şifreleme_sırası)
    print("text index : {}".format(textindex[0:-1]))  #  [0:-1] sonradan eklendi
    #print(text)
    print(newtext)
    


    pass
def breaktext():
    input_text = text # şifrelemiş metin                                                                     qweosfrr        atmosfer
    text_değişim = input("please enter text index : ") # şifrelenmiş metindeki değişen harflerin index i     0-1-2-6
    text_değişim = list(text_değişim.split("-"))       #                                                     0 1 2 6   ilk buna göre for başlat
    key1 = input("plese enter key 1 : ") # şifrelerken kullanılan anahtar 1                                  atmeid    ['a', 't', 'm', 'e', 'i', 'd']
    key2 = input("plese enter key 2 : ") # şifrelerken kullanılan anahtar 2                                  qwerty    ['q', 'w', 'e', 'r', 't', 'y']
    #keyindexlist = input("please enter key input :") # anahtarların kullanıldığı indexler                   q0w1e2r3

    yeni_metin = ""
    metin_index = 0

    for i in input_text:
          
        
        if str(metin_index) in text_değişim:   # str(input_text.index(i))
            key2_index = key2.index(i)
            key1_index = key1[key2_index]
            yeni_metin = yeni_metin + key1_index
            metin_index += 1
        else:
            metin_index += 1
            yeni_metin = yeni_metin + i
            


    pass
    print(yeni_metin)


########################
text = input("please enter your message : ")

print("if you want to coding your message please enter --> 1\nif you want to break your message please enter --> 2")

choice = input("your choice : ")

if choice=="1":
    
    secret = input("please enter key1 : ")
    secret2 = input("please enter key2 : ")
    #print("your keys : \n{} key 1\n{} key 2".format(secret,secret2))
    
    createtext(text,newtext,şifreleme_sırası,textindex,kontrol_text)
elif choice == "2":
    breaktext()
    pass



