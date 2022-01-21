#csomagok importálása
import os
#import keyboard
import time

#változók megadása

#A szám amit be kell olvasni
    #Kezdőértéke a None, mivel a while ciklusban ki tudom ezt használni az ismétlések vizsgálatára,
    #vagyis a ciklust mindaddig futtatjuk, míg a number változónak nem lesz szám értéke
number : int = None
#segéd változó, a beolvasott értéket fogja tárolni
data : str = ""

#while ciklus, ami mindaddig fog futni míg a number változó nem kap szám értéket, azaz az értéke nem None lesz
while(number == None):
    data = input("Kerem a szamot: ")
    #megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható e
    #mindegy hogy ez a szám int vagy float típusú
    #isdigit() -> bool változót ad vissza
    if(data.isdigit()):
        #ha az isdigit() függvény értéke igaz, akkor számot ír be a felhasználó
        #amit biztos át tudunk szám típussá alakítani
        number = int(data)
    #az isdigit() függvény értéke hamis, avagy a felhasználó nem számot írt be
    #így a number változó értéke továbbra is None marad, azaz a felhasználó nem számot írt be
    #ciklust ismételni kell
    else:
        print("\nNem szamot adott meg!")
        #a programot futtató szálat (thread) elaltatjuk 3 másodpercre
        time.sleep(3)
        #letöröljük a képernyőt
        os.system("cls")

        #print("\nA folytatashoz nyomjon meg az ENTER billentyut.")
        #egy végtelen WHILE ciklust írunk, mivel arra fogunk várni hogy a felhasználó
        #lenyomja a kért billentyűt (ENTER)
        #while(True):
            #figyeljük hogy a felhasználó lenyomta-e az ENTER gombot
        #    if(keyboard.is_pressed('enter')):
            #letöröljük a képernyőt
        #        os.system("cls")
                #kilépünk a (végtelen) while ciklusból
        #        break

#Kiírjuk a beolvasott számot
print(f"A beolvasott szam {number}")