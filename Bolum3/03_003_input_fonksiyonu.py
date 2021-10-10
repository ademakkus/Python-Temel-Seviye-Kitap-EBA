isim=input("isminizi giriniz: ")
print("merhaba! ",isim)
#isminizi giriniz: adem
#merhaba! adem
a=input("birinci sayıyı giriniz: ")
b=input("ikinci sayıyı giriniz: ")
print("girdiğiniz sayıların toplamı: ",a+b)

'''birinci sayıyı giriniz: 6
ikinci sayıyı giriniz: 8
girdiğiniz sayıların toplamı: 68
'''
a=int(input("birinci sayıyı giriniz: "))
b=int(input("ikinci sayıyı giriniz: "))
print("girdiğiniz sayıların toplamı:",a+b)
'''
birinci sayıyı giriniz: 5
ikinci sayıyı giriniz: 8
girdiğiniz sayıların toplamı: 13
'''
on_mesaj="Sayın "
mesaj_sonu=" nisan dönemi faturaınız: "
abone_no=input("abone numaranız")
tuketim=input("tuketim miktarı")
tuketim_tutari=int(tuketim)*4.0
mesaj=on_mesaj+abone_no+mesaj_sonu+tuketim+" tl dir."
print(mesaj)
'''
abone numaranız: 123456
tuketim miktarı: 20
Sayın 123456 nisan dönemi faturaınız: 20 tl dir.
'''