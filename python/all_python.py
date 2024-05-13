print("HELLO WORLD") # herhangi bir ifadeyi konsola yazdirmak icin print fonkıyonu kullanilir string bir ifade ise cift tirnak integer bir ifadeyse tirnak kullanilmaz
# string(str) degiskenleri
first_name = "mahmud"# sting bir ifade degiskeni tanımlamak ıcın  cift tirnak yada tek tirnak kullanılır
last_name = 'code'# sting bir ifade degiskeni tanımlanır
full_name = first_name + " " + last_name# sting ifadelerde degiskenlerin bir biriyle toplanabilir ve bir baska degiskene atanabilir
print(first_name)# bir degiskeni  konsola yazdirmak icin gene print kullanılır (her hangi bir ifade degisken integer character vs konsola yazdirmak icin print kullanılır)
print(type(first_name))# bir degiskenin veri tipini konsola yazdirmak icin type fonkıyonu  kullanılır
print("Hello " + full_name)# burda hem bir string ifade hemde string bir degisken birlikte konsola yazdirildi
#ok
# F (string)
isim = "mahmud code"
yas = 18

# f-string kullanarak bir dize biçimlendirme
mesaj = f"Benim adım {isim} ve ben {yas} yaşındayım." #f cift tırnak ıcınde bir degisken yazdırılabilir
print(mesaj)

x = 3.14159

# Biçimlendirme seçenekleriyle birlikte f-string kullanarak
mesaj = f"x değeri yaklaşık olarak {x:.5f}'dir."
print(mesaj)

# integer (int)
age = 18 #integer bir degisken tanımlanır
age += 1 # burda age degiskenini 1 artirdik
print("your age  = " + str(age))  # burda print fonkıyonunda + operatoru kullanırken eger bir string ifade ve ineteger bir degisken varsa yanında o integer degiskeni bir string bir ifadeye cevrimen lazım yada  "+" yerine  "," operatorunu kullanılabilir
print(type(age)) # bir degiskenin veri tipini konsola yazdirmak icin type fonkıyonu  kullanılır

#float (float)

weight = 75.4  #double bir degisken tanımlanır
print("merhaba ", full_name, "senin boyun ", weight)# burda yukardaa oldugu gibi string bir ifadeye cevirmedik cunku , operatoru kullanıldı
print(type(weight)) # bir degiskenin veri tipini konsola yazdirmak icin type fonkıyonu  kullanılır

#boolean (bool)
human = True # bool bir degisken tanımlanır
women = False # bool bir degisken tanımlanır
print("your are human : "+ str(human))
print("your are a women : " + str(women))
print(type(human)) # bir degiskenin veri tipini konsola yazdirmak icin type fonkıyonu  kullanılır
print(type(women)) # bir degiskenin veri tipini konsola yazdirmak icin type fonkıyonu  kullanılır

#coklu atama
name, age, school = "mahmud", 18, "code"# burda 3 degiskenı tek bir satirda tanımlandı
print(name)
print(age)
print(school)

age1 = age2 = age3 = 18  # burda 3 degısken aynı oldugu ıcın  = operatoru ıle ısıtlendı gene 3 satir  yerine tek satirda tanımlandı
print(age1)
print(age2)
print(age3)


#strings method (string fonksıyonlari)

name = "Mahmud Code"
print(name) # string bir ifadeyi bir sey degıstırmeden yazar
print(len(name)) # string dizisindeki karakter sayisini yazdirir
print(name.find("a")) # belirlenen karakterin index numarasını yazdirir
print(name.capitalize()) # string ifadedeki ilk harfi buyuk harfe cevirir (bosluk varda ıslemez sadece ılk harfi cevirir)
print(name.upper()) # string bir ifadeyi butun karakterlerını buyuk harfe ceviri
print(name.lower()) # string bir ifadeyi butun karakterlerini kucuk harf yapar
print(name.isdigit()) # integer bir ifade olup olmadına gore true yada false yazdırır
print(name.isalpha()) # alfabetik karakterler olup olmadına gore true yada false yazdirir (yani string dizisi sadece alfabetik karakterler icermeli bosluk virgil vesayre ıcermemelı)
print(name.count("m")) # burda belırlenen bir karakterin kac kere yazildigni gosteriri
print(name.replace("h", "h")) # burda belirlenen bir karakterin yerine gececek deger bir karakter belırlenir
print(name*2) #burda istenilen miktarda degiskeni yazdirir

