import random
import os
import time

start:int= None #kezdőértéke a kitalálandó számnak
end:int = None #végérték
titkos:int = None #maga a szám


#szám beolvasása határértékek közt
def szamBeolvasasa(kezdoErtek:int, vegErtek:int, szoveg:str)-> int:
    eredmeny:int = None

    while(eredmeny== None):
        data:str=input(f"Kérem adjon meg egy számot {kezdoErtek} és {vegErtek} között: ")       
        if(data.isnumeric() and int(data) >= kezdoErtek and int(data) <= vegErtek):   
            eredmeny = int(data)
            return eredmeny
        elif(data.isnumeric and int(data) < kezdoErtek or int(data) > vegErtek):
            print("A szám nem esik bele a  tartományba!")    
        else:
            print("Nem jó számot adott meg!")

#a random szám legenerálása
def random(kezdoErtek:int, vegErtek:int)->int:
    return random.randint(kezdoErtek, vegErtek)

#tipp bekérése
def tippBeolvasasa()-> int:
    eredmeny:int = None

    while(eredmeny== None):
        data:str=input("Kérem adjon meg egy tippet: ")       
        if(data.isnumeric()):   
            eredmeny = int(data)
            return eredmeny
        elif(data.isnumeric and int(data) < kezdoErtek or int(data) > vegErtek):
            print("A szám nem esik bele a  tartományba!")    
        else:
            print("Nem jó számot adott meg!")

#kitalálás kiírása
def sikeresTipp(probalkozasokSzama:int, szam:int)-> None:
    print(f"Nagyszerű, kitalálta a {szam} számot ennyi próbálkozás után {probalkozasokSzama}!")

#találgatások kiírása
def sikertelenTipp(tipp:int, szam:int)-> None:
    if(tipp > szam):
        print(f"A kitalálandó szám kisebb a tippnél.")
    else:
        print(f"A kitalálandó szám nagyobb a tippnél.")

def jatek(tipp:int)-> None:
    probalkozasokSzama:int = 0
    tipp:int= None

    while(tipp != szam):
        tipp: int = tippBeolvasasa()
        probalkozasokSzama += 1
        if(tipp == szam):
            sikeresTipp(probalkozasokSzama, tipp, szam)
        else:
            sikertelenTipp(tipp, szam)
    

#főprogram
start = szamBeolvasasa(0,9)
end = szamBeolvasasa(40,50)
titkos = random(start,end)

jatek(titkos)