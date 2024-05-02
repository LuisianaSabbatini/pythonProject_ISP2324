

nomevariabile = 2 # assegnamento di un valore (2) ad una variabile (nomevariabile)
i2 = 3 # dare nomi particolari alle variabili OK ma no simboli o numeri come primo carattere
i_2 = 4 #possono essere usati underscore per fare "spazi" nei nomi variabili, altrimenti il CamelCase è generalmente utilizzato

var2 = nomevariabile #assegnato ad una variabile, un'altra variabile --> fanno riferimento allo stesso oggetto
print(var2)

var1 = var3 = var4 = 9 # assegnamento multiplo sincrono
print(type(var1)) # type, funzione per vedere il tipo di una variabile

x=5
y=x

x=x+1 # se incremento x di 1...cosa succede ad y
print('y vale {}'.format(y))
print('x vale {}'.format(x))

# UNPACKING
v1, v2 = [3, 4] # serve la stessa numerosità a dx e sx dell'=
print(v1)
print(v2)


# INDENTAZIONE
# è obbligatoria dopo una riga di dichiarazione di funzione o dopo altri costrutti che prevedono la chiusura della dichiarazione con i :
def funzione_prova(): # finisce per : quindi vuole almeno una riga successiva indentata!! Altrimenti non potete eseguire il codice
    pass # per non far fare niente alla funzione, senza creare errori di esecuzione...
variabile = 3
print(variabile)


# TIPI PRIMITIVI
v_stringa = '123' #str
print(type(v_stringa))

v_float = 1.0 # float
print(type(v_float))

int_esa = 0x2A # interi esadecimali
print(int_esa)

float_esp = 1.02e2 # float esponenziale
print(float_esp)


# CONVERSIONE TRA NUMERI
int("13") # conv a int di una stringa numerica
# int("abc") # possibile purché la stringa possa essere interpretata con un int!

print(float(x))
print(x)
x_float = float(x) # assegnamento della conversione
print(x_float)


# OPERATORI MATEMATICI
x+y
x-y
x*y
x/y
x**y #elevamento a potenza
x += 2 # operazioni in place (+, -, *, /)
y -= 2
x % 2 # operatore modulo
print(x)

# VARIABILI DI TIPO BOOLEANO
v_b1 = True
v_b2 = False

# operatori booleani
print(v_b1 and v_b2) #falso
print(v_b1 or v_b2) #vero
print(not v_b1) #falso

print((v_b1 or v_b2) and v_b1) #espressioni con operatori booleani

# valori falsi in python (tutto il resto è interpretato come vero)
bool = False
# bool = None
# bool = 0
# bool = 0.0
# bool = ''
# bool = ()
# bool = []
# bool = {}

if bool:
    print(str(bool) + " è vero!")
else:
    print(str(bool) + " è falso!")



# CONDIZIONALI (if....)
if v_b1: #argomento direttamente booleano
    print(v_b1)
    print("v_b1 è vero")
elif not v_b2: # posso aggiungere quanti elif desidero
    pass # keyword per non fare nulla ma bypassare il controllo "qualità" del codice scritto
else: # non è obbligatorio, ed in caso è solamente uno
    print("nessuna condizione precedente era vera.")

# operatori di confronto in python: ==, is, <,>,>=,<=, !=, in
if v1 == v2:
    print("stesso valore")
elif v2 > v1:
    print("v2 è strettamente maggiore di v1")
elif v2 != v1:
    print("v2 è diverso da v1 e minore di esso")

s1 = 'ciao'
s2 = s1
s2 = 'Ciao'

# l'operatore is verrà trattato più avanti...

#in
if 2 in [1,2,3]:
    print("il numero è nell'insieme")


# STRINGHE: sono immutabili!!
c = 'ciao'
d = "Luisiana"
print(c+d)
print(c*4)
print(c[0])
print(c[:2]) # fino a indice 2 (escluso)
print(c[-1])

#c[0] = 'C' # errore essendo immutabili
#print(c)

stringa_gigante = '''stringa
su più 
    righe'''

print(stringa_gigante)

for pincopallino in d: #ciclo for su elemento iterabile/scorrere
    print(pincopallino)

print(pincopallino)

## str() e repr()
print(type(str(x)))

