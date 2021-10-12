'''
#############################
split( ) metodu, listeyi belirtilen ayıracı kullanarak yeniden döndürmeye yarar. Yani split( ) karakter
dizilerini istenen şekilde böler. -ayırıcı diye tanımladığımız ilk parametre, karakter dizisinin nereden bö-
lüneceğini seçer.Dosya ve veritabanı işlemlerinde
sıkça kullanılır.
#############################
'''
bilgi=input("bilgilerinizi araya virgül koyarak yazınız: ")
liste=bilgi.split(",")
print(liste)
''' 
bilgilerinizi araya virgül koyarak yazınız: Hafsa,Meva,Konya,1
['Hafsa', 'Meva', 'Konya', '1']
'''
cumle="23 nisan herkese mutlu olsun"
kelimeler=cumle.split(" ")      #list e dönüştü
print("cümlenizde ",len(kelimeler),"adet kelime vardır")
#cümlenizde 5 adet kelime vardır