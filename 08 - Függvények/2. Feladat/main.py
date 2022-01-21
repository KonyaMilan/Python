import time
import os

from inputlib import *

def udvozles(nev: str) -> None:
    print(f"Üdvözlöm {nev}.")

felhasznalo: str = nevBekeres()
udvozles(felhasznalo)