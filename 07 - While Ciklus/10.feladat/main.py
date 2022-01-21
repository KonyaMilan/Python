import os
import time

n: int = None
nData: str = ""
ottelOszthato: int = 0
szamokSzama: int = 0

while(n==None or n > 99 or n < 0):
    nData = input("Adjon meg egy maximum 2 jegyű pozitív számot:")

    if(nData.replace("-","").isnumeric()):
        n = int(nData)

        if(n > 99 or n < 0):
            print("Rossz számot adott meg!")
            time.sleep(3)
            os.system("cls")
print("A páros számok:")
for i in range(0, n+1, 1):
    if(i%2 == 0):
        print(f"{i}", end=" ")
    if(i%5 == 0):
        ottelOszthato+=1
    if(i%11 == 0):
        szamokSzama+=1
print(f"\nAz öttel osztható számok száma: {ottelOszthato}")
print(f" A 11-el osztható számok száma: {szamokSzama}")
print("A 7-el osztott számok, melyeknek a maradéka 3:")
for j in range(0, n+1, 1):
    if(j%7 == 3):
        print(f"{j}", end=" ")