from matematikaifuggvenyek import *
from io import *

def tizedesSzamBeolvasasa(a:str)->float:
    szam:int=None
    while(szam==None):
        beolvasottSzam=input(f"{a}")
        if(beolvasottSzam.replace("-","").replace(".","").isdigit()):
            number=int(beolvasottSzam)
            return number
        else:
            print("Nem számot adott meg!")
            time.sleep(3)
            os.system("cls")
            
            
def nevBekeres() -> str:
    nev: str = None

    while(nev == None):
        data: str = input("Kérem a nevét: ")


        if(len(data) < 3):
            print("Túl rövid a név, min 3 karakter")
            time.sleep(3)
            os.system("cls")
        else:
            nev = data 

    return nev