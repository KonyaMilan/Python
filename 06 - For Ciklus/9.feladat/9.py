print("kezdőérték =")
kezdoertek:int = int(input())

print("végérték =")
vegertek:int = int(input())


if(kezdoertek%2 != 0):
    kezdoertek-=1

for i in range (vegertek,kezdoertek,-1):
    print(i)
           