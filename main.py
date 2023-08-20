#🙌🏼 Easy: Kullanıcıdan alınan bir kelimenin uzunluğunu hesaplayan bir kod parçacığı yazar mısın?
Y= str(input("Bir Kelime Giriniz: "))
print(len(Y))
#🌟Medium:  Kullanıcıdan aldığınız bir sayının basamaklarının toplamını hesaplayan bir kod parçacığı yazar mısın?
X = input("Bir Sayı Giriniz:  ")
toplam = 0
for rakam in X:
    toplam += int(rakam)
print("Sayının Rakamları Toplamı: ", toplam)
#💪🏻Hard: Kullanıcıdan aldığınız bir metnin içindeki sesli harfleri sayan ve bunu kullanıcıya geri dönen bir kod parçacığı yazar mısın?
Z = input("Bir Metin Giriniz:")
sesli_harf = "AEIİOÖUÜaeıioöuü"
sayac = 0
for i in Z:
    if i in sesli_harf:
        sayac += 1
print("%s metnindeki sesli harf sayısı: %d" % (Z,sayac))
