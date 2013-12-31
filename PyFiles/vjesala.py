# jednostavna igrica vjesala
import random
import time
print ('Ovo je igrica vjesala 1.0 beta verzija')
time.sleep(1)
print ('Napravio Stevan Bogosavljevic → http://stevy.iz.rs')
print ()
time.sleep(2)
vjesalapozicije = [ '''
 ___
 O  |
    |
    |
    |
 ==== ''','''
 ___
 O  |
 |  |
    |
    |
 ==== ''','''
 ___
 O  |
/|  |
    |
    |
 ==== ''','''

 ___
 O  |
/|\ |
    | 
    |
 ==== ''','''

 ___
 O  |
/|\ |
/   |
    |
 ==== ''','''

 ___
 O   |
/|\  |
/ \  |
     |
 ====  ''']

recnik = '''ananas banana vjetar golub dobar ekvivalent zamka impresija junastvo
kurac lovac ornament pijanstvo rakija svet tranzicija ulica fakultet hemija
mozak debil programer mravojed  internet laptop magarac vebsajt genije'''.split() 
def nasumicnaRec(listareci):
    indeksreci = random.randint(0,len(listareci)-1)
    return listareci [indeksreci]
def prikazTable (vjesalapozicije,promasenaSlova , tacnaSlova ,tajnaRec):
    print (vjesalapozicije[len(promasenaSlova)])
    print()
# Prvo definisem funkcije
    print ('Promasena slova :', end = '')
    for slovo in promasenaSlova:
        print (slovo,end ='')
        print()
        polja ='_' * len(tajnaRec)
        for i in range (len(tajnaRec)):
            if tajnaRec [i] in tacnaSlova:
                polja = polja [:i]+ tajnaRec[i] + polja[i + 1:]
        for slovo in polja :
            print (slovo,end='')
        print()
def pogodak(vecpogodjeno):
    while True :
        print ('Pogodi slovo .')
        pokusaj=input()
        pokusaj = pokusaj.lower()
        if len(pokusaj) != 1:
            print ('Kucaj samo po jedno slovo !')
        elif pokusaj in vecpogodjeno:
                print ('Vec si probao to slovo.Izaberi ponovo.')
        elif pokusaj not in 'abcdefghijklmnopqrstuvwxyz':
                print ('Nemoj kucati slova sa kovrckom (šđčćž) .Ova verzija programa ih ne Podrzava')
        else :
            return pokusaj
def igratiPonovo():
    print ('Hoces li da igras ponovo (da/ne)')
    return input().lower().startswith('d')
print ('VJESALA')
promasenaSlova = ''
tacnaSlova = ''
tajnaRec= nasumicnaRec (recnik)
igraJeZavrsena = False
while True :
    prikazTable(vjesalapozicije,promasenaSlova,tacnaSlova,tajnaRec)
    pokusaj= pogodak (promasenaSlova + tacnaSlova)
    if pokusaj in tajnaRec:
        tacnaSlova = tacnaSlova + pokusaj
        svaSlovaPogodjena = True
        for i in range (len(tajnaRec)):
            if tajnaRec[i] not in tacnaSlova:
                svaSlovaPogodjena = False
                break
        if svaSlovaPogodjena:
            print ('Bravo ! Tajna rijec je '+ tajnaRec + 'Pobjedio si !')
            igraJeZavrsena = True
        else :
            promasenaSlova = promasenaSlova + pokusaj
            if len(promasenaSlova) == len(vjesalapozicije) -1 :
                prikazTable (vjesalapozicije,promasenaSlova,tacnaSlova,tajnaRec)
                print ('Istrosio si sve pokusaje !\n Posle '+ str(len(promasenaSlova)) +'promasenih pokusaja i ' + str(len(tacnaSlova)) + 'tacnih pokusaja , rijec je bila '  + tajnaRec)
                igraJeZavrsena = True
        if igraJeZavrsena:
            if igratiPonovo():
                promasenaSlova = ''
                tacnaSlova = ''
                igraJeZavrsena = False
                tajnaRec = nasumicnaRec(recnik)
            else:
                print ('Pritisni ENTER da izadjes .')
                input ()
                break
