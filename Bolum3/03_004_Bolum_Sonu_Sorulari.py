'''
1.Ekrana “Merhaba Dünya” yazan programı yazınız.
2. Kullanıcıdan ismini alarak merhaba “Ali” şeklinde çıktı veren programı yazınız.
3. Girilen iki sayının toplamını bulan ve ekrana yazdıran programı yazınız.
4. Girilen iki sayının ortalamasını bulan ve ekrana yazdıran programı yazınız.
'''
#1.
print("Merhaba Dünya")
#2.
isim = input('İsminizi Girin : ')
print("Merhaba "+isim)
#3.
sayi1 = int(input('1. sayıyı girin: '))
sayi2 = int(input('2. sayıyı girin: '))
print("girdiğiniz sayıların toplamı: ",sayi1+sayi2)
#4.
sayi1 = int(input('1. sayıyı girin: '))
sayi2 = int(input('2. sayıyı girin: '))
print("girdiğiniz sayıların ortalaması: ",(sayi1+sayi2)/2)