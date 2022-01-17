def Asalmi(sayi):
    kontrol=0
    for i in range(2,sayi):
        if(sayi%i==0):
            kontrol=1
    if(kontrol==1):
        return False
    else:
        return True
toplam=0
for i in range():#,57,8,9,10
    if(Asalmi(i)==True):
        toplam+=i
print(toplam)
