sonuc=0
for i in range(100,1000):
    for j in range(100,1000):
        sayi=i*j
        yeniSayi=(str(sayi)[::-1])
        yeniSayi=int(yeniSayi)
        if(sayi==yeniSayi):
            if(yeniSayi>sonuc):
                sonuc=yeniSayi
print(sonuc)













