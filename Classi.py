class Persona():
    def __init__(self, nome, cognome, eta, voti = 0): # opzione B (attr con valore di iniz.): __init__(self, nome, cognome, eta)
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.voti = voti # 0

class Cittadino(Persona):
    def __init__(self, nome, cognome, eta, voti=0):
        super().__init__(nome, cognome, eta, voti)
        self.votato = False

    def votare(self, candidato):
        if not(self.votato):
            self.votato = True
            candidato.voti += 1
        else:
            print("Hai già votato!!! Furbetto")

p1 = Persona("Luisiana", "Sabbatini", 32, 2)
# print(p1.votato)
# p1.votato = 0
# print(p1.votato)

p2 = Persona("Mario", "Rossi", 35,7)

# print(p2.votato)

c1 = Cittadino("Luisiana", "Sabbatini", 32)
print(c1.votato)

c2 = Cittadino("Mario", "Rossi", 35,7)

c1.votare(p1)
print(p1.voti)
c1.votare(p2)
print(c1.voti)