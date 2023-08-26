
"""
Ders Programların isimlendirilmesi 
örnek :
S_1_1 = 1.sınıf 1. dönem
S_1_2 = 1.sınıf 2. dönem

"""


import random
import numpy as np
import csv

class Dersler:
    def __init__(self):
        
        self.S_1_1 = {
            
            "English" : [2,0,"ENG0101",60,"BAHATTİN ASLAN"],
            "Fizik I" : [3,2,"FZK0101",60,"Aslı Ayten Kaya"],
            "Matematik I" : [4,0,"MAT0101",80,"EMEL AŞICI"],
            "Lineer Cebir " : [3,0,"MAT0103",60,"NİHAL ÖZDOĞAN"],
            "Introduction to Mechatronics Engineering"  : [2,0,"MCH0111",100,"Ahmet Fenercioğlu"],
            "Computer Programming I"  : [3,2,"MCH0113",80,"YILMAZYILDIZ KAYAARMA"],
            "Malzeme Bilimi" : [3,0,"MMM0291",80,"Mehmet Onur Genç"],
            "Türk Dili I" : [2,0,"TUD0101",100,"NİHAL ÖZCAN"]

            }

        self.S_1_2 = {
            
            "English II" : [2,0,"ENG0102",60,"BURAK AKYOL"],
            "Fizik II" : [3,2,"FZK0102",80, "Aslı Ayten Kaya"],
            "Bilgisayar Destekli Teknik Resim" : [2,2,"MAK0192",100,"Mehmet Onur Genç"],
            "Matematik II" : [4,0,"MAT0102",60,"Burhan Alveroğlu"],
            "Fundementals Of Electrical Circuits"  : [3,2,"MCH0112",80,"Ahmet Fenercioğlu"],
            "Computer Programming II"  : [3,2,"MCH0114",100," Saffet Vatansever"],
            "Türk Dili II " : [2,0,"TUD0102",60,"NİHAL ÖZCAN"]

            }
        
        self.S_2_1 = {
            
            "Atatürk İlkeleri ve İnkilap Tarihi I" : [2,0,"AİT0201",60,"Gökçe SÜZGÜN IŞIK"],
            "İş Sağlığı ve Güvenliği I" : [2,1,"İSG0201",60,"Derya İde"],
            "Diferansiyel Denklemler" : [4,0,"MAT0291",80,"NİHAL ÖZDOĞAN"],
            "Engineering Mechanics -Statics" : [3,0,"MECH0201",100],
            "Elektronik I"  : [2,2,"MKT0211",100,"Mustafa KOCAKULAK"],
            "Mantık Devreler"  : [3,2,"MKT0213",80,"Ahmet Remzi ÖZCAN"],
            "Sayısal Yöntemler" : [3,0,"MKT0215",60,"Burhan Alveroğlu"],
            "Sosyal Seçmeli Ders/Social Elective Course (Grup A)" : [2,0,"SOS/SECIII",80]

            }
        
        self.S_2_2 = {
            
            "Atatürk İlkeleri ve İnkilap Tarihi II" : [2,0,"AİT0202",60,"Gökçe SÜZGÜN IŞIK"],
            "İş Sağlığı ve Güvenliği II" : [2,0,"İSG0202",60,"Derya İDE"],
            "Mühendislik Matematiği" : [3,0,"MAT0292",100,"Gökhan GELEN"],
            "Control Systems I" : [3,0,"MCH0212",60,"Üyesi Ekrem DÜVEN"],
            "Engineering Mechanics -Dynamics "  : [3,0,"MECH0204",80,"Mehmet Onur GENÇ"],
            "Elektronik II"  : [2,2,"MKT0212",100,"Oğuz MISIR"],
            "Termodinamik" : [3,0,"MKT0214",60,"Mustafa ÇOBAN"],
            "Sosyal Seçmeli Ders/Social Elective Course (Grup B)" : [2,0,"SOS/SECIV",80]

            }
        
        self.S_3_1 = {
            
            "Control Systems II" : [3,0,"MCH0311",80,"Fatih ONAY"],
            "Electric Machines and Energy Conversion" : [2,2,"MCH0313",60,"Ahmet FENERCİOĞLU"],
            "Measurement Techniques and Instrumentation" : [2,2,"MCH0315",80,"Mert YILMAZ"],
            "Mikroişlemci Tabanlı Sistem Tasarımı" : [2,2,"MKT0311",100,"Oğuz MISIR"],
            "Makine Elemanları" : [3,0,"MKT0313",60,"Özgür ALTINIŞIK"],
            }
        
        self.S_3_2 = {
            
            "Mekatronik Mühendisliğinde Tasarım" : [0,4,"MKT0401",60,"Nurettin Gökhan ADAR"],
            "Robot Kinematiği ve Dinamiği" : [3,0,"MKT0403",60,"İsmail ÖZTÜRK"],

            "Digital Signal Processing" : [3,0,"MCHE0301",80,"Ahmet FENERCİOĞLU"],
            "Communication Systems" : [3,0,"MCHE0302",60,"Murat PEKER"],
            "Digital Control Systems" : [3,0,"MCHE0303",80,"Ahmet Remzi ÖZCAN"],
            "Güç Elektroniği" : [3,0,"MKTS0301",80,"Gökhan GELEN"],
            "Programlanabilir Denetleyiciler"  : [3,0,"MKTS0302",100,"Ahmet MERT"],
            "Malzeme Mekaniği" : [3,0,"MKTS0303",100,"İsmail ÖZTÜRK"],
            "Hidrolik ve Pnömatik Sistemler" : [3,0,"MKTS0304",60,"Ekrem DÜVEN"],
            "Akışkanlar Mekaniği" : [3,0,"MKTS0305",60,"Saffet VATANSEVER"],
            "Algılayıcılar ve Dönüştürücüler"  : [3,0,"MKTS0306",80,"Nurettin Gökhan ADAR"],
            "Yapay Sinir Ağlarına Giriş" : [3,0,"MKTS0307",100,"Fatih ONAY"],
            "İşletim Sistemlerine Giriş" : [3,0,"MKTS0308",60,"Selma YILMAZYILDIZ KAYAARMA"],

            
            }
        
        self.S_4_1 = {
            
            "Sektör Eğitimi" :  [5,0,"SEP0001",60,"Üyesi Mehmet Onur GENÇ"],

            "Kontrol ve Otomasyon Paketi" : [5,15,"MKTS0480",100,"Oğuz MISIR"],
            "Robot Teknolojileri Paketi" : [5,15,"MKTS0482",80,"İlhan TUNÇ"],
            "Makine ve İmalat Teknolojileri Paketi" : [5,15,"MKTS0484",60,"Mustafa KOCAKULAK"],
            "Otomotiv Teknolojileri Paketi" : [5,15,"MKTS0486",80,"Mert YILMAZ"],
            
            }
        

        self.S_4_2 = {
            
            "Bitirme Çalışması" :           [0,4,"MKT0402",60,"Fatih ONAY"],
            "Technical Elective Course" :  [3,0,"TECVIII",80,"Samet GÜL"],
            "Teknik Seçmeli Ders(2 Ders)" : [3,0,"TSDVIII",60,"Özgür ALTINIŞIK"],
            

            "Artifical Neural Networks and Intelligent System" : [3,0,"MCHE0401",80,"Oğuzhan KURNAZ"],
            "Operating Systems" : [3,0,"MCHE0402" ,60,"Ahmet FENERCİOĞLU"],
            "Finite Element Methods" : [3,0, "MCHE0403",100,"Murat PEKER"],
            "Computer Aided Design" : [3,0,"MCHE0404" ,80,"Ahmet Remzi ÖZCAN"],
            "Advenced Algorithms and Database Systems" : [3,0,"MCHE0405" ,60,"Gökhan GELEN"],
            "Internet Programming " : [3,0, "MCHE0406",80,"Ahmet MERT"],
            "Fuzzy Control" : [3,0, "MCHE0407",100,"İsmail ÖZTÜRK"],
            "Image Processing":[3,0,"MCHE0408" ,80,"Ekrem DÜVEN"],
            "Donanım Tanımlama Dilleri":[3,0,"MKTS0401" ,100,"Saffet VATANSEVER"],
            "Biyomekatronik ":[3,0, "MKTS0402",60,"Selma YILMAZYILDIZ KAYAARMA"],
            "Endüstriyel İletişim Sistemleri":[3,0,"MKTS0403" ,60,"Mehmet Onur GENÇ"],
            "Bilgisayar Destekli İmalat":[3,0,"MKTS0404" ,80,"Oğuz MISIR"],
            "Endüstriyel Robot Programlama":[3,0,"MKTS0405" ,100,"İlhan TUNÇ"],
            "Otomotiv Mekatroniği":[3,0,"MKTS0406" ,60,"Mustafa KOCAKULAK"],
            "Mikroelektromekanik Sistemler(MEMS)":[3,0,"MKTS0407",60,"Mert YILMAZ"],
            "Mekanizma Tekniği":[3,0, "MKTS0408",60,"Fatih ONAY"],
            "Mekanik Titreşimler":[3,0,"MKTS0409" ,80,"Oğuzhan KURNAZ"],
            
            }
        
        self.dönemler = {
                         "S_1_1" : self.S_1_1 ,
                        "S_1_2" : self.S_1_2,
                         "S_2_1":self.S_2_1 ,
                         "S_2_2": self.S_2_2,
                         "S_3_1":self.S_3_1 ,
                         "S_3_2":self.S_3_2 ,
                         "S_4_1":self.S_4_1 ,
                         "S_4_2": self.S_4_2
                         }



        
        

