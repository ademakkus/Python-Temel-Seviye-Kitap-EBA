''':cvar
Python, her ne kadar veri tiplerini otomatik olarak verse
 de bir değişkenin veri tipini kontrol etmek ve
kullanım amacına göre değiştirmek gerekebilir.
Bir değişkenin veri tipini öğrenmek için “type( )” komutu
kullanılır.
'''
sayi1=5
sayi2=10.556
metin1="1"
#metin1 değişkenine tırnak içinde verilen sayının string
# tipinde bir değişkenolduğuna dikkat ediniz.
sayi3=4+5j
askerlikYaptiMi=True
#True doğru, 1, evet anlamındadır.
print ("1. değişkenin veri tipi: ", type(sayi1))
print ("2. değişkenin veri tipi: ", type(sayi2))
print ("3. değişkenin veri tipi: ", type(metin1))
print ("4. değişkenin veri tipi: ", type(sayi3))
print ("5. değişkenin veri tipi: ", type(askerlikYaptiMi))
listem=['Çınar', 24, 'Mühendis', True]
print ("6. değişkenin veri tipi: ", type(listem))
demet1=('Çınar', 24, 'Mühendis', True)
print ("7. değişkenin veri tipi: ", type(demet1))
sozluk={'adi': 'Çınar','yasi': 24, 'meslekUnvani':'Mühendis', 'askerlikDurumu': True}
print ("8. değişkenin veri tipi: ", type(sozluk))