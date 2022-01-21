import os
import time
import random

penz: int = 0
penzData: str = ""
uditoAr: int = 300
kivalasztottUdito: int = None
kivalasztottUditoData: str = ""
visszajaro: int = 0

while(penz == 0 or penz < uditoAr):
    penz+= random.randint(0, 200)
    print(f"Önnél {penz} Ft van jelenleg.")
    time.sleep(3)
    os.system("cls")

print("Elérhető üdítők: \n1 – Ice Tea \n2 - Limonádé \n3 - Epres jégkása \n4 - Almalé \n5 - Szénsavmentes ásványvíz")

while(kivalasztottUdito == None or kivalasztottUdito < 1 or kivalasztottUdito > 5):
    kivalasztottUditoData = print("Kérem a felsorolt üdítők közül válasszon!")
    if(kivalasztottUditoData.isnumeric()):




    