class Program:
    def __init__(self):

        self.hafta = {
            
            "Pzt" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },

            "Sal" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },
                    
            "Çar" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },

            "Per" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },

            "Cum" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },
            
            
            }
    
        




labaratuvar = {
        "G-368":60,
        "G-374":100
                }
ders1 = {
        "G-151":60,
        "E-347":80 ,
        "E-243":100
        }

labaratuvarlar = {
    
            "Pzt" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },

            "Sal" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },
                    
            "Çar" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },

            "Per" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },

            "Cum" : {"08.00" : [],
                     "09.00" : [],
                     "10.00" : [],
                     "11.00" : [],
                     "13.00" : [],
                     "14.00" : [],
                     "15.00" : [],
                     "16.00" : []
                     },
    
    
    }



  

ders_programları = {}
derslers = Dersler()

dersler = Dersler()
program = Program()

Kalan_dersler = {
    "S_1_1" : [],
    "S_1_2" : [],

    "S_2_1" : [],
    "S_2_2" : [],

    "S_3_1" : [],
    "S_3_2" : [],

    "S_4_1" : [],
    "S_4_2" : [],
}



for dönems in derslers.dönemler.keys():

    dönem = dersler.dönemler[dönems]


    ####################
    dönemler = [dönem,dersler.S_1_2]
    
    
    ####################

    günler = []
    while True:
        gün = random.choice(list(program.hafta.keys()))
        if gün not in günler:
            günler.append(gün)
        if len(günler) == 5:
            break

    

    for gün in günler:   # program.hafta.keys()
        for saat in program.hafta[gün].keys():
            stop = 0
            for ders in dönem.keys():
                
                if dönem[ders][0] > 0:
                    for i in ders1.keys():
                        if ders1[i] >= dönem[ders][3]:
                            if dönem[ders][0] > 0:
                                program.hafta[gün][saat] = [ders,i,dönem[ders][-1]] # [dönem[ders],i]
                                dönem[ders][0]-=1
                                #print(ders)
                                stop = 1
                                break
                elif dönem[ders][1] > 0:
                    for i in labaratuvar.keys():
                        if labaratuvar[i] >= dönem[ders][3]:
                            if dönem[ders][1] > 0 and labaratuvarlar[gün][saat] == []:
                                program.hafta[gün][saat] = [ders,i,dönem[ders][-1],"labaratuvar"] # [dönem[ders],i]
                                dönem[ders][1]-=1
                                labaratuvarlar[gün][saat] = 1
                                #print(ders)
                                stop = 1
                                break
                if stop ==1:
                    break
                #print(ders)
    counter = 0
    for gün in program.hafta.keys():
        for saat in program.hafta[gün].keys():
            if program.hafta[gün][saat] != []:
                counter+=1
               
    print(counter)

    
    ders_programları[dönems] = program

    dersler_listesi = []
    
    for dersler in derslers.dönemler[dönems].keys():
        dersler_listesi.append(dersler)

    ayarlanan_dersler = []

    for gün in program.hafta.keys():
        for saat in program.hafta[gün]:
            if program.hafta[gün][saat] != []:
                ayarlanan_dersler.append(program.hafta[gün][saat][0])
            
    dl = np.array(dersler_listesi)
    ad = np.array(ayarlanan_dersler)

    
        
    Kalan_dersler[dönems].append(np.setdiff1d(dl,ad))



    dersler = Dersler()
    program = Program()
    

    


     
   

