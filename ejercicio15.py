ahorro = 1 
dias = 0

while ahorro < 10000:
    ahorro *= 2
    dias += 1

    if dias % 10 == 0:
        print(f"Pasaron estos dias {dias}: y tienes = {ahorro}")