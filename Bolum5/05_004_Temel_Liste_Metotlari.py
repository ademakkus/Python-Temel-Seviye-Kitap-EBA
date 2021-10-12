'''
Sıra No  Metot Adı   Görevi
1        ‘append’    Listeye yeni eleman ekleme işlemini yapar. Bu metot ile listeye sadece bir eleman eklenebilir ve eklenen eleman listenin sonunda yer alır.
2        ‘clear’ Listeyi değil içindeki tüm ifadeleri silmeye yarar.
3        ‘copy’ Listeden listeye kopyalama işlevine yaramaktadır.
4       ‘count’ Listenin içinde sorgulanan elemandan kaç adet olduğunu bulmamızı sağlar.
5       ‘extend’ Listeler arası genişletme işlevini görür.
6       ‘indis’ Listedeki elemanları almamızı sağlar.
7       ‘insert’ Listenin istenilen indis numarasına eleman eklenebilir.
8       ‘pop’  Listedeki elemanın indisi ile silme işlem yapar. indis belirtmediğinizde isevarsayılan olarak listenin son elemanını siler. Ayrıca bu metot silinen elemanı ekrana yazmaktadır.
9       ‘remove’ Listede istenilen elemanın değerini yazarak silme işlemi yarar.
10      ‘sort’ Listenin elemanlarını alfabetik olarak sıralar.
11      ‘reverse’ Bu metot sort metodunun aksine listedeki elemanları ters alfabetik olarak sıralar.
12      ‘del’ Liste içerisinden bir elemanı silmek için kullanılır. Silme işlemi indis numarasına göre yapılmaktadır.
'''
##append
takimlar=["gs","fb","bjk"]
takimlar.append("ts")
print(takimlar)
#['gs', 'fb', 'bjk', 'ts']
##insert
sebzeler =["lahana","marul","pırasa","ıspanak","fasulye"]
sebzeler.insert(2,"patlıcan")
print(sebzeler)
#['lahana', 'marul', 'patlıcan', 'pırasa', 'ıspanak', 'fasulye']
##copy
iller1 =["konya","karaman","kocaeli","kayseri","kahramanmaraş"]
iller2=[]
iller2 = iller1.copy()
print("İller 2 listesi")
print(iller2)
#['konya', 'karaman', 'kocaeli', 'kayseri', 'kahramanmaraş']
##count: öğenin listede kaç defa bulunduğunu döndürür.
takimlar = ['GS','FB','BJK','TS','FB','ÇS','ES','FB']
print(takimlar.count('FB'))
#3
##extend: extend komutu listelerdeki ögelerin kendi elemanlarını koruyarak genişletme işlemi yapar
kus1=["bıldırcın","papağan","kartal","akbaba","şahin"]
kus2=["baykuş","muhabbet"]
kus1.extend(kus2)
print(kus1)
#['bıldırcın', 'papağan', 'kartal', 'akbaba', 'şahin', 'baykuş', 'muhabbet']
##index:verilen bir ögenin indis numarasını vermektedir
sebzeler =["lahana","marul","pırasa","ıspanak","fasulye"]
print(sebzeler.index("ıspanak"))
##clear:liste elemanlarını siler
liste =["ayva","nar","kiraz","kayısı","Üzüm"]
liste.clear()
print(liste)
#[]
##pop:
sebzeler =["lahana","marul","pırasa","ıspanak","fasulye"]
sebzeler.pop(2)
print(sebzeler)
#['lahana', 'marul', 'ıspanak', 'fasulye']
print(sebzeler.pop())
#sebzeler.pop('ıspanak') # hata verir
print(sebzeler)

##remove:elemanı listeden siler
sehirler =["adana","ağrı","bursa","konya","ankara"]
sehirler.remove("konya")
print(sehirler)
#['adana', 'ağrı', 'bursa', 'ankara']
##reverse:
sayilar=[10,20,30,40,50,60,70]
print('---Normal Liste---')
sayilar.reverse()
print('---Ters Çevrilmiş Liste---')
print(sayilar)
#[70, 60, 50, 40, 30, 20, 10]

##sort
isimler=["elif","ayşe","kemal","kaan","hafsa"]
isimler.sort()
print(isimler)
##['ayşe', 'elif', 'hafsa', 'kaan', 'kemal']

##sort
takimlar = ['GS','FB','BJK','TS']
del takimlar[2]
print(takimlar)
#['GS', 'FB', 'TS']

##dir(list)
print(dir(list))
''' 
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__',
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy',
'count', 'extend', 'indis', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''