import os
import time

szum: int = 0
text: str =""
num: int = 0
proba: int = 0

while(szum < 100):
    text = input("Kérem a számot!")
    if(text.replace("-","").isnumeric()):
        num = int(text)
        szum+=num
        proba+=1
        print(f"{szum}, próbaszám: {proba}")
    else:
        print("Nem írt be számot!")
print(f"A szám {szum} lesz {proba} próba után.")