# type casting ( bir degerin veri tipini baska bir veri tipine cevirmek)

x = 1 # integer bir deger
y = 3.0 #float bir deger
z = "6" # string bir deger

print(x)
print(y)
print(z*2)#z charaterini 2 kere yazar

x = float(x) # x yanı integer olan degsikenin floata donusturme
y = str(y) # y yani float olan degiskenin stringe  donusturme
z = int(z) # z yani string olan degiskenin integera donusturme

print(x)
print(y)
print(z*2) # yukarda bir integere cevirildigi icin ikiye carpar

#input  in python

name = input("what is your name ?: ") #kullanıcıdan giris istemek icin input fonskıyonu kullanılır
print("Hello ", name)
age = int(input("how old are you ?: ")) # burda bir integer deger almak icin basa veri turunu yazdik cunku input fonskıyonu her zaman string deger alır kullanıcıdan baska veri turu istenirse fonksıyonun basına belırtmelıdır
print("you are " + str(age) + " years old" )
height = float(input("how tall are you")) #burda bir flout deger almak icin input fonksıyonu kullanıldı ve float oldugnu belırtıldı
print("you are " + str(height) + " cm tall")
human = bool(input("are you human or women( true/false)")) #burda bir bool deger alındı (hangı veri turunde ise basa yazilmali)
print(human)

#random in python

import random

random.seed(1)# zamani kontrol eder her calıstırıldıgında aynı sonucu vermemesi icindir (birden fazla yazılabilir)
x = random.randint(1,6) # 1 ile 6 sayisina kadar olan sayilarini temsil eder
#print(x)

y = random.random() #cikti buyuk bir kesirli sayiyi temsil eder
#print(y)


list = ['one','two','three','four']# bir liste tanımlama
z = random.choice(list)#bir listenin elemanlari arasinda rastgele(random) bir sayi tanımlar
#print(z)

list2 = ['i','he','she','it','you','we','they']
random.shuffle(list2) #tanımlanan bir listin elemanlarını karıstırır
#print(list2)

list3 = ['i','love','you']
l = random.sample(list3,3)#tanımlı bir listeyi elemanlarını karıstıran ve sonra hepsını yazdirmak ıcındir
#print(l)

#randrange(start,stop,step) bunalara bak
#random.uniform()
#random.expouariate()
#random.gauss()
#getstate
#getstate(state_obj)
#getrandbits(k)



#math kutuphanesi
import math  # matematiksel fonksiyonları içeren bir modül


pi = 3.14
x = 1
y = 2
z = 3
print(round(pi)) #degiskeni en yakın tam sayıya yuvarlar
print(math.ceil(pi)) #degiskeni en buyuk tam sayiya yuvarlar
print(math.floor(pi)) # degiskeni en kucuk tam sayiya yuvarlar
print(abs(pi)) #degiskenin mutlak degerini yazdiri
print(pow(pi,2)) #degiskenin girilen sayi kac kuvveti alınır
print(math.sqrt(pi)) #degiskenin karekoku alırnır
print(min(x,y,z)) # yazilan degiskenlerin minumum olanini yazdirir
print(max(x,y,z)) #yazilan degiskenlerin maxımum olanini yazdirir


# string ifade dilimleme
#[start:end:step]

name = "mahmud code"

first_name = name[:6] #  [0:5] yani ilk indexten 5 nci indexe kadar yazdiri
print(first_name)
last_name = name[7:] # 7 inci ındexten baslar ve sonun akadar yazdirir
print(last_name)
dual_name = name[::2] # ikiser ikiser yazdirir
print(dual_name)
reverse_name = name[::-1] #tersten yazdirir
print(reverse_name)

website = "http://www.google.com/"
website2 = "http://www.wikipedia.com/"

