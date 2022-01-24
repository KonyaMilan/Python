import time
import os

def hiba(uzenet: str)->None:
    print(uzenet)
    time.sleep(3)
    os.system("cls")

def pontBekeres()->int:
    pontSzam: int = None
    while(pontSzam == None):
        data: str = input("Kérem a pontszámot:")
        if(data.isdigit()):
            pontSzam = int(data)
            if(pontSzam >= 0 and pontSzam <= 0):
                return pontSzam
            else:
                pontSzam = None
                print("0 és 100 közötti értéket adjon meg!")
        else:
            hiba("Nem számot adott meg!")

def vizsgalat(szam: int)-> int:
    if(szam < 50):
        return 1
    elif(szam >= 50 and szam < 60):
        return 2
    elif(szam >= 60 and szam < 70):
        return 3
    elif(szam >= 70 and szam <80):
        return 4
    else:
        return 5

def kiiratas(pontSzam: int, osztalyzat: int)-> None:
    print(f"Ön {pontSzam} pontot ért el, az eredménye pedig {osztalyzat}.")

pontSzam: int = pontBekeres()
osztalyzat: int = vizsgalat(pontSzam)
kiiratas(pontSzam, osztalyzat)