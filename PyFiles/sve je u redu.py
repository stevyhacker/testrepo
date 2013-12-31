import random
import time
def Uvod ():
    print ('Ti si u zemlji zmajeva')
    time.sleep(1)
    print ('Moras da pronadjes blago')
    print ('Ono se nalazi u jednoj od pecina ispred tebe')
    time.sleep (2)
    print ('U jednoj se nalazi dobri a u jednoj gladni zmaj')
    print ()
def izaberiPecinu ():
    pecina = ''
    while pecina != '1' and pecina != '2':
        print ('Izaberi pecinu u koju ces da udjes ?(1 or 2)')
        pecina = input ()
    return pecina
def provjera (izabranaPecina):
    print ('Ulazis u pecinu ...')
    time.sleep (2)
    print ('Mracno je i prljavo')
    time.sleep (1)
    print ('Veliki zmaj se odjednom pojavljuje i otvara svoje celjusti ...')
    print ()
    time.sleep (2)
    dobriZmaj = random.randint (1,2)
    if izabranaPecina == str (dobriZmaj):
        print ('i dava ti svoje blago !!! ')
    else:
        print ('I prozdire te u jednom zalogaju !!! ')
igratiponovo = 'da'
while igratiponovo == 'da':
    Uvod()
    brojPecine =izaberiPecinu()
    provjera(brojPecine)
    print ('Hoces li da igras ponovo ? (da,ne)')
    igratiponovo = input ()