slice = slice(11,-5) #slice fonskıyonu belirili indexleri silip yazdirir

print(website[slice])
print(website2[slice])

#karar yapilari

me = bool(input("how are you are you mahmud write True are you  not write False"))
if me == bool(False): # kosul yapsıdır eger ifin ıcındekı kosul saglanmassa elif varsa o kod calısır eger yoksa else in altindakı kodlar calısır
    print("you are not mahmud ?") # ustekı kosul saglanırsa calısacak kod
elif me == bool(True): #ifin saglanmadıgı surece calısır (birden fazla kullanılır)
    print("you are mahmud :)") # ilk if calısmassa calısacak kod
else: #ne ifin nede elifin saglanmadıgı surece calısır
    print("how is you ?") # hıc bir kosul saglanmassa calısacak kod


#mantik operatorler (and,or,not)

age = int(input("yasinizi girin"))
if age>=17 and age <= 24: # and operatoru iki kosulunda saganması gerek eger saglanmassa else blognu calıstırır
    print("sen 17 ile 24 yasindasin") #ustekı ıkı kosulunda saglandıgnda calısacak olan kod
else: # ifin icindekı kosullar saglanmadıgı surece calısır
    print("sen 24 ten buyuksun")

name = str(input("ismini yada nicknameini gir"))
if name == "Mahmud" or name == "masterx": # or operatoru ikinin saglanmassi gerekmez sadece bir kosul saglanırsa calısır
    print("merhaba " + name) #if saglanırsa calısacak kod
else: # ifin icndekı ıkı kosulda saglanmassa calisacak olan kod
    print("sen mahmud degilsin")
    print("sen masterx degilsin")

#loops
#while loop

name = ""  # bos bir stirng ifade tanımlama

while len(name) == 0:  # while loop kosulun saglandıgı surece calısır ve altındakı kodu hep calıstırır
    name = str(input("adini gir")) #yukardakı kosul saglandıgı surece calısacak kod
    print("gir lan ismini") #kosul saglandıgı surece calısacak kod
print("merhaba " + name) #while dongunun ıcınde olmadıgı icin dongunun bitirminde calısacak kod

#for loop
#for looplarda degiskenin altında yazilan her kod o loopa aittir eger her hangi bir kodda bir sapma olursa for looptan cıkar
import time #zamanla ilgili fonksiyonları içeren bir modül

for i in range(10): #for eleman in aralik ve bu dongu 0 ıle 9 arası deger dondurur
    print(i + 1) # for dongusu calıstıgı haldı yazilcak kod
# for dongusu start degri 0 ıse direk stop degeri yazilabilir ama step degeri varsa strat degri tanımlanmalı
name = "mahmud code"
for i in name:  #bu dongu name degiskenin icindeki her elemanı tek tek yazdirir
    print(i)

for i in range(0,20,2): # range(start, stop +, step) range tanımlanmıs bir sayi listesidir
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) #bu sleep fonskıyonu zamanı bir sanıyelıgne dondurur
print("happy new year!")

list = {1,24,6,8,5,4,3,5} #sonra
for i in list: # bu for loopu listteki butun elemanları tek tek yazdirir
    print(i)

#ic ice donguler
satir = int(input("satir sayisini gir"))
sutun = int(input("sutun sayisini gir"))
isaret = str(input("isareti giriniz "))

for i in range(satir): # ılk for (for dongulerınde  degiskenin altında olan her seyılk fora aittir)
    for j in range(sutun): # ikinci for (degiskenin altindaki her kod ikinci fora aittir)
        print(isaret, end="  ")# end parametresı print fonskıyonu bıttıgnde sonunda eklenıcek her hangi bir seyi sonuna ekler
    print()


# break = calıstıgnda anında kodu sonlandırır yada bir dongunun veya kosul yapısında ıse anında onu sonlandırır
# continue = calıstıgnda kodun yada kosul veya dongunun basına atar
# pass = calıstıgnda eger kosul yapsında ıse o kodu pas gecer

name = ""
while name != "mahmud":
    name = str(input("adini dogru gir"))
    if name == "code":
        break # bu kodda eger kullanıcı code yazarsa while dongusunden cıkar

