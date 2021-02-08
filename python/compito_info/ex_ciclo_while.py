#!/usr/bin/env python3

# ================ ESEMPIO DI CICLO WHILE ======================
#
# DEFINISCO UNA FUNZIONE CHE:
# CALCOLI IL VALORE DI X^2 PER TUTTI INTERI NUMERI CHE VANNO
# DA 0 AD UN NUMERO CHE VERRA' RICHIESTO ALL'AVVIO DEL PROGRAMMA
# PERCUI SE INSERIRAI num = 4 ALLORA IL SISTEMA CALCOLERA' TUTTI I
# QUADRATI DEI NUMERI DA 0 A 4.
# 
#  

def ciclo_while(): 

    num = int(input("Inserisci un numero INTERO e POSITIVO:  "))
    
    # INIZIALIZZO LE VARIABILI i e i2 OVVERO IL CONTATORE e IL VALORE
    # # DI i AL QUADRATO
    
    i = 0 # i assumerà la funzione del numero da elevare al quadrato
          # dunque sarà i = 0, i = 1, i = 2, ... fino a che sarà UGUALE a num
          # ad ogni ciclo, il valore sarà incrementato di uno

    i2 = 0 # i assumerà la funzione di valore elevato al quadrato
    
    # num, come già detto sarà il valore massimo che potrà raggiungere i
    # ovvero, il valore massimo del quale noi vorremo calcolare il quadrato 

    while (i <= num ): 
        # ================== blocco da eseguire =========================
        # fino a che (while) viene VERIFICATA la condizione indicata 
        # nella parentesi dopo "while" ovvero: 
        # "i è MINORE O UGUALE A "num" ?"
        # 
        # Se la risposta è SI allora ESEGUI il blocco
        # Se la risposta è NO allora ESCI dal ciclo.
        #

        # QUESTA ISTRUZIONE CALCOLA IL QUADRATO DI i
        i2 = i ** 2  # ** è l'operatore di elevamento a potenza di Python
        
        # QUESTA ISTRUZIONE "STAMPA" A VIDEO IL RISULTATO DEL QUADRATO
        print(str(i) + " elevato al quadrato mi da: " + str(i2))
        
        # QUESTA ISTRUZIONE INCREMENTA IL CONTATORE i DI UN'UNITA'
        i = i + 1

ciclo_while()

# AD ESEMPIO:
# 
# num = 4
# i = 0
# i2 = 0
#
# ESEGUO
# i = 0, i <= 4? SI => i2 = i**2 = 0, i = i + 1 = 1
# i = 1, i <= 4? SI => i2 = 1**2 = 1, i = i + 1 = 2
# i = 2, i <= 4? SI => i2 = 2**2 = 4, i = i + 1 = 3
# i = 3, i <= 4? SI => i2 = 3**2 = 9, i = i + 1 = 4
# i = 4, i <= 4? SI => i2 = 4**2 = 16, i = i + 1 = 5
# i = 5, i <= 4? NO => ESCI DAL CICLO


