# https://docs.python.org/3/library/functions.html built in function


# print("hello world")
# print("my name mahmud code")

# name = "mahmud code"
# print("maho" in name)

# x = 5
# y = -x

# print(x)
# print(y)

# a = 3.15
# b = -0.2

# print(a)
# print(b)

# age1 = age2 = age3 = 18 
# print(age1)
# print(age2)
# print(age3)

# name, age, school = "mahmud", 18, "code"
# print(name)
# print(age)
# print(school)

# isim = "mahmud code"
# mesaj = "Hello World"

# print(isim)
# print(mesaj)

# mesajim = f"senin adin galiba {isim} ve bunu demek istiyosun {mesaj}"
# print(mesajim)

# mesajim1 = f"senin a digerin galiba {a:.2f}'mi"
# print(mesajim1)

# dogru_mu = True
# yanlis_mi = False

# print(dogru_mu)
# print(yanlis_mi)

# meyveler = ["elma", "muz", "cilek"]
# print(meyveler)

# print(meyveler[0])
# print(meyveler[1])
# print(meyveler[2])

# koordinat = (3, 5)
# print(koordinat)

# ogrenci = {"isim": "Mahmud", "yas": 18, "not": "kaldi mal"}
# print(ogrenci)
# print(ogrenci.keys())
# print(ogrenci.values())

# renkler = {"kirmizi", "yesil", "mavi", "siyah"}
# print(renkler)

# in - not in
# g = 5
# if g > 4:
#     print("g 4ten buyuk")

# h = 10
# if h > 10:
#     print("h 10dan kucuk")
# else:
#     print("h 10a esit")

# j = 9
# if j > 9:
#     print("j 9den kucuk")
# elif j < 9:
#     print("j 9dan buyuk")
# else:
#     print("j 9a esit")

# sebze = ["domates", "sogan", "patates"]
# for meyve in sebze:
#     print(meyve)

# sayac = 1
# while sayac <= 5:
#     print(sayac)
#     sayac += 1

# def merhaba():
#     print("merhaba")

# merhaba()

# def selamla(isim):
#     print("selam " + isim + "!")

# selamla("mahmud")

# def kare(x):
#     return x * x

# print(kare(4))

# isim1 = "Mahmud"
# print(type(isim1))

# age = 18
# print(type(age))

# dogru = True
# print(type(dogru))

# yaklasik = 4.33323
# print(type(yaklasik))

# first_name = "Mahmud"
# last_name = "Code"
# full_name = first_name + " " + last_name
# print(full_name)
# print("your age is " + str(age))
# print("are you human : " + str(dogru))
# print(len(full_name))

# x = 0
# print("merhaba"+ x)
# str(x)
# print("merhaba", x)

# #strings method (string fonksıyonlari)
# name = "Mahmud Code"
# print(name) 
# print(len(name))
# print(name.find("a")) 
# print(name.capitalize())
# print(name.upper())
# print(name.lower()) 
# print(name.isdigit()) 
# print(name.isalpha()) 
# print(name.count("m"))
# print(name.replace("h", "h")) 
# print(name*2) 


# name = input("lutfen isimini gir ")
# age = int(input("lutfen yasini gir "))
# er = bool(input("eger erkeksen true yazarmisin ")) 
# print(name, age, er)

# #math kutuphanesi
# import math  # matematiksel fonksiyonları içeren bir modül

# pi = 3.14
# x = 1
# y = 2
# z = 3
# print(round(pi)) 
# print(math.ceil(pi)) 
# print(math.floor(pi)) 
# print(abs(pi)) 
# print(pow(pi,2))
# print(math.sqrt(pi)) 
# print(min(x,y,z)) 
# print(max(x,y,z))

# isim = "mahmud"
# print("merhaba",isim)
# print("merhaba",end=isim)


# #[start:stop:step] (indexing)
# name = "mahmud code"

# first_name = name[::-1]
# print(first_name)

# #(sagdan,soldan) slice
# yo_name = slice(3,-2)
# print(name[yo_name])

#list 

# ages = [18, 87, 97, 5, 3, 8, 6, 9, 4, 3, 2, 1, 43, 23, 65, 84] 
# food = ["hamburger", "hotdog", "pizza", "coffee", "soda", "tea", "ice cream", "cake"]

# for i in ages: 
#     print(i, end=" ")
# print()
# for j in food:
#     print(j, end=" ")
# print()

# print(ages) 
# print(food)

# ages[1] = 12 
# food[5] = "wafer"

# print(ages[1])
# print(food[5])


