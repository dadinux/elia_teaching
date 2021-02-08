#!/usr/bin/python

#librerie
import math
 
#Variabili
m = 1.6 #Kg
g = 9.81 #m/s^2
angle_alpha = 22 #gradi

#calcolo seno e coseno
cos_alpha = math.cos(math.radians(angle_alpha)) #converto l'angolo da gradi a radianti
sin_alpha = math.sin(math.radians(angle_alpha)) #converto l'angolo da gradi a radianti

print(cos_alpha)
print(sin_alpha)

#calcolo componenti
P = m * g
Px = P * sin_alpha
Py = P * cos_alpha

print(P)
print(Px)
print(Py)



