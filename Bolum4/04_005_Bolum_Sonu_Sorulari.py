import null as null
#1
sayi=int(input('Bir sayı giriniz:'))
mesaj=null
if sayi<0:
    mesaj='NEGATİF'
elif sayi>0:
    mesaj = 'POZİTİF'
else:
    mesaj = 'SIFIR'
print('sayı '+mesaj+' dır.')
print(f'sayı {mesaj} dır.')
print('sayı {} dır.'.format(mesaj))
#2
not1=int(input("Birinci vize notunu giriniz:"))
not2=int(input("İkinci vize notunu giriniz:"))
final=int(input("Final notunu giriniz:"))
ortalama=(not1+not2+final)/3
print(f'Not ortalaması:{ortalama}')
if ortalama<50:
    print("KALDI")
else:
    print('GEÇTİ')

#3------
s1=int(input("Birinci sayıyı giriniz:"))
s2=int(input("İkinci  sayıyı giriniz:"))
if s1>s2:
    print('Birinci sayı büyüktür')
if s1<s2:
    print('İkinci  sayı büyüktür')
if s1==s2:
    print('İki  sayı EŞİTTİR')


#4------
s1=int(input("Birinci sayıyı giriniz:"))
s2=int(input("İkinci  sayıyı giriniz:"))
if s1>s2:
    print('Birinci sayı büyüktür')
elif s1<s2:
    print('İkinci  sayı büyüktür')
else:
    print('İki  sayı EŞİTTİR')

#5*----
sayi1=12
sayi2=60
toplam=0
if sayi1<=sayi2:
    if sayi1%2==0:
        sayi1=sayi2
        toplam=sayi1+sayi2
else: toplam=sayi2-sayi1
toplam+=toplam
print(toplam)
#240
#6*----
sayi1=40
sayi2=13
toplam=0
if sayi1<=sayi2:
    if sayi1%2==0:
        sayi1=sayi2
        toplam=sayi1+sayi2
else: toplam=sayi2-sayi1
toplam+=toplam
print(toplam)
#-54
#7*----
a=int(input("Mevsim No:"))
if(a==1):
    print("İlkbahar")
elif(a==2):
    print("Yaz")
elif(a==3):
    print("Sonbahar")
elif(a==4):
    print("Kış")
else: print("Aralıkta olmayan bir değer girdiniz")
''' Mevsim No: 2
Yaz

'''
#8*----
a=int(input("1. kenar:"))
b=int(input("2. kenar:"))
c=int(input("3. kenar:"))
d=int(input("4. kenar:"))
if(a==b==c==d):
    print("Kare!")
elif(a==c and b==d or a==b and c==d ):
    print("Dikdörtgen")
else: print("Diğer Dörtgen")
''' 
1. kenar:6
2. kenar:7
3. kenar:8
4. kenar:9
Diğer Dörtgen
'''
#9*-----
a=int(input("1. kenar:"))
b=int(input("2. kenar:"))
c=int(input("3. kenar:"))
if(a!=b and a!=c and b!=c):
    print("Çeşitkenar Üçgen!")
elif(a==b==c):
    print("Eşkenar Üçgen!")
else: print("İkizkenar Üçgen")
''' 
1. kenar:3
2. kenar:5
3. kenar:6
Çeşitkenar Üçgen!
'''
#10* ------
boy = float(input("Boy: Örnek 1.73----:"))
kilo = float(input("Kilo: Örnek: 78.40----:"))
endeks = kilo/(boy**2)
if endeks<18.5:
    print("Zayıfsınız")
elif endeks > 18.5 and endeks <=25 :
    print("Normalsiniz")
elif endeks > 25 and endeks <=30:
    print("Kilolusunuz")
elif endeks > 30:
    print("Dikkat! obez")
''' 
Boy: Örnek 1.73----:1.75
Kilo: Örnek: 78.40----:95
Dikkat! obez
'''

