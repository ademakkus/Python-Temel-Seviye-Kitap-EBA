dilekce="""
                                                                                                   tarih: {}
T.C.
{} ÜNİVERSİTESİ
{} Fakültesi Dekanlığına
Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede belirtilen mazeretim gereğince   {}  Eğitim-Öğretim Yılı {}  yarıyılında
 öğrenime ara izni (kayıt dondurma) istiyorum.

Gereğini bilgilerinize arz ederim.
imza
Öğrenci Bilgileri
-----------------
Ad              :{}
Soyad           :{}
TC Kimlik No    :{}
Adres           :{}
Telefon         :{}
Ekler           :{}
"""
tarih=input("tarih:")
universite=input("üniversite adı:")
fakulte=input("fakülte adı:")
bolum=input("bölüm adı:")
ogrenci_no=input("öğrenci no. :")
ogretim_yili=input("öğretim yılı:")
yari_yil=input("yarıyıl:")
adi=input("öğrencinin adı:")
soyadi=input("öğrencinin soyadı:")
tc_kimlik_no=input("TC Kimlik no. :")
adres=input("adres:")
tel=input("telefon:")
ekler=input("ekler:")
print(dilekce.format(tarih, universite, fakulte, bolum,
ogrenci_no, ogretim_yili, yari_yil, adi, soyadi, tc_kimlik_no,
adres, tel, ekler))
