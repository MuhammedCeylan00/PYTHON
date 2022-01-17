MuhammedHesap={
    'ad':'muhammed',
    'soyad':'CEYLAN',
    'HesapNo':'1112345',
    'Bakiye':3000,
    'EkHesap':4000
}

def ParaCek(Hesap,miktar):
    if (Hesap['Bakiye']>miktar):
        print("paranizi alabilirsiniz.")
        Hesap['Bakiye']-=miktar
    elif (Hesap['Bakiye']+Hesap['EkHesap']>miktar):
        EkHesapKullanimi=input('Bakiyeniz yetersiz.Ek hesap kullanilsinmi?(e/h)')
        if EkHesapKullanimi=='e':
            Hesap['Bakiye']=0
            Hesap['EkHesap']-=(miktar-Hesap['Bakiye'])
            print("Paranizi alabilirsiniz.")
        else:
            print(f"{Hesap['HesapNo']} nolu hesabinizda {Hesap['Bakiye']} bulunmaktadir.")    
                
def ParaYatirma(Hesap,miktar):
    Secim=input('Hangi hesabiniza para yatirmak istersiniz?(Normal/ek)...')
    if Secim=='Normal':
        Hesap['Bakiye']+=miktar
        print(f"Normal hesap bakiyeniz {Hesap['Bakiye']} olarak guncellendi.")
    elif Secim=='ek':
        Hesap['EkHesap']+=miktar
        print(f"Ek hesap bakiyeniz {Hesap['EkHesap']} olarak guncellendi.")
    else:
        print("Lutfen gecerli secim yapiniz....")




ParaYatirma(MuhammedHesap,5000)
