print("x = ")
x:int = int(input())

maradek:int = x % 4
maradek2:int = x % 6 

if(maradek == 0 and maradek2 == 0):
    print("a szám osztható 4-el és 6-al")
else:
    print("a szám nem osztható 4-el és 6-al")