# drinks = ["tea", "soda", "coffe", "fruit juice"]
# foods = ["wafer", "hotdog", "pizza"]
# prices = [4, 2, 6, 1, 5]
# tasty = [False, False, True, True, True, False]
# classm = ['a', 'b', 'c']
# drinks.append("energy drink") #listeye yenı eleman ekler
# drinks.remove("tea") # listeden bir eleman siler
# drinks.pop()#son elemanı listeden siler
# drinks.insert(0, "cake") #listeye istenilen yere eleman ekler
# drinks.sort() #listeyi eger integer bir listeyse onun kucukten buyuge sıralar eger string bir listeyse onu alfabetık sılaramasına gore sıralar
# drinks.clear() #Bir listenin içindeki tüm öğeleri kaldırmak için kullanılır.
# kopya = drinks.copy() # Bir listenin kopyasını oluşturmak için kullanılır.
# print(kopya) #kopyalanan elemanları ekrara yazar
# drinks.index("tea") #listenin belirlenen elemanını yerini yani index yerini belirler
# kac = drinks.count("soda")#Belirli bir değere sahip olan öğelerin sayısını bulmak için kullanılır.
# print(kac)
# drinks.extend(foods) #bir listenin sonuna başka bir listenin öğelerini ekler
# print(drinks)
# drinks.reverse()#Bir listenin öğelerini tersine çevirmek için kullanılır.
# uzunluk = len(drinks)
# print(uzunluk)
# minimum = min(prices) #Bir listenin en küçük öğesini bulmak için kullanılır.
# print(minimum)
# maksimum = max(prices) #Bir listenin en büyük öğesini bulmak için kullanılır.
# print(maksimum)
# toplam = sum(prices)#Bir listenin öğelerinin toplamını bulmak için kullanılır.
# print(toplam)
# sonuc = any(tasty) # Bir listenin içinde en az bir doğru (True) değer içeren bir öğe olup olmadığını kontrol etmek için kullanılır.
# print(sonuc)
# sonuc = all(tasty)#Bir listenin içindeki tüm öğelerin doğru (True) değerler olduğunu kontrol etmek için kullanılır.
# print(sonuc)
# for indeks, deger in enumerate(classm): #Bir listenin öğelerini hem değerleriyle hem de indeksleriyle döndürmek için kullanılır.
#     print(indeks, deger)
# karistir = list(zip(tasty, classm))# Birden fazla listenin öğelerini eşleştirerek yeni bir liste oluşturmak için kullanılır.
# print(karistir)
# sirali = sorted(prices) #Bir listenin öğelerini sıralamak için kullanılır. Orijinal liste üzerinde değişiklik yapmaz, sıralanmış bir kopya döndürür.
# print(sirali)
# terssirali = list(reversed(prices)) #  Bir listenin öğelerini ters sırada döndürmek için kullanılır. Orijinal liste üzerinde değişiklik yapmaz, ters sırada bir kopya döndürür
# print(terssirali)


#2D list

# egg = [[1,2,3,4,5],[5,6,7,8,9]]
# #print(egg[1][4])

# drinks = ["tea", "soda", "coffe", "fruit juice"]
# foods = ["wafer", "hotdog", "pizza","pasta"]
# prices = [4, 2, 6, 1]

# all = (drinks,foods, prices)
# print(all[1][3])

# tuple #
# koordinat = (18,"mahmud","code",'AA')
# print(koordinat)

# print(koordinat.count("mahmud"))
# print(koordinat.index(18))

# for ben in koordinat:
#     print(ben)

# if "mahmud" in  koordinat:
#     print("1yes you are here ")
# else:
#     print("1no you are not here")

# ben = {"ben",34,"sen","o ", "bu",18,True,'A',3.212}
# print(ben)

# koordinat = set(("benma",2))
# print(koordinat)

# renkler = {"kirmizi","yesil","mavi"}

# for x in renkler:
#     print(x)

#key:value
 #1:40:12
 
#set
# koordinat = set(("benma",2))
# print(koordinat)
 
#food = {"pasta", "cake", "chicken"}
# food.add("joke")
# food.remove("pasta")
# food.clear()
# for x in food:
#     print(x)
     
#name = {"mahmud", "code", "bro", "ko", "cake"}
# food.update(name)
# all = food.union()
# for x in all:
#     print(x)
#print(food.difference(name))
#print(food.intersection(name))

#dictionary


# ulke = {'KW': 12,
#         'TR': 10,
#         'PS': 2,
#         'SY': 1,}

# ulke.update({'JP':3})
# ulke.pop('KW')
# ulke.clear()
# print(ulke.keys())
# print(ulke.values())
# print(ulke['KW'])
# print(ulke.get('TR'))
# print(ulke.items())
    
# for key,values in ulke.items():
#     print(key, values)

#index op [] islower

# def add(*sayi):
#     sayi = list(sayi) 
#     sayi[0] = 0 # ilk elemani 0 yapma
#     sonuc = 0
#     for arg in sayi:
#         sonuc += arg
#     return sonuc

# # Fonksiyonu çağırırken farklı sayıda argümanlar iletebilirsiniz
# print(add(1, 2, 3))  # Çıktı: 6
# print(add(4, 5, 6, 7))  # Çıktı: 22

#devamını yap
#print("hello {} how are you?".format("mahmud")) 
    

#random

# import random
# list = [1,2,3,4,5,6,7,8,9,10]
# x1 = random.random() #0 ile 1 arasinda rastgele bir ondalık sayı uretır
# x2 = random.randint(1,6) # belirli bir aralikta rastegle sayi uretir 
# x3 = random.choice(list) # liste icinden rastegele bir eleman secme
# x4 = random.sample(list,2) # bir listeden num kadar rastegle eleman alma 
# x5 = random.shuffle(list)  # liste elemanlarını karıstırma 
# x6 = random.seed(2,43)

# print(x1,x2,x3,x4,x5,x6)

#  raise ValueError
#  except ValueError try
#  as
#
#

#file işlemleri




# oop


