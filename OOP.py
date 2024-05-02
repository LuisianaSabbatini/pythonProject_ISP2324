## PROGRAMMAZIONE ORIENTATA AGLI OGGETTI IN PYTHON
# NB: non possiamo esplicitare la visibilità privata in python, di default è applicata la visibilità pubblica

class ContoBancario():

    # attributi con ambito di classe
    numeroConti = 0

    def __init__(self, nomeIntestatario, cognomeIntestatario, idConto, saldo = 0): #costruttore --> dichiarazione relativi ad attributi con ambito di istanza
        if type(nomeIntestatario) == str:
            self.nomeIntestatario = nomeIntestatario # attributo nomeIntestatario, con ambito di istanza
        else:
            print('Errore: inserire il primo argomento di tipo stringa!')
            var = input()
            self.nomeIntestatario = var
        self.cognomeIntestatario = cognomeIntestatario
        self.idConto = idConto # attributo idConto, con ambito di istanza
        self.saldo = saldo
        # self.emailAttr = '{}.{}@email.it'.format(self.nomeIntestatario.lower(), self.cognomeIntestatario.lower())
        ContoBancario.numeroConti += 1

    @property # property decorator - dichiarare attributi con particolari funzionalità
    def email(self): # GETTER
        if self.nomeIntestatario == None or self.cognomeIntestatario == None:
            return None
        else:
            return '{}.{}@email.it'.format(self.nomeIntestatario.lower(), self.cognomeIntestatario.lower())

    @email.setter
    def email(self, nuovaMail):
        '''riceve in input una stringa mail del tipo: nome.cognome@dominio.it e aggiorna i valori degli attributi nome e cognome'''
        dati, dominio = nuovaMail.split('@')
        nome, cognome = dati.split('.')
        self.nomeIntestatario = nome
        self.cognomeIntestatario = cognome

    @email.deleter
    def email(self):
        self.nomeIntestatario = None
        self.cognomeIntestatario = None

    # metodi così definiti hanno automaticamente ambito di istanza
    def deposito(self, importo):
        self.saldo += importo

    def prelievo(self, importo):
        self.saldo -= importo

    #metodo per creare un summary dell'intestatario del conto
    def datiIntestatario(self):
        return 'Gentile {} {}'.format(self.nomeIntestatario, self.cognomeIntestatario)

# creare un oggetto di tipo ContoBancario
conto1 = ContoBancario('Luisiana', 'Sabbatini', 12345)
print(conto1.__dict__)
# conto1.cognomeIntestatario = 'Sabbatini' # da evitare se vogliamo seguire i principi dell'OOP...
# print(conto1.__dict__)

# vedere il valore degli attributi con ambito di istanza: è possibile solo tramite dot notation sul singolo oggetto istanziato
print(conto1.nomeIntestatario)
print(conto1.idConto)
print(conto1.datiIntestatario())
print(conto1.email)
# print("questa è la mail creata a modo di semplice attributo con ambito di istanza")
# print(conto1.emailAttr)

conto1.nomeIntestatario = 'Mario'
print("questa è la mail gestita dal property decorator")
print(conto1.email)
# print("questa è la mail creata a modo di semplice attributo con ambito di istanza")
# print(conto1.emailAttr)

conto1.email = 'mario.rossi@email.it'
print(conto1.nomeIntestatario)
print(conto1.cognomeIntestatario)
print(conto1.email)

del conto1.email # svuotamento di una proprietà
print(conto1.nomeIntestatario)
print(conto1.cognomeIntestatario)
print(conto1.email)

print('Il numero di conti correnti attivi è: %i' % ContoBancario.numeroConti)

conto2 = ContoBancario('Mario', 'Rossi', 23456)
# vedere come conto1 sia un oggetto con un proprio indirizzo
# print(conto1)
# print(conto2.nomeIntestatario)

# print(ContoBancario.__dict__)


print('Il numero di conti correnti attivi è: {}. Il primo è intestato a {}. Il secondo è intestato a {}'.format(ContoBancario.numeroConti, conto1.nomeIntestatario, conto2.nomeIntestatario))

# accesso ad attributi con ambito di classe: abbiamo due modalità
print(ContoBancario.numeroConti)
print(conto1.numeroConti)


# manomettiamo un oggetto di tipo ContoBancario...
# conto1.numeroConti = 4
# print(conto1.numeroConti) # abbiamo aggiuntop un attributo con ambito di istanza, chiamato "numeroConti"
# print(ContoBancario.numeroConti)
# print(conto2.numeroConti) #faccio riferimento all'attributo della classe!

# print('Il dict associato all''oggetto conto1 è diventato: {}'.format(conto1.__dict__))


#____________________________________________________________________________________________________
#### EREDITARIETÀ
# method resolution order: logica che python utilizza per "cercare" i metodi ogni volta che invochiamo metodi su un oggetto appartenente ad una qualche gerarchia di ereditarietà

class ContoLibretto(ContoBancario):
    def __init__(self, nomeIntestatario, cognomeIntestatario, idConto, tassoInteresse, saldo=0): # OVERLOADING
        super().__init__(nomeIntestatario, cognomeIntestatario, idConto, saldo)     # sfrutto quanto implementato nella classe madre
        self.tassoInteresse = tassoInteresse

    def deposito(self, importo): #OVERRIDING
        super().deposito(importo * self.tassoInteresse) #senza riscrivere il metodo, sfrutto quello della superclasse

    @classmethod #decoratore per metodo di classe
    def nuovoDaStringaUnita(cls, datiIntestatario, idConto, tassoInteresse, saldo=0):
        if ' ' not in datiIntestatario:
            raise ValueError #lancio di un errore
        nomeIntestatario, cognomeIntestatario = datiIntestatario.split(' ', 2)
        return cls(nomeIntestatario, cognomeIntestatario, idConto, tassoInteresse, saldo)

