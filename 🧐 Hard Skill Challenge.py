#🙌🏼 Easy: Kullanıcıdan aldığın iki sayının toplamını ekrana yazdıran bir kod parçacığı yazar mısın?
x = int(input("Bir Sayı Giriniz: "))
y = int(input("Bir Sayı Giriniz: "))
print("İki Sayının Toplamı: ",x+y)

#💪🏻Hard: Kullanıcının girdiği bir sayı karekökten çıkıyorsa çıktığı halini eğer çıkmıyorsa karekökten tam olarak çıkmıyor hata mesajı veren kod parçacığını yazar mısın?
import math
def tamkare(x):
    if float(math.sqrt(x)) == int(math.sqrt(x)):
        print("X Bir Tam Kare Sayı ")
    elif float(math.sqrt(x)) != int(math.sqrt(x)):
        print("X Bir Tam Kare Sayı Değil ")

tamkare(9)
