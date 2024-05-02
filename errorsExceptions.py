## ERRORI ED ECCEZIONI

#errori --> vanno per forza corretti per poter eseguire il codice
# eccezioni --> possono essere gestite

try:
    # myFile = open('prova.txt') # potrebbe lanciare un'eccezione --> va gestita (exception handling)
    raise ZeroDivisionError # lancio l'errore/eccezione
except FileNotFoundError:
    print('Nome di file non valido!')
except NameError:
    print('Riferimento non risolvibile!')
except Exception:
    print('Errore indefinito!')
else: # blocco di codice che verrà eseguito solo se non si verifica alcuna eccezione
    # myFile.close()
    print('non si è verificata alcuna eccezione')
finally: # blocco di codice che verrà eseguito sempre alla fine, sia nel caso di eccezioni sia nel caso senza eccezioni
    print('eseguirò sempre questo codice dentro il finally')