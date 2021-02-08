def esercizio_2():

    x = int(input("Inserisci un numero intero positivo:  "))
    N = int(input("Inserisci un secondo numero intero positivo:  "))

    i = 0
    print("x= " + str(x))
    print("N= " + str(N))
    print("")
    print("")    
    print(str(N) + " numeri successivi a " + str(x) + ":")
    print("")
    while(i < N):
        x = x + i
        i = i + 1
        print(str(x))
    
esercizio_2()
