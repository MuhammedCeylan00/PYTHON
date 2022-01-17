BDegeri = int(input("Baslangic degeri ne olsun: "))
SayiAdedi = int(input("Kac sayi olacak: "))
AsalListem = []


def AsalKontrol(Baslangic, Adet):
    while(1):
        sayac = 0
        kontrol = 0
        for i in range(2, Baslangic):
            if(Baslangic % i == 0):
                kontrol = 1
        Baslangic += 1
        if(kontrol == 0 and sayac <= Adet):
            sayac += 1
            AsalListem.append(Baslangic)
            if(sayac == Adet):
                break


AsalKontrol(BDegeri, SayiAdedi)
for x in AsalListem:
    print(x)
