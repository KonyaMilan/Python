import os
import time
import random

#asd = random.randint(60, 90)

parosszam: int = None
parosData: str = ""
parostavolsaga: int = 0
parosneggyeloszthato: int = 0
paratlanszam:int = None
paratlanData: str = ""
paratlantavolsaga: int = 0
paratlanneggyeloszthato: int = 0
atlag: int = 0

while(parosszam == None or parosszam % 2 == 1):
    parosData = input("Adjon meg egy páros számot:")
    if(parosData.replace("-", "").isnumeric()):
        parosszam = int(parosData)
        if(parosszam % 2 == 1):
            print("Páratlan számot adott meg!")
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

while(paratlanszam == None or paratlanszam <= parosszam):
    paratlanData = input(f"Adjon meg egy páratlan számot amely nagyobb {parosszam}-nál:")
    if(paratlanData.replace("-", "").isnumeric()):
        paratlanszam = int(paratlanData)
        if(paratlanszam <= parosszam or paratlanszam % 2 == 0):
            print(f"Nem páratlan számot adott meg / Nem {parosszam}-nál nagyobb számot adott meg!")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

rng: int = random.randint(parosszam, paratlanszam)
print(f"A gép generált egy {parosszam} és {paratlanszam} közti számot, ami {rng}")

for i in range(parosszam, rng, 1):
    parostavolsaga+= 1
    if(i % 4 == 0):
        parosneggyeloszthato+=1

for j in range(rng, paratlanszam, 1):
    paratlantavolsaga+= 1
    if(j % 4 == 0):
        paratlanneggyeloszthato+=1

if(paratlantavolsaga == parostavolsaga):
    print(f" A két szám egyenlő távolságra van {rng}-től ")
if(paratlantavolsaga < parostavolsaga):
    print(f"{paratlanszam} közelebb áll {rng}-hez/hoz, mint {parosszam}")
else:
    print(f"{parosszam} közelebb áll {rng}-hez/hoz, mint {paratlanszam}")

atlag = (parosszam + paratlanszam) / 2
print(f"A két szám átlaga {atlag}")
print(f"{parosszam} és {rng} között {parosneggyeloszthato} szám osztható 4-el.")
print(f"{paratlanszam} és {rng} között {paratlanneggyeloszthato} szám osztható 4-el.")