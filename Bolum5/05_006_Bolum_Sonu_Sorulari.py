#1 Harfler adıyla bir liste oluşturup içine ‘a’, ‘e’, ‘i’, ‘o’, ‘i’, ‘u’ elemanları kaydediniz. Bu listede i ve pharflerinin sayısını ekrana yazdırınız.
harfler = ['a', 'e', 'i', 'o', 'i', 'u']
count = harfler.count('i')
print('i harflerinin sayısı:', count)
count = harfler.count('p')
print('p harflerinin sayısı:', count)
'''
i harflerinin sayısı: 2 
p harflerinin sayısı: 0
'''
#2 Liste1, liste2, liste3 ve liste4 adında dört adet liste oluşturup aynı satırda olacak şekilde tanımlayıp,
#her bir listeye birer adet eleman girip listeleyiniz.
liste1,liste2,liste3,liste4= ['a',100,3.14,'python']
print(liste1)
print(liste2)
print(liste3)
print(liste4)
''' 
a
100
3.14
python
'''
#3 İki adet liste tanımlayarak bu iki listeyi “+” operatörü ile toplama işlemi yaptırılıp, üçüncü bir listeye
#atama işlemini yapınız. Son listeyi ekrana yazdırınız.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#['a', 'b', 'c', 1, 2, 3]
##4 Aşağıdaki listeyi hem küçükten büyüğe hem de büyükten küçüğe doğru sıralanacak şekilde ekrana listeleyiniz.
#liste = [34,1,56,334,23,2,3,19]
liste = [34,1,56,334,23,2,3,19]
liste.sort()
print('küçükten büyüğe doğru',liste)
liste.reverse()
print('büyükten küçüğe doğru',liste)
''' 
küçükten büyüğe doğru [1, 2, 3, 19, 23, 34, 56, 334]
büyükten küçüğe doğru [334, 56, 34, 23, 19, 3, 2, 1]
'''
#5
'''
küçükten büyüğe doğru [1, 2, 3, 19, 23, 34, 56, 334]
büyükten küçüğe doğru [334, 56, 34, 23, 19, 3, 2, 1]
'''
listem= ["Merhaba", "Türkiye", "Nasılsın", "Tebrikler"]
print(listem[-1])
print(listem[-3])
print(listem[-4])
''' 
Tebrikler
Türkiye
Merhaba
'''
#6
''' 
Tebrikler
Türkiye
Merhaba
'''
liste = [1, 2, 3, 4, 5, 6, 7]
print(liste[1:3])
print(liste[:3])
print(liste[3:])
print(liste[:])
''' 
[2, 3]
[1, 2, 3]
[4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]

'''
#7

'''
Aşağıda verilen örnekte boş kalan kısımları doldurunuz.
isimler = ['ali','veli','ayşe']
……………………………………………………..
ad_soy1 = isimler[0] +' '+ soyisimler[0]
……………………………………………………………
ad_soy3 = isimler[2] +' '+ soyisimler[2]
print(ad_soy1)
………………………….
print(ad_soy3)
ali türk
veli izci
ayşe erel
'''
isimler = ['ali','veli','ayşe']
soyisimler = ['türk','izci','erel']
ad_soy1 = isimler[0] +' '+ soyisimler[0]
ad_soy2 = isimler[1] +' '+ soyisimler[1]
ad_soy3 = isimler[2] +' '+ soyisimler[2]
print(ad_soy1)
print(ad_soy2)
print(ad_soy3)
''' 
ali türk
veli izci
ayşe erel
'''

#8
''' 
liste = ['bir','iki','dört']
print(liste)
['bir', 'iki', 'dört'] şeklinde ekran çıktısı olmaktadır. Ama ['bir', 'iki', 'üç',
'dört', 'beş'] olacak şekilde listeyi güncelleyiniz.
'''
liste = ['bir','iki','dört']
liste[2]='üç'
liste.insert(3,'dört')
liste.insert(4,'beş')
print(liste)
#['bir', 'iki', 'üç', 'dört', 'beş']

##9
''' 
Aşağıdaki listede listenin ilk ve son verilerine ulaşmak ve listelemek için gerekli kodları yazınız.
liste=["birinci veri", "ikinci veri", "üçüncü veri ", "dördüncü veri",
"beşinci veri"]
'''
liste=["birinci veri","ikinci veri","üçüncü veri ","dördüncü veri","beşinci veri"]
#beş elemanlı listenin ilk verisi
print(liste[0])
#beş elemanlı listenin son verisi
print(liste[4])
#birinci veri