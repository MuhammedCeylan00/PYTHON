# boy ,kilo    kilo/boy2

boy = (input("boyunuzu giriniz(metre veya santimetre):"))
kilo = float(input("kilonuzu giriniz:"))

if(("." in boy)):
    boy = float(boy)
    KBI = kilo/(pow(boy, 2))
    print("metre olarak girilmis")
else:
    boy = float(boy)
    boy = boy/100
    KBI = kilo/(pow(boy, 2))
    print("cm olarak girilmis")

if(KBI <= 18.5):
    print(KBI)
    print("Normal olabilmen icin  "+str(18.5-KBI)+"alman lazim")
    print("zayıf")
elif(18.5 < KBI <= 24.9):
    print(KBI)
    print("normal")
elif(24.9 < KBI <= 29.9):
    print(KBI)
    print("Normal olabilmen icin  "+str(KBI-24.9)+"vermen lazim")
    print("Kilolu")
elif(29.9 < KBI <= 39.9):
    print(KBI)
    print("Normal olabilmen icin  "+str(KBI-29.9)+"vermen lazim")
    print("obez")
else:
    print(KBI)
    print("Aşırı obez")
