Sayi=int(input('Sayi girin:'))
sayac=0
for i in range(2,Sayi):
    if Sayi%i!=0:
        sayac=0
    else:
        sayac+=1

if sayac==0:
    print("Bu sayi asaldir.")        
else:
    print("Bu sayi asal değildir.")    