n = int(input("inserisci quanti numeri vuoi: "))

numero = 0
i = 0
somma_pari= 0
somma_dispari = 0

while(i < n):
    numero = int(input("inserisci un numero: "))
    if numero % 2 == 0:
        somma_pari = somma_pari + numero
    else:
        somma_dispari = somma_dispari + numero
    i = i + 1

print("la somma dei numeri pari e': " , somma_pari)
print("la somma dei numeri dispari e': " , somma_dispari)