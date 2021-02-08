# NOTE PER ELIA:
# ===================================================================================|
# "\n" aggiunge una riga vuota                                                       |
# "\t" aggiunge una tabulazione in modo tale da allineare i valori in colonna        |
#                                                                                    |
#                                                                                    |
# QUESTA SEZIONE È FACOLTATIVA E SERVE SOLO A PULIRE LA PAGINA DALLE ALTRE RIGHE     |
#                                                                                    |                                    
#                     >>>>> NON    DEVI   FARLA <<<<<                                |
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

# chiaramente NON DEVI INSERIRE LA FUNZIONE clear() QUA SOTTO
clear() # lancio la funzione clear() per pulire la pagina prima di inserire i dati

print("\n\n")

# RICHIESTA INSERIMENTO DATI =================================
#base = float(input("Inserisci un valore per la base: "))       #float definisce che il tipo di dato è a "virgola mobile"
#altezza = float(input("Inserisci un valore per l'altezza: "))  #float definisce che il tipo di dato è a "virgola mobile"

# Calcolo area e perimetro e assegno i valori alle variabili area e perimetro

base = float(input("Inserisci un valore positivo per la base: "))
while (base<=0):
    base = float(input("Hai inserito un valore errato per la base. Inserisci un valore positivo: "))

altezza = float(input("Inserisci un valore positivo per l'altezza: "))
while (altezza<=0):
    altezza = float(input("Hai inserito un valore errato per l'altezza. Inserisci un valore positivo: "))

# === CALCOLO AREA E PERIMETRO ===
# 
# area = base * altezza
# perimetro = (base + altezza)*2
# 
# ============================


clear() # lancio la funzione clear() per pulire la pagina prima di mostrare i risultati

# PRESENTAZIONE RISULTATI =====================================
print("\n\n")
print("------ Dati iniziali rettangolo ----------------\n")
print("Base: " + "\t\t\t" + str(base))
print("Altezza: " + "\t\t" + str(altezza) + "\n\n")
print("------ Risultati problema ----------------------\n")
print("Area: " + "\t\t\t" + str(base * altezza))
print("Perimetro: " + "\t\t" + str((base + altezza) * 2) + "\n")
print("------------------------------------------------\n\n\n\n\n\n\n\n\n\n\n\n")