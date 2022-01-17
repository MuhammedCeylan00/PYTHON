for i in range(2, 600851475143):
    kontrol = 0
    if(600851475143 % i == 0):
        for j in range(2, i):
            if(i % j == 0):
                kontrol = 1
        if(kontrol == 0):
            print(i)
