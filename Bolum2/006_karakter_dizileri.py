'''
####################################################
Karakter dizisi, kullanıcıdan alınan değerlerin metin
formatında tutulduğu veri tipleridir. Python karakter
dizisi oldukça kullanışlı işlevlere sahiptir.

Bir karakter dizisi ekrana yazdırılabilir, başka bir karakter dizisiyle birleştirilebilir.
“len( )” metodu bir karakter dizisinin uzunluğunu vermektedir
##############################################
'''
metin1 = 'Merhaba '
metin2 = 'Mars'
print (metin1) # karakter dizisinin tamamını yazar
print (metin1 * 2) # karakter dizisini 2 defa yazar
print (metin1 + metin2) # iki karakter dizisini birleştirir
print ('metin1 adlı değişkendeki değerin uzunluğu:', len(metin1))
#Boşluğun da bir karakter olduğunu gözden kaçırmayınız.