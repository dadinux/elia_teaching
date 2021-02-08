# -*- coding: utf-8 -*-

# QUESTA SEZIONE È FACOLTATIVA E SERVE SOLO A PULIRE LA PAGINA DALLE ALTRE RIGHE     |
#                                                                                    |                                    
#                                                                                    |  
from os import system, name         # importa "system" dalla libreria "os"           |
                                    #                                                |
def clear():                        # definisce la funzione clear()                  |  
                                    #                                                |    
    if name == 'nt':                # for windows                                    |
        _ = system('cls')           #                                                |
    else:                           # for mac and linux(here, os.name is 'posix')    |    
        _ = system('clear')         #                                                |
# ========================== FINE SEZIONE FACOLTATIVA ===============================|

clear()

n = int(input("\n\n\nInserisci di quanti numeri vuoi calcolare la media (n intero e positivo): "))
while(n <= 0):
    clear()
    n = int(input("\n\n\nInserisci di quanti numeri vuoi calcolare la media (n intero e positivo): "))

numero = 0
somma = 0
media = 0

clear()
print("\nVerrà ora richiesto di inserire %d numeri interi positivi.\n\n" %n)

for i in range(1,n+1):
    print("Step %d" %i)
    print("*********\n")
    numero = int(input("Inserisci un numero: "))
    somma = somma + numero
    media = somma / i
    print("La media parziale è:  %f" % (media))

clear()

print("\n\n**********************  RISULTATO  **********************\n")
print("La media di tutti gli n = %d  numeri inseriti è: %f\n\n\n" % (n, media))