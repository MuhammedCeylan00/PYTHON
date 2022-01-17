def bul(sayi):
    if not isinstance(sayi, int):
        raise TypeError("sayi integer olmali")
    elif not sayi >= 0:
        raise ValueError("sayi sifirdan buyuk olmali.")

    def faktAl(sayi):
        if sayi <= 0:
            return 1
        else:
            return sayi*faktAl(sayi-1)
    return faktAl(sayi)


try:
    print(bul(13))
except Exception as ex:
    print(ex)
