# plakalar={'kocaeli':41,'istanbul':34}

# print(plakalar['istanbul'])

# UYGULAMA
Ogrenciler={}
number=int(input("ogrenci no:"))
name=input("isim:")
surname=input("soyad:")
phone=input("ogrenci telefon:")

Ogrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})

number=int(input("ogrenci no:"))
name=input("isim:")
surname=input("soyad:")
phone=input("ogrenci telefon:")

Ogrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})
number=int(input("ogrenci no:"))
name=input("isim:")
surname=input("soyad:")
phone=input("ogrenci telefon:")

Ogrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon':phone
    }
})

OgrNo=int(input("bilgi icin ogr no girin:..."))
ogrenci=Ogrenciler[OgrNo]
print(ogrenci)
