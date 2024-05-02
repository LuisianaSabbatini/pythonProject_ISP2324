from OOP import ContoLibretto, ContoBancario

# 1.apertura del file
myFile = open('prova.txt', 'r') # 'w' write - 'r+' lettura e scrittura


# 2. elaborazioni sul/dal file
i=1
for line in myFile:  # iteriamo sulle righe del file
    nome, cognome, id, saldo = line.split('-')
    nome_conto = "conto" + str(i)
    globals()[nome_conto] = ContoBancario(nome, cognome, id, saldo) # creo oggetti con nomi incrementali direttamente dalle righe del file txt
    i+=1

print(conto1)
print(conto2)
print(conto3)


# 3. CHIUSURA DEL FILE!!!
print(myFile.closed)# --> restituirà False
myFile.close()
print(myFile.closed)# --> restituirà True


#___________________________________________________________________________________
# SECONDA ALTERNATIVA: APERTURA E GESTIONE DI FILE CON CONTEXT MANAGER
with open('prova.txt', 'r') as mF:
    i=1
    for line in mF:  # iteriamo sulle righe del file
        nome, cognome, id, saldo = line.split('-')
        nome_conto = "conto" + str(i)
        globals()[nome_conto] = ContoBancario(nome, cognome, id, saldo) # creo oggetti con nomi incrementali direttamente dalle righe del file txt
        i+=1

    print(conto1)
    print(conto2)
    print(conto3)

# print(mF.closed) # --> restituirà True


#___________________________________________________________________________________
## ALTRE FUNZIONI PER FILE...ce ne sono moltissime

# myFile.readlines() # rest lista con righe rimanenti nel file
# myFile.write('stringa aggiunta')



#____________________________________________________________________________________
## INPUT UTENTE DA PROMPT

variabile_inserita = input('inserire un numero intero:')
print(variabile_inserita)

from mainISP import stampa_n
stampa_n(int(variabile_inserita))



#____________________________________________________________________________________
## PICKLE

import pickle

#creazione del file con pickle
with open('file_custom', 'wb') as newFile:
    pickle.dump(conto1, newFile, pickle.HIGHEST_PROTOCOL)



# estrazione info dal file pickle
with open('file_custom', 'rb') as f:
    data = pickle.load(f)
    print(data)

print(data.nomeIntestatario)

