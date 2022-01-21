import os
import time

number : int = None
data : str = ""

while(number == None or number < 0 or number > 99):
    data = input("Kérek egy számot 0-99 között: ")
    if(data.replace("-", "").isnumeric()):
        number = int(data)
        if(number != None and (number < 0 or number > 99) ):
            print("\nNincs megfelelő szám!")
            time.sleep(3)
            os.system("cls")
        
    else:
        print("\nNem egy 0-99 közé eső számot adott meg!")
        time.sleep(3)
        os.system("cls")

print(f"Az ön életkora {number}")

if(number >= 0 and number <=6):
    print("Maga egy gyerek")
elif(number >= 7 and number <= 18):
    print("Maga egy iskolás")
elif(number >= 19 and number <=65):
    print("Maga egy dolgozó")
elif(number > 65):
    print("Maga egy nyugdíjas")
