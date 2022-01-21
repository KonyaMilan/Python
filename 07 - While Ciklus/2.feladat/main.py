#név nem lehet üres string
#szóközök (1 vagy több)
#név hossza (min: 3 karakter)
import os
import time

nev : str = ""

while(nev == "" or nev.isspace() or len(nev)<3 ):  
    print("Adja meg a nevét!")
    nev : str = str(input())

    if(nev == "" ):
        print("Nem adott meg nevet!")
        time.sleep(3)
        os.system("cls")

    elif(nev.isspace()):
        print("A névhez nem adhat meg szóközt!")
        time.sleep(3)
        os.system("cls")

    elif(len(nev) < 3):
        print("A névnek legalább 3 karakter hosszúnak kell lennie!")
        time.sleep(3)
        os.system("cls")   
    
print(f"Üdvözlöm {nev}!")
       

