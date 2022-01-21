import random

tipp: int = 0
rnd: int = 0
tippekSzama: int = 1
temp: str = ""

rnd = random.randint(0,9)

while(tipp != rnd and tippekSzama <= 5):
    temp = ""
    while(temp == "" or temp.isspace() or not temp.isnumeric()):
        temp = input(f"Kérem az {tippekSzama}. tippet:")
        if(temp.isnumeric()):
            tipp = int(temp)
            tippekSzama += 1
        else:
            print(f"Nem számot adott meg tippnek!")

if(tipp == rnd):
    print(f"Gratulálunk, eltalálta a számot: {rnd} a(z) {tippekSzama}. tippelésre")
else:
    print(f"Sajnáljuk, sajnos nem találta el a számot: {rnd} dont care didnt ask youre white cry about it stay mad get real L mald seethe cope harder hoes mad basic skill issue ratio you fell off the audacity triggered any askers redpilled  get a life ok and cringe touch grass donowalled not based yourre a gypsy not funny didnt laugh youre grammar issue go outside get good reported ad hominem GG ask deez ez clap straight cash ratio again final ratio stay mad stay pressed pedophile cancelled done for mad free freer than air rip bozo slight smile cringe again mad cuz bad lol irrelevant cope  jealous  go ahead whine about it  your problem  dont care even more  sex offender  sex defender  not okay  glhf  problematic")