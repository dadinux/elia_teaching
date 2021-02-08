#!/usr/bin/env python3


# 
#  

def ciclo_while_somma(): 
 
    i = 0 # i assumerà la funzione del numero da elevare al quadrato
          # dunque sarà i = 0, i = 1, i = 2, ... fino a che sarà UGUALE a num
          # ad ogni ciclo, il valore sarà incrementato di uno

    isomma = 0 
    


    while (i <= 10 ): 
        # ================== blocco da eseguire =========================
        # fino a che (while) viene VERIFICATA la condizione indicata 
        # nella parentesi dopo "while" ovvero: 
        # "i è MINORE O UGUALE A "10" ?"
        # 
        # Se la risposta è SI allora ESEGUI il blocco
        # Se la risposta è NO allora ESCI dal ciclo.
        #

        # QUESTA ISTRUZIONE CALCOLA LA SOMMA
        isomma = isomma + i 
        
        # QUESTA ISTRUZIONE "STAMPA" A VIDEO IL RISULTATO DEL QUADRATO
        print(str(isomma))
        
        # QUESTA ISTRUZIONE INCREMENTA IL CONTATORE i DI UN'UNITA'
        i = i + 1

ciclo_while_somma()



