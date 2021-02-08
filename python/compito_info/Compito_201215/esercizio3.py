#!/usr/bin/env python3
def esercizio_3():

    print("")
    print("")
    nr_alunni=int(input("Inserire numero alunni: "))
    #print(type(nr_alunni))

    i = 1
    eta_tot = 0

    while(i<=nr_alunni):
        print("")
        print("")
        eta = int(input("Inserisci l'età dello studente " + str(i) + " :"))
        print("")
        print("Lo studente " + str(i) + " ha " + str(eta) + " anni")
        print("")    
        eta_tot = eta_tot + eta
        i = i + 1
    
    i = i - 1
    print("Hai inserito l'età di " + str(i) + " studenti")
    
    media = eta_tot / i

    print("")
    print("")
    print("Gli Studenti hanno in media " + str(media) + " anni")


    
    
    
esercizio_3()

