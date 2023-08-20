#🙌🏼 Easy: Kullanıcıdan aldığın sayının karesini hesaplayarak ekrana yazdıran kod parçacığını yazar mısın?
X = int(input("Lütfen Bir Sayı Giriniz: "))
print("Sayının Karesi: ",X**2)
#🌟Medium:  Oluşturduğunuz bir dizinin medyanını hesaplayan bir kod parçacığı yazar mısınız?
def median(lst):
    n= len(lst)
    if n <1:
        return
    if n %2 == 1:
        return print("Ortanca Terim:" ,sorted(lst)[n//2])
    else:
        return print("Ortanca Terim:" ,sum(sorted(lst)[n//2-1:n//2+1])/2)
lst = [2,3,4,1,3,5,7,8,5,7,5,4,3,2,7,8,9,9,7,5,4]
median(lst)
# 💪🏻Hard: Kullanıcıdan aldığınız bir sayının Armstrong sayısı olup olmadığını kontrol eden bir kod parçacığı yazar
# mısınız? (Armstrong sayısı: Basamaklarının üçüncü kuvvetinin toplamı, sayıya eşit olan sayılardır.)



def armstrong(sayı):
    toplam = 0
    for x  in basamak:
     rakam = int(x)**len(basamak)
     toplam += rakam
    if(sayı == toplam):
        print("Bu bir armstrong sayısıdır. ")
    else:
        print("Bu bir armstrong sayısı değildir. ")

sayı = int(input("Sayıyı Giriniz: "))
basamak = str(sayı)
armstrong(sayı)