# istanziazione dcon il costruttore classico
contoLibretto1 = ContoLibretto('Luisiana', 'Sabbatini', 98765, 0.05)
contoLibretto2 = ContoLibretto('Mario', 'Rossi', 87654, 0.05, 1000)

#istanziazione con il coastruttore secondario definito tramite classmethod
contoLibretto3 = ContoLibretto.nuovoDaStringaUnita('Mario Rossi', 1928, 0.04,200)
# print(contoLibretto1.__dict__)
# print(contoLibretto1.saldo)
print(contoLibretto3.datiIntestatario())



# print(help(ContoLibretto)) # per vedere il dettaglio relativo ad una classe

# print(ContoLibretto.mro()) #per vedere il method resolution order di una classe

# print(issubclass(ContoLibretto, ContoBancario)) #per controllare manualmente l'eventuale gerarchia di ereditarietà tra classi
# print(issubclass(ContoBancario, ContoLibretto))

# print(isinstance(conto1, ContoBancario)) # per vedere se un oggetto è istanza di una particolare classe
# print(isinstance(contoLibretto1, ContoBancario))

# METODO STR
# print(conto1.__str__())
# print(id(conto1) )



class ContoLibrettoProva(ContoBancario):
    # codice per avere un cosrtruttore alternativo dove nomeIntestatario è composto da nome e cognome
    # e va splittato per riempire gli attributi dell'oggetto

    # qua sotto la soluzione rudimentale con più alternative manualmente gestite dentro al nostro costruttore
    # --> i nomi dei parametri possono diventare fuorvianti in questo caso, proporremo quindi una soluzione con
    # decoratore @classmethod
    def __init__(self, nomeIntestatario, idConto, tassoInteresse, cognomeIntestatario = None, saldo = 0): # OVERLOADING
        if cognomeIntestatario is None:
            self.nomeIntestatario, self.cognomeIntestatario = nomeIntestatario.split(' ')
            self.idConto = idConto
            self.tassoInteresse = tassoInteresse
            self.saldo = saldo
        else:
            super().__init__(nomeIntestatario, cognomeIntestatario, idConto, saldo)     # sfrutto quanto implementato nella classe madre
            self.tassoInteresse = tassoInteresse

    def deposito(self, importo): #OVERRIDING
        super().deposito(importo * self.tassoInteresse) #senza riscrivere il metodo, sfrutto quello della superclasse

contoL1 = ContoLibrettoProva('Luisiana', 98765, 0.05,'Sabbatini')
contoL2 = ContoLibrettoProva('Mario Rossi', 98765, 0.05)

print(contoL1.datiIntestatario())
print(contoL2.datiIntestatario())



#____________________________________________________________________________________________________
## EREDITARIETÀ MULTIPLA

class Foo():
    foo = 'attributo foo di classe foo'
    def mFoo(self):
        print('ciao Foo')

class Bar():
    foo = 'attributo foo di classe bar'
    bar = 'attributo bar di classe bar'
    def mBar(self):
        print('ciao Bar')

class FB(Bar, Foo): # purché separate da virgola, possono esserci più superclassi per FB
    fb = 'attributo sottoclasse'
    def mFB(self):
        super().mBar()

oggFB = FB() # è possibile istanziare oggetti FB perché l'__init__ è definito a livello di superclasse object

print(oggFB.foo)

# print(help(FB))
oggFB.mFB()

class FB(Foo, Bar): # purché separate da virgola, possono esserci più superclassi per FB
    fb = 'attributo sottoclasse'

oggFB = FB() # è possibile istanziare oggetti FB perché l'__init__ è definito a livello di superclasse object

print(oggFB.foo)

# print(help(FB))


#____________________________________________________________________________________________________
## MONKEY PATCHING
#1. definire una funzione
def get_tassoInteresse(self):
    return self.tassoInteresse

#2. aggiungere la funzione definita ad una classe
ContoLibretto.get_tassoInteresse = get_tassoInteresse

print(contoLibretto1.get_tassoInteresse())


#________________________________________________________________________________________________
# CLASSI ASTRATTE
#PRIMA SOLUZIONE non del tutto buona (rende possibile istanziare la classe astratta)
class Frutta: #classe astratta
    def controlla_classe_astratta(self):
        raise NotImplementedError("controllare l'implementazione!") # lanciando un errore

class Mela(Frutta): # sotto-classe concreta
    def controlla_classe_astratta(self):
        #....
        print('è stata fornita un''implementazione del metodo astratto')

mela = Mela()
mela.controlla_classe_astratta()

frutto = Frutta() #istanziazione di una classe astratta.
print(id(frutto))


#SECONDA SOLUZIONE: con il modulo Abstract Base Class (ABC)
from abc import ABCMeta, abstractmethod
class ClasseAstratta(metaclass=ABCMeta):
    @abstractmethod
    def metodo_astratto(self): ##CONTROLLARE
        pass
class Sottoclasse(ClasseAstratta):
    def metodo_astratto(self): #forniamo una concreta implementazione del metodo astratto
        print('ho implementato il metodo astratto')

oggetto1 = Sottoclasse()

print('l''id dell''oggetto concreto è {}'.format(id(oggetto1)))

# oggetto2 = ClasseAstratta()
# print('l''id dell''oggetto astratto è {}'.format(id(oggetto2)))



