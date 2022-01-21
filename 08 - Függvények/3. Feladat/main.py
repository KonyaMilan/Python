import datetime
import time
import os

felhasznaloNev: str = None
szuletesiEv: int = None
kor: int = None

#nev bekérése
def nevBeolvasasa() -> str:
    eredmeny: str = None
    while (eredmeny == None):
        data: str = input("Kérem a nevét:")
        if(len(data) > 3):
            eredmeny = data
            return eredmeny
        else:
            print("Túl rövid nevet adott meg!")
            time.sleep(3)
            os.system("cls")
#születési év bekérése
def szuletesiEvBekerese() -> int:
    eredmeny: int = None
    ma: datetime = datetime.datetime.now() # a mai dátumot adja vissza
    jelenlegiEv: int = int(ma.strftime("%Y")) #visszaadja a jelenlegi évet a dátumból
    while(eredmeny == None):
        data: int = input("Kérem adja meg a születési évét:")
        if(data.isnumeric()):
            eredmeny = int(data)

            if(eredmeny >= jelenlegiEv):
                eredmeny = None
                print("A születési év nem lehet nagyobb mint a jelenlegi év!")
                time.sleep(3)
                os.system("cls")

            return eredmeny
        else:
            print("Nem megfelelő születési évet adott meg!")
            time.sleep(3)
            os.system("cls")
#életkor kiszámítása
def eletkorKiszamitasa(ev: int) -> int:
    ma: datetime = datetime.datetime.now()
    jelenlegiEv: int = int(ma.strftime("%Y"))

    return jelenlegiEv - ev

#kiíratás
def kiiratas(nev: str, ev: int) -> None:
    print(f"{nev} ön az idén {ev} éves.")

#főprogram
felhasznaloNev = nevBeolvasasa()
szuletesiEv = szuletesiEvBekerese()

kor = eletkorKiszamitasa(szuletesiEv)

kiiratas(felhasznaloNev, kor)