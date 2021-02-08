nr = int(input("\n\nQuanti numeri vuoi inserire? : "))

print("\n\nVerranno inseriti " + str(nr) + " numeri\n\n")

i = 1
somma = 0

while(i <= nr):
    numero = int(input("[nr." + str(i) + "] - " + "Inserisci un numero: "))
    i = i + 1 # Incremento il contatore PRIMA del ciclo if altrimenti, a causa della funzione "continue",
              # l'incremento verrebbe saltato in caso di numero pari
    
    if(numero%2 == 0): continue # Con questa istruzione, se il ciclo if valuta numero come "pari",
                                # esclude il resto delle istruzioni del blocco di codice del ciclo while
                                # e passa al valore "nr" successivo.
    
    somma = somma + numero      # se "numero" viene valutato dispari viene eseguita la somma
    
    

print("\n\nLa somma dei numeri dispari inseriti e': " + str(somma) + "\n\n\n")

