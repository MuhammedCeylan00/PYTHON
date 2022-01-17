# Fibonacci dizisindeki her yeni terim, önceki iki terimin eklenmesiyle
# oluşturulur.
# 1 ve 1 ile başlayarak, ilk 10 terim şöyle olacaktır:

# 1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# Fibonacci dizisindeki değerleri dört milyonu geçmeyen terimleri
# dikkate alarak çift değerli terimlerin toplamını bulunuz.

terimBir = 1
terimIki = 1
toplam = 0

for i in range(4000000):
    terimUc = terimBir+terimIki
    if(terimUc % 2 == 0):
        toplam += terimUc
    terimIki, terimBir = terimUc, terimIki
print(toplam)
