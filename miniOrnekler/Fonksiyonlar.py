# def IsimYaz(isim,tekrar):
#     print(isim*tekrar)
# IsimYaz('Muhammed ',5)   


# def Sayilar(*arg):
#     print(list(arg))
# print(Sayilar(1,2,5,7,9)) 


# def AsalBul(say1,say2):
#     Sayac=0
#     for i in range(say1+1,say2):
#         Sayac=0
#         for j in range(2,i):
#             if i%j==0:
#                 Sayac+=1
#         if Sayac==0:
#             print(f"{i} sayisi asaldir.")        
                
# AsalBul(7,20)         


def TamBolenBul(Sayi):
    Listem=[]
    for i in range(1,Sayi+1):
        if Sayi%i==0:
            Listem.append(i)
    print(Listem)    
    
TamBolenBul(100)    