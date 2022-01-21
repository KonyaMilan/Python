print("x =")
x: int= int(input())
print("y =")
y: int= int(input())
print("z =")
z: int= int(input())

if(x>y and x>z and y>z):
    print(f"{z}, {y}, {x}")
elif(x>y and x>z and z>y):
    print(f"{y}, {z}, {x}")
elif(y>x and y>z and x>z):
    print(f"{z}, {x}, {y}")
elif(y>x and y>z and z>x):
    print(f"{x}, {z}, {y}")
elif(z>x and z>y and x>y):
    print(f"{y}, {x}, {z}")
elif(z>x and z>y and y>x):
    print(f"{x}, {y}, {z}")
elif(x==y and x>z):
    print(f"{z}, {x}, {y}")
elif(x==z and x>y):
    print(f"{y}, {x}, {z}")
elif(z==y and y>x):
    print(f"{x}, {z}, {y}")
elif(x==y and x<z):
    print(f"{x}, {y}, {z}")
elif(x==z and x<y):
    print(f"{x}, {z}, {y}")
elif(z==y and y<x):
    print(f"{y}, {z}, {x}")

else:
    print(f"A három szám egyenlő. ({x},{y},{z})")
