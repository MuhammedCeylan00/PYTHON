
def geblo(n):
    gebloSayisi = 1
    liste = [1]

    for i in range(n):
        liste.append((gebloSayisi+1) * (gebloSayisi+2))
        gebloSayisi =(gebloSayisi+1) * (gebloSayisi+2)
    print(liste)


geblo(5)
