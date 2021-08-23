sayi1=int(input('sayi 1 girin:'))
sayi2=int(input('sayi 2 girin:'))

#Asal sayı sadece kendisi ve 1e bölünür
sayac=0
for i in range(sayi1+1,sayi2):
    sayac=0
    for j in range(2,i):#i=5
        if(i%j==0):
            sayac=1
    if(sayac==0):
        print(i)


