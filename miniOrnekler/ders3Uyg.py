
degiskenler = []


def hesapla(degisken):
    if isinstance(degisken, list):
        for ilkDiziElemanlari in degisken:
            hesapla(ilkDiziElemanlari)
    else:
        degiskenler.append(degisken)


degisken = [0, 1, 2, [2, 3, 4], [2, 6, 7, [2, 2], ], ]

ornekListe = [[['ahmet', 'mehmet', 'azra'],
               'turgut'], 'azra', 'zeynep', 'azra']
degisken
hesapla(ornekListe)

yeniDizi = set(degiskenler)

for a in yeniDizi:
    print(a, end=',')
