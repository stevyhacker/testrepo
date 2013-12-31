#Ovo je program za nesto
import random
broj = random.randint(1,20)
print('Zamislio sam jedan broj od 1 do 20.Reci')
brojpokusaja = 0
while brojpokusaja < 6:
    pokusaj = input()
    pokusaj = int(pokusaj)
    brojpokusaja = brojpokusaja + 1
    if pokusaj < broj:
        print ('broj je veci')
    if pokusaj > broj:
        print ('broj je manji')
    if pokusaj == broj:
        break
if pokusaj == broj:
    brojpokusaja = str (brojpokusaja)
    print ('Pogodili ste u ' + brojpokusaja + ' broju pokusaja')
if pokusaj != broj:
    print ('Broj je bio ' + broj)
