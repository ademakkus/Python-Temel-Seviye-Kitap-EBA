liste = [1,2,3,4,5,6,7,8,9,10]
print(liste)
# 1. eleman
print(liste[0])
# 6. eleman
print(liste[5])
# Baştan 5. indekse kadar (dahil değil)
print(liste[:5])
# 1.indisten 5.indise kadar
print(liste[1:7])
print(liste[5:])
print(liste[::2])
''' 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
1 7
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 6, 7]
[6, 7, 8, 9, 10]
[1, 3, 5, 7, 9]
'''
liste = [ "merhaba", "dünya", "merhaba", "güle güle" ]
print (liste [- 1 ]) #son ögeyi listeler
print( liste [- 3 ]) #sondan üçüncü ögeyi listeler
print(liste [- 4 ]) #sondan dördüncü ögeyi listeler
print(liste[::-1]) #sondan başa doğru listeleme yapmak için kullanılır
''' 
güle güle
dünya
merhaba
['güle güle', 'merhaba', 'dünya', 'merhaba']

'''