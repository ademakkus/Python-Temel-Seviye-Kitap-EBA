dosya = open('deneme.txt', 'w')
#if  dosya.exists():
 #   dosya = open('deneme.txt', 'w')
for i in range(3):
    no = input('numaranız:')
    ad = input('adınız:')
    soyad = input('soyadınız:')
    dosya.write(f'{no} {ad} {soyad}\n')


dosya=open('deneme.txt','r')
veri=dosya.read()
sonuc=veri.split(' ')
print(sonuc)
for s in sonuc:
    for a in s:
        #print(a[0],a[1],a[2])
        print(a,sep=',')
print()
