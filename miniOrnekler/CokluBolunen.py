def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd(b%a,a)

n=int(input("N degerini giriniz: "))
ekok=1
for i in range(2,n+1):
    ekok=(ekok*i)/gcd(ekok,i)
print(ekok)




