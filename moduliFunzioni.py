## MODULI
# import math
import random as rnd #import di modulo assegnandogli un nome personalizzato
from math import sin, sqrt # importare singole funzioni da un modulo

print(sqrt(9))
print(rnd.randint(0,10)) # genera un numero intero casuale nell'intervalòlo 0-10

## MEGLIO IMPORTARE SINGOLE FUNZIONI O L'INTERO MODULO???

def sqrt(numero):
    return numero**2

print(sqrt(9))

# function resolution order --> se abbiamo metodi con stesso nome in moduli diversi,
# meglio import "manuale"
# from modulo1 import funzioneOmonima as modulo1_funz
# from modulo2 import funzioneOmonima as modulo2_funz
# nel codice potrò invocare sia la versione di modulo1 che la versione di modulo 2 facendo riferimento ai nomi che ho dato




