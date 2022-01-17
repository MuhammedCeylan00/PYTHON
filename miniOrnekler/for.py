sayilar=[1,3,5,7,9,12,19,21]

# for i in sayilar:
#     if(i%3==0):
#        print(i)


# toplam=0
# for i in sayilar:
#     toplam+=i
    
# print(toplam)

# kare=0
# for i in sayilar:
#     if(i%2!=0):
#         kare=i*i
#         print(kare)

# Sehirler=['Kocaeli','istanbul','ankara','izmir','rize']

# for i in Sehirler:
#     if(len(i)<=5):
#         print(i)

Urunler=[
    {'name':'Samsung S6','price':'3000'},
    {'name':'Samsung S7','price':'4000'},
    {'name':'Samsung S8','price':'5000'},
    {'name':'Samsung S9','price':'6000'},
    {'name':'Samsung S10','price':'7000'}
]

# Toplam=0
# for key in Urunler:
#     Toplam+=int(key['price'])
# print(Toplam) 


for key in Urunler:
    if (int(key['price'])<=5000):
        print(key)