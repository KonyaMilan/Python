import os
import time

number : int = None
data : str = ""

while(number == None or number < 0 or number > 9):
    data = input("Kérek egy számot 0-9 között: ")
    if(data.replace("-", "").isnumeric()):
        number = int(data)
        if(number != None and (number < 0 or number > 9) ):
            print("\nNincs megfelelő szám!")
            time.sleep(3)
            os.system("cls")
        
    else:
        print("\nNem egy 0-9 közé eső számot adott meg!")
        time.sleep(3)
        os.system("cls")

print(f"a Beolvasott szám {number}")