phone = "0535-282-86-46"
for i in phone:
    if i == "-":
        continue # burda eger i degiskeni - karakterını gosterırse onun uzerinden atlar ve kod basa doner
    print(i, end="")  #yani bu kodu calıstırmaz

for i in range(1,100):
    if i%2==0:
        pass# burda ustekı kosul saglandıgı surece pas gecer saglanmassa else calısısr
    else:
     print(i)



# list

ages = [18, 87, 97, 5, 3, 8, 6, 9, 4, 3, 2, 1, 43, 23, 65, 84] # list boyle yazilir [] arasında yazilir bu integer bir listedir
food = ["hamburger", "hotdog", "pizza", "coffee", "soda", "tea", "ice cream", "cake"] # string bir listede boyle tanımlanır
for i in ages: #bu metodla liste yazdirilir
    print(i, end=" ")
print()
for j in food:
    print(j, end=" ")
print()

print(ages) #yada boylede liste ekrana yazdirilir
print(food)

ages[1] = 12 #bir listeye belirli  bir elemani degistirir
food[5] = "wafer"

print(ages[1]) #bir listede belirli elemani yazdirir
print(food[5])

#liste fonskıyonları (build fonction)

drinks = ["tea", "soda", "coffe", "fruit juice"]
foods = ["wafer", "hotdog", "pizza"]
prices = [4, 2, 6, 1, 5]
tasty = [False, False, True, True, True, False]
classm = ['a', 'b', 'c']
drinks.append("energy drink") #listeye yenı eleman ekler
drinks.remove("tea") # listeden bir eleman siler
drinks.pop()#son elemanı listeden siler
drinks.insert(0, "cake") #listeye istenilen yere eleman ekler
drinks.sort() #listeyi eger integer bir listeyse onun kucukten buyuge sıralar eger string bir listeyse onu alfabetık sılaramasına gore sıralar
drinks.clear() #Bir listenin içindeki tüm öğeleri kaldırmak için kullanılır.
kopya = drinks.copy() # Bir listenin kopyasını oluşturmak için kullanılır.
print(kopya) #kopyalanan elemanları ekrara yazar
drinks.index("tea") #listenin belirlenen elemanını yerini yani index yerini belirler
kac = drinks.count("soda")#Belirli bir değere sahip olan öğelerin sayısını bulmak için kullanılır.
print(kac)
drinks.extend(foods) #bir listenin sonuna başka bir listenin öğelerini ekler
print(drinks)
drinks.reverse()#Bir listenin öğelerini tersine çevirmek için kullanılır.
uzunluk = len(drinks)
print(uzunluk)
minimum = min(prices) #Bir listenin en küçük öğesini bulmak için kullanılır.
print(minimum)
maksimum = max(prices) #Bir listenin en büyük öğesini bulmak için kullanılır.
print(maksimum)
toplam = sum(prices)#Bir listenin öğelerinin toplamını bulmak için kullanılır.
print(toplam)
sonuc = any(tasty) # Bir listenin içinde en az bir doğru (True) değer içeren bir öğe olup olmadığını kontrol etmek için kullanılır.
print(sonuc)
sonuc = all(tasty)#Bir listenin içindeki tüm öğelerin doğru (True) değerler olduğunu kontrol etmek için kullanılır.
print(sonuc)
for indeks, deger in enumerate(classm): #Bir listenin öğelerini hem değerleriyle hem de indeksleriyle döndürmek için kullanılır.
    print(indeks, deger)
karistir = list(zip(tasty, classm))# Birden fazla listenin öğelerini eşleştirerek yeni bir liste oluşturmak için kullanılır.
print(karistir)
sirali = sorted(prices) #Bir listenin öğelerini sıralamak için kullanılır. Orijinal liste üzerinde değişiklik yapmaz, sıralanmış bir kopya döndürür.
print(sirali)
terssirali = list(reversed(prices)) #  Bir listenin öğelerini ters sırada döndürmek için kullanılır. Orijinal liste üzerinde değişiklik yapmaz, ters sırada bir kopya döndürür
print(terssirali)

#2D list 1:30




