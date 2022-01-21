suminput: str = ""
inputtext: str = ""
number: int = 0
proba: int = 0
osszeg: int = None
szum: int = 0

while(osszeg==None or osszeg < 100):
    suminput=input("Mit szeretne szumnak megadni?:")
    if(suminput.replace("-", "").isnumeric()):
        osszeg = int(suminput)
        if(osszeg < 100):
            print("Minimum 100 lehet a szum")
    else:
        print("Nem számot adott meg!")

while(szum < osszeg):
    inputtext=input("Kérek egy számot!:")
    if(inputtext.replace("-", "").isnumeric()):
        number = int(inputtext)
        szum += number
        proba += 1
        print(f"Az eddigi számok összege {szum}, a bevitelek száma {proba}")
    else:
        print("Nem számot adott meg!")
print(f"A végső érték: {szum}, {proba} próbálkozás után")