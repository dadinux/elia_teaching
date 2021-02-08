
from os import system, name         # importa "system" dalla libreria "os"           |
                                    #                                                |
def clear():                        # definisce la funzione clear()                  |  
                                    #                                                |    
    if name == 'nt':                # for windows                                    |
        _ = system('cls')           #                                                |
    else:                           # for mac and linux(here, os.name is 'posix')    |    
        _ = system('clear')

clear()

n = int(input("Quante righe vuoi stampare:  "))
grafica = input("Quale grafica vuoi usare? a=stelline b=cerchi c=puntini : ")
i = 1

clear()

if(grafica == "a"):
    stringa="*******"
elif(grafica == "b"):
    stringa="ooooooo"
elif(grafica == "c"):
    stringa="......."

while(i <= n):
    print(stringa)
    i = i + 1




