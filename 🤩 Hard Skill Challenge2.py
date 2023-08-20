#EasyChallenge
Sayac = 0
Sayı = int(input("Bir Sayı Giriniz: "))
for i in range(2,Sayı):
    if Sayı%i == 0:
        Sayac += 1
        break
if Sayac == 0:
    print("Sayı Asaldır.")
else:
    print("Sayı Asal Değildir.")


#MediumChallenge
Girdi = str(input("Bir kelime giriniz: "))
print("Büyük harfli hali : ",Girdi.upper())

