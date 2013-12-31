#Ovo je program " Pogodi broj "
import random
brojPokusaja = 0
print ('Zdravo,Ovo je program "Pogodi broj", Reci svoje ime')
ime = input ()
broj=random.randint (1,20)
print ('Dobro, ' + ime + ' Zamislio sam broj od 1 do 20')
while brojPokusaja < 6:
    print ('Pogodi broj ')
    pokusaj = input ()
    pokusaj = int (pokusaj)
    brojPokusaja = brojPokusaja + 1
    if pokusaj < broj:
        print ('Tvoj broj je previse nizak')
    if pokusaj > broj:
        print ('Tvoj broj je previse visok')
    if pokusaj == broj:
        break
if pokusaj == broj:
    brojPokusaja = str ( brojPokusaja )
    print ('Bravo,Pogodio si iz '+ brojPokusaja + ' pokusaja !')
if pokusaj != broj:
    broj = str (broj)
    print ('Nisi pogodio ! Broj koji sam zamislio je ' + broj)
    
    
    
        
