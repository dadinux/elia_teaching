# Cosa non va in questo codice:
# 

x=0         # Contatore ciclo while
Xsomma=0    # Somma di tutti i numeri da 1 a 10


while x <= 1234567890:
    
    Xsomma = Xsomma + x       # Ricordati identazione
    x = x + 2                 # Ricordati identazione

print("Il totale è: " + str(Xsomma))

# Il comando Print non può accoppiare due tipi di dato differenti
# Per questo uso la funzione str per convertire il tipo di dato int
# corrispondente alla variabile Xsomma in un dato di tipo stringa




