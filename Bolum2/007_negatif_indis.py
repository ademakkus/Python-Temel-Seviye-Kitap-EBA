'''
Karakter dizisine sondan başlandığını ifade eder. metin[-1] karakter dizisinin
en sonundaki karakteri verir. metin [-2] ise sondan ikinci karakteri verir.
Karakter dizilerinde indisler ritmik atlanarak dilimleme yapılabilir.
Bunun için [başlangıç indisi: bitiş indisi: ritmik artış miktarı] şeklinde kullanılır. “metin[0:8:2]” : 0’dan başlayarak 0, 2, 4 ve 6 indis numaralı
karakterleri dilimler.
'''
metin='Merhaba Mars'
print (metin[0]) # ifadenin ilk karakterini yazar.
print (metin[4:7]) # ifadenin 5, 6 ve 7. karakterlerini yazar.
print (metin[8::]) # 9. karakterden sonuncu karaktere kadar yazar.
print (metin[-2]) # karakter dizisinin en sondan ikinci karakterini yazar.
print (metin [:7]) # indisi 0' dan 7'ye kadar olan (7 dahil değil) karakterleri yazar.
print (metin[8:]) # başlangıç indisinden sonra tüm karakterleri yazar.
print(metin[0:8:2]) # 0, 2, 4 ve 6 indis numaralı karakterleri dilimler.