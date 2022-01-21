#1 - Írjunk programot amely összead, kivon, szoroz és eloszt két számot. 
#A matematikai műveleteket függvényekkel oldjuk meg.

from matematikaifuggvenyek import *

osszeg:float=None
kulonbseg:float=None
szorzat:float=None
hanyados:float=None
szam1:int=None
szam2:int=None
beolvasottSzam:str=""
 

 
szam1=tizedesSzamBeolvasasa("Kérem az első számot: ")
szam2=tizedesSzamBeolvasasa("Kérem a második számot: ")
 
osszeg=osszedas(szam1,  szam2)
kulonbseg=kivonas(szam1, szam2)
szorzat=szorzas(szam1, szam2)
hanyados=osztas(szam1, szam2)
 
print(f"A számok összege: {osszeg}\nKülönbsége: {kulonbseg}\nSzorzata: {szorzat}\nHányadosa: {hanyados}")
