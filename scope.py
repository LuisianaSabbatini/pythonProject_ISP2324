## SCOPE DELLE VARIABILI : Locale - Enclosed - Globale - built-in
#commentare/togliere il commento dalle linee di codice #global e #nonlocal per vedere gli effetti delle due keyword

var1_int = 2 # assegnamento globale
print('var1_int originariamente vale: ', str(var1_int))
def funz1():
    # global var1_int
    var1_int = 75 # assegnamento locale (interno ad una funzione)
    print('in funz1 vale ' + str(var1_int))

def funz2():
    var1_int = 75 # assegnamento locale (interno ad una funzione)
    print('in funz2 vale ' + str(var1_int))
    def funz_annidata():
        # nonlocal var1_int
        var1_int = 5 # assegnamento locale annidato
        print('in funz_annidata vale ' + str(var1_int))
    funz_annidata()
    print('appena terminata funz_annidata e dentro funz2 vale ' + str(var1_int))

funz1()

print('in globale dopo funz1 vale ' + str(var1_int))

funz2()

print('in globale dopo funz2 vale ' + str(var1_int))