## ALcuni metodi per le stringhe
print(stringa_gigante.split(' ')) #split in base a un carattere separatore
print('-'.join('ciao')) #join delle
print(d.lower())
print(d) #sempre immutato!
print(d.upper())
print(d.find('a'))
print(d.rfind('a'))
print('scambiando le a con le o ottengo: ', d.replace('a', 'o'))
print(d.strip()) #per rimuovere eventuali spazi iniziali o finali da una stringa

# formattazione di stringhe composte da valori di variabili
nome = "alunno 1"
eta = 10

print("%s ha %i anni" % (nome, eta)) #criteri di formattazione stringhe
print("{} ha {} anni".format(nome, eta)) #altre modalità di formattazione stringhe, con placeholder

#CICLI

# FOR
for i in [0,1,2,3]:
    print(i)

for i in range(0,5):
    print(i)

# WHILE
i=0
while i<3:
    print(i)
    i += 1

a=10
while True:
    a -= 1
    print(a)
    if a<7:
        break # esce dal ciclo while
    elif a==8:
        continue # interrompe i comandi di questa iterazione e passa alla successiva
    print('fatto')


# ARRAY
from array import *

my_array = array('i', [1,2,3,4,5,6,7,8]) #inizializzare un array (istanza di tipo array)
print(my_array)

my_array2 = my_array

my_array.append(9) # è un'operazione in place
for i in my_array:
    print(i)

my_array.insert(1, 2)
for i in my_array:
    print(i)

## uguaglianza ed identità sugli array
print('my_array vale ', my_array)
print('my_array2 vale ', my_array2)
print('my_array e my_array2 sono uguali? ', my_array == my_array2)
print('my_array e my_array2 sono identici? ', my_array is my_array2)

my_arr2 = array('i', [10,10])

my_array.extend(my_arr2)
print("array concatenati: ", my_array)

my_array.remove(2)

my_array.pop() # rimmuove l'ultimo elemento

print("array dopo le rimozioni varie: ", my_array)

my_array.reverse()

my_array.count(2) #per contare le occorrenza del 2 nell'array
# my_array.find(3) #per trovare la prima occorrenza (indice) di un valore nell'array

# COLLEZIONI: LISTE, TUPLE, DIZIONARI
# LISTE: collezioni ordinate
lista_numerica = [1, 2, 3]
lista_stringhe = ['abc', 'def', 'ghi']
lista_mista = [1, 'abc', 2.2]
lista_vuota = []

lista_numerica.append(4)
print('ecco come appare una lista: ', lista_numerica)
print('ecco l''elemento di indice 3 della lista definita sopra: ', lista_numerica.index(3))
#print(lista_numerica.index(5)) #restituisce errore essendo 5 fuori dal range degli elementi esistenti

lista_stringhe.pop()
print(lista_stringhe)

lista_mista.remove(2.2)
print(lista_mista)

lista_mista.reverse()

lista_aggregata = lista_mista + lista_numerica
print(lista_aggregata)

#lista_aggregata.sort(reverse=True)
#print(lista_aggregata)

print(len(lista_aggregata))

print(len(my_array))

#print(lista_aggregata[len(lista_aggregata)-1])#accedere all'ultimoi elemento della lista

#slice notation: spezzare liste in sotto-liste
#print(lista_aggregata[:(len(lista_aggregata)/2)])

#iterazioni su liste
for i in lista_aggregata:
    print(i)

print('abc' in lista_aggregata)

lista_ripetute = ['abc']*4
print(lista_ripetute)

# LISTA MULTIDIMENSIONALE
lista_multidim = [[[1,2,3], [4,5,6], [7,8,9]],[[1,2,3], [4,5,6], [7,8,9]]]
print(lista_multidim[1][1][2])



#_________________________________________________________________________________________
# DIFFERENZE TRA IS (identità) e == (uguaglianza)

# uguaglianza vs identità
lista1 = [1,2,3,4]
lista2 = [1,2,3,4]
# lista2 = lista1


if lista1 is lista2: # Vero solo se i due oggetti sono proprio la stessa cosa (id univoco)
    print('le due liste sono identiche')
elif lista1 == lista2: #
    print('le due liste sono uguali')
    print('id lista 1: {}'.format(id(lista1)))
    print('id lista 2: {}'.format(id(lista2)))
else:
    print('nessuna opzione')
    print(lista1)
    print(lista2)

lista1[1] = 9
print(lista2)



#TUPLA: è una entità immutabile
indirizzo_ip = ('10.20.30.40', 8080) #l'oggetto tupla originale
indirizzo_ip = '11.11.11.11', 9090 # altro modo di inizializzare la tupla
indirizzo_vuoto = ()
tupla1 = ('a', 'b', 'c')
print(len(indirizzo_vuoto))
print(len(indirizzo_ip))

print(max(tupla1))
print(min(tupla1))

tupla_da_lista = tuple(lista_mista)
print(tupla_da_lista)
print(lista_mista)



#DIZIONARI: chiavi:valori
diz = {'Italia': 'Roma', #nazione:capitale
       'Inghilterra': 'Londra'}

print(diz['Italia'])
diz['Francia'] = 'Parigi' #aggiunta di coppia chiave/valore
print(diz)

del diz['Italia'] # rimozione di una coppia chiave/valore
print(diz)

print(diz.keys()) #restituisce la lista delle chiavi

print(diz.values()) #restituisce la lista dei valori

print(diz.items()) #restituire le coppie
print(diz)

for k in diz:
    print(k, diz[k])

for k, val in diz.items():
    print(k, val)

diz2 = {'Francia': 'Parigi',
        'Germania': 'Berlino'}

diz_tot = {**diz, **diz2} # per unire due dizionari devo usare questa notazione con doppio asterisco
print(diz_tot)


## UTILIZZO DI DEL
del v2 #eliminazione di variabili
#print(v2)


#INSIEMI
insieme_classe = {'alunno1', 'alunno2', 'alunno3'}
insieme_classe_pom = {'alunno1', 'alunno3', 'alunno5'}
insieme_classe.add('alunno4') #operazione di aggiunta su insieme
print(insieme_classe)

print(insieme_classe.intersection(insieme_classe_pom)) # intersezione

classe_totale = insieme_classe.union(insieme_classe_pom) # unione
print(classe_totale)

# VARIABILE NONE
lista_nulla = None


# IMPORT MODULO MATH
import math

print(math.sqrt(4)) #faccio riferimento direttamente alla classe math.
print(math.pi)

math.sqrt(4)

#FUNZIONI BUILT IN
len(my_array) # len()

for i in range(1,7,2): # inizio, fine, passo
    print(i)


# FUNZIONI PERSONALIZZATE
def stampa123(): #non serve specificare il tipo di ritorno
    "funzione che stampa 1 2 3 Via!!! a terminale" #doc string
    for i in range(1,4):
        print(i)
    print("Via!!!")

stampa123()

def stampa_n(n): # prende in input easattamente un valore
    for i in range(1,n+1):
        print(i)

stampa_n(5)


stampa123.__doc__ # per accedere alla doc string di una funzione

#FUNZIONI CON NUMERO DI ARGOMENTI VARIABILE
def stampa_variabile(*args):
    if len(args) == 1:
        stampa_n(args)
    elif len(args) == 2:
        for i in args: # sistemare
            print(i)

print("stampa variabile con un solo argomento")
# stampa_variabile(2)
stampa_variabile(1,2,3,5,7)


# keyword arguments
def stampakwa(**kwargs):
    for name, value in kwargs:
        print(name, value)

# stampakwa(Nazione = 'Italia') #value

# def funzione(*args, **kwargs)


## FUNZIONI LAMBDA
# SINTASSI: lambda arg1, arg2: istruzione
# NB: restituisce il valore automaticamente

ciao = lambda: 'Ciao!'
print(ciao)

str_up = lambda s: s.upper() # dichiarazione della funzione lambda
print(str_up('ciao'))

## funzioni con ARGOMENTI OPZIONALI (per questi argomenti forniamo un valore di default)

def fare(action = 'nothing'): #'nothing' è il valore di default per l'argomento
    return action

print(fare()) #con zero argomenti

print(fare('parlare')) # con un argomento fornito esplicitamente

# print(fare('parlare', 'mangiare')) # restituisce errore, non è una funz a numero variabile di argomenti!!
def restituisci_somma(n1, n2):
    return n1 + n2 # il return è keyword per far restutuire qualcosa alle funzioni

print(restituisci_somma(1,2))
print(1+2)

## INTROSPEZIONE
print(type(v_stringa)) #restituisce il tipo di una variabile
print(dir(v_stringa)) #restituisce tutti i metodi della classe a cui la variabile appartiene
print(dir(math))

# print(help(str)) #restituisce tutti i metodi con la relativa descrizione

a1 = 2
print(id(a1)) #identità dell'oggetto

l1 = [1,2,3,4]
print((type(l1)))