for i in ders_programları.keys():
    #print(f"----------------------{i}-------------------------")
    with open(f"{i}.csv", "w", newline="") as f:
        yazıcı = csv.writer(f)
        yazıcı.writerow(['Ders', 'Hoca', 'Gün' , "Saat" , "Sınıf"])

        for gün in ders_programları[i].hafta.keys():
            yazıcı.writerow([' ', ' ', ' ' , " " , " "])
            yazıcı.writerow([" ", ' ', ' ' , " " , " "])
            for saat in ders_programları[i].hafta[gün].keys():
                if ders_programları[i].hafta[gün][saat] != []:
                    if ders_programları[i].hafta[gün][saat][-1] != "labaratuvar":
                        yazıcı.writerow([ders_programları[i].hafta[gün][saat][0], ders_programları[i].hafta[gün][saat][2], gün , saat , ders_programları[i].hafta[gün][saat][1]])
                    else:
                        yazıcı.writerow([f"{ders_programları[i].hafta[gün][saat][0]} - labaratuvar", ders_programları[i].hafta[gün][saat][2], gün , saat , ders_programları[i].hafta[gün][saat][1]])
                else:
                    yazıcı.writerow([' ', ' ', gün , saat , " "])
                #print(ders_programları[i].hafta[gün][saat],gün,saat)
        
        
        



        print(f"> {i} - {Kalan_dersler[i]}")