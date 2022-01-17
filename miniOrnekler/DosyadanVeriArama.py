a = (" [17372.544441]")
bulunanlar = ()
with open("ipTables.log") as file:
    for line in file:
        if line in a:
            bulunanlar += line
if bulunanlar:
    with open("bulunanlar.txt", "w") as file:
        for i in bulunanlar:
            file.write(i + "\n")