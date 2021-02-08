#!/usr/bin/env python3

## Verify if the inserted number is odd or even

# DEFINISCO UNA FUNZIONE CHE:
# - VERIFICHI SE NUMBER È PARI O DISPARI
# - CHE RADDOPPI IL VALORE DI NUMBER SE QUESTO È PARI
# - CHE TRIPLICHI IL VALORE DI NUMBER SE QUESTO È DISPARI
# 
#  

def odd_or_even(): 

    import math ## Python math library

    print(" ODD or EVEN?")
    print("_________________________")
    print("")
    number = int(input("Insert a integer:  " ))
    
# CICLO IF

    if (number % 2) == 0 :
        
        print("")
        print(str(number) + " è un numero pari")
        print("")
        print("Raddoppio il valore di number: " + str(number * 2))
        print("")
        print("")
    
    else:
        print("")
        print(str(number) + " è un numero dispari")
        print("")
        print("Triplico il valore di number: " + str(number * 3))
        print("")
        print("")


odd_or_even()


