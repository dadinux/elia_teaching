
# DEFINIZIONE DELLA FUNZIONE CHE CONTROLLA CHE I DUE NUMERI
# SIANO COMPRESI FRA DUE ESTREMI DATI
# estremo1 => estremo inferiore
# estremo2 => estremo superiore

def verifica(estremo1,estremo2):
   
   numero = int(input("Inserire un numero da " + str(estremo1) + " a " + str(estremo2) + ": "))
   
   while(numero < estremo1 or numero > estremo2):
      numero = int(input("Hai inserito un numero non valido. Inserisci un numero fra " + str(estremo1) + " e " + str(estremo2) + ": "))
   
   return numero


# CHIAMATA DELLA FUNZIONE  "verifica" per tre differenti estremi

numero1 = verifica(0,10)
numero2 = verifica(20,30)
numero3 = verifica(40,50)



if(numero1%2 == 0 and numero2%2 == 0 and numero3%2 == 0):
    print("Il prodotto dei numeri immessi è: " + str(numero1 * numero2 * numero3))
else:
    print("I numeri non sono entrambi pari")
