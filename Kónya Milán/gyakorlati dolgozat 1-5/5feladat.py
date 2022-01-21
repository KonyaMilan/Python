print("a=")
a : int = int(input())

print("b=")
b : int = int(input())

print("c=")
c : int = int(input())

print("d=")
d : int = int(input())

szorzat : float = (a + b) * c

kulonbseg : float = szorzat - d

eredmeny : float = kulonbseg % 7

print(f" {szorzat} - {d} = {kulonbseg}")
print(f" A {kulonbseg} % 7 művelet maradéka {eredmeny}")
