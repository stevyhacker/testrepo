# (Igra za debile) Carstvo warcraft

import random
import time

def Pocetak():
    print('Dobodošli u carstvo warcraft')
    print('U ovom svijetu postoje vilenjaci, ljudi, orci i razna druga sranja.')
    print('Svi imaju odredjene prednosti.')
    print('vilenjaci nap=10 od=5, ljudi nap=8 od=7, orci nap=4 od=11')
def Borba():
    print('odaberite vrstu 1. vilenjaci 2. ljudi 3. orci ')
    vrsta=input()
    neprijatelj=random.randint(1, 3)
    uslov=random.randint(1, 2)
    if vrsta=='1' and neprijatelj==1 and uslov==1:
        print('Pobjedili ste vilenjaka u napadu.')
    if vrsta=='1' and neprijatelj==1 and uslov==2:
        print('Izgubili ste u odbrani od vilenjaka.')
    if vrsta=='1' and neprijatelj==2 and uslov==1:
        print('Pobjedili ste ljuda u napadu.')
    if vrsta=='1' and neprijatelj==2 and uslov==2:
        print('Izgubili ste u odbrani od ljuda.')
    if vrsta=='1' and neprijatelj==3 and uslov==1:
        print('Izgubili ste od orka u napadu')
    if vrsta=='1' and neprijatelj==3 and uslov==2:
        print('Pobjedili ste u odbrani od orka')
    if vrsta=='2' and neprijatelj==1 and uslov==1:
        print('Pobjedili ste vilenjaka u napadu.')
    if vrsta=='2' and neprijatelj==1 and uslov==2:
        print('Izgubili ste u odbrani od vilenjaka.')
    if vrsta=='2' and neprijatelj==2 and uslov==1:
        print('Pobjedili ste ljuda u napadu.')
    if vrsta=='2' and neprijatelj==2 and uslov==2:
        print('Izgubili ste od ljuda u odbrani.')
    if vrsta=='2' and neprijatelj==3 and uslov==1:
        print('Izgubili ste orka u napadu.')
    if vrsta=='2' and neprijatelj==3 and uslov==2:
        print('Pobjedili ste u odbrani od orka')
    if vrsta=='3' and neprijatelj==1 and uslov==1:
        print('Izgubili ste u napadu na vilenjaka.')
    if vrsta=='3' and neprijatelj==1 and uslov==2:
        print('Pobjedili ste u odbrani od vilenjaka.')
    if vrsta=='3' and neprijatelj==2 and uslov==1:
        print('Izgubili ste u napadu na ljuda.')
    if vrsta=='3' and neprijatelj==2 and uslov==2:
        print('Dobili ste u odbrani od ljuda.')
    if vrsta=='3' and neprijatelj==3 and uslov==1:
        print('Izgubili ste u napadu na orka.')
    if vrsta=='3' and neprijatelj==3 and uslov==2:
        print('Dobili ste u odbrani od orka.')
PlayAgain='yes'
while PlayAgain=='yes' or 'y':
    Pocetak()
    Borba()
    print('Do you want to play again(yes or no)')
    PlayAgain=input()

        
