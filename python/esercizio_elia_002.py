n = int(input("quanti numeri vuoi inserire: "))

numero = 0
i = 1
media = 0
somma = 0

while(i <= n):
    numero = int(input("inserire un numero: "))
    somma = somma + numero
    media = somma / i
    print("la media e': " + str(media))

    i = i + 1

print("\n\nla media finale e': " + str(media))

