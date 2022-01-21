print("x =")
x: float = float(input())

print("y =")
y: float = float(input())

print("z =")
z: float = float(input())

print("q =")
q: float = float(input())

osszeg: float = (x + y)
kulonbseg: float = (z - q)

eredmeny: float = osszeg / kulonbseg

print(f" {osszeg} / {kulonbseg} = {eredmeny}")