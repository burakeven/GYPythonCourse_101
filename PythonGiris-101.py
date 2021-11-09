#SAYILAR VE STRINGLERE GIRIS
9+9
print(9+9)
print("Hello AI")
type("Hello AI Era") #içerisine yazılan değerin veya yazının tipini gösterir.

#STRINGLERE YAKINDAN BAKIS
123
type(123)
"123"
type("123")

"a" + "b"
"a"  " b"
"a" + "-b"
#"a"-"b" iki stringi çıkarma yapmaya çalışıyorsun, hatalı.

" a"*3 #3 tane a'yı yan yana yazar.

#STRING METODLARI-FONKSIYONLARI - len()
gel_yaz="gelecegi_yazanlar"
#del mvk - gel_yaz yerine mvk yazmıştım, onu sildim.

a = 9
b = 10

a*b

len(gel_yaz) #içine girmiş olduğum ifadenin boyutunu verir. Mesela gel_yaz degiskeni içerigi 17 olarak gösterir.
#STRING METODLARI - upper() & lower()
gel_yaz.upper()
gel_yaz.lower()

gel_yaz.islower()
B = gel_yaz.upper()
B.isupper()

#STRING METODLARI - replace()
gel_yaz.replace("e","a") #e harflerini a harfine çevirdim.
gel_yaz.replace("a","i")

#STRING METODLARI - strip() --Istenmeyen karakterleri kesmek için kullanılır.
gel_yaz1=" gelecegi_yazanlar "
gel_yaz1.strip() #bu kodla beraber gelecegi_yazanların sol ve sagindaki boslukları sildirdim.
gel_yaz1="*gelecegi_yazanlar*"
gel_yaz1.strip("*")

gel_yaz1="lgelecegi_yazanlarl"
gel_yaz1.strip("l")

#METODLARA GENEL BAKIS
gel_yaz="gelecegi_yazanlar"
dir(gel_yaz) #metodları gözlemleyebiliriz
gel_yaz.title() #Mesela bu method basliklari buyutur.
a=15
dir(a)


#SUBSTRINGS
gel_yaz="gelecegi_yazanlar"
gel_yaz[0] #g'i gösterir

gel_yaz[0:3] #0. Indeksten 3'e kadar alır, 3 dahil degil. : ifadesi ise;
#soldakinden sagdakine kadar secim yapmak anlamina gelir.
gel_yaz[3:7]

#DEGISKENLER
a=9
b="python_101"
c=a*2

b*2
a*2

type(1+2j)

#TYPE_CONVERSIONS
toplama1= input() #kullanıcıdan bilgi almak için kullanılır.
toplama2=input() 

type(toplama1)
toplama1+toplama2

int(toplama1)+int(toplama2)

int(11.2)

float(12)

type(str(12))

#print()
print("gelecegi_yazanlar")
print("gelecegi","yazanlar")
print("gelecegi","yazanlar",sep="_") #sep bir argümandır.

#print() #sol parantezi yazdığın gibi argümanları karşına çıkartır. 
#Aynı zamanda bu arg görme islemi sag üstteki blokta help alanında gözükür.

#?print #Detaylı özelliklerine buradan erişim sağlanır.



