import os
import time
import random

megtakaritottPenz: float = None
megtakaritottPenzData: str = ""
honapokSzama: int = 4

while(megtakaritottPenz == None or megtakaritottPenz > 100000 or megtakaritottPenz < 50000):
    megtakaritottPenz = input("Mennyi megtakarított pénze van?:")
    if(megtakaritottPenzData.replace("-", "").isnumeric()):
        megtakaritottPenz = float(megtakaritottPenzData)
        if(megtakaritottPenz < 50000 or megtakaritottPenz > 10000):
            print("Túl kevés/sok a megtakarított pénze!")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

while(megtakaritottPenz < 50000):
    megtakaritottPenz = megtakaritottPenz * 1.02
    honapokSzama+=1

print(f"{honapokSzama} hónap után lett a banki pénze 100.000 Ft 2%-os kamattal.")

    
