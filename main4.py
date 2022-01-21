print("Melyik a kedvenc filmje?")
kedvencFilm: str = str(input())

print("Ki rendezte a filmet?")
filmRendezo: str = str(input())

print("Mikor jelent meg a film?")
megjelenesiEv: int = int(input())

print("Ki a kedvenc szereplője?")
foSzereplo: str = str(input())

print(f"{megjelenesiEv}-ban {filmRendezo} rendezésében megjelent a/az {kedvencFilm} című film {foSzereplo} főszereplésével.")