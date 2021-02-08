# Esercizio_1

somma_pari = 0
somma_dispari = 0
numero = 0


risposta = str(input("Vuoi inserire un numero? "))

while(risposta == "si"):
    numero = int(input("Inserisci un numero intero: "))
    if numero % 2 == 0:
       somma_pari = somma_pari + numero
    
    else:
        somma_dispari = somma_dispari + numero
    
    risposta = str(input("Vuoi inserire un altro numero: "))

print("La somma dei numeri pari e': " , somma_pari)
print("La somma dei numeri dispari e': " , somma_dispari)


