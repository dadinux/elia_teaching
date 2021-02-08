#!/usr/bin/python3

user_input = float(input("Enter Number: "))

if user_input > 100:
    print("Greater")
elif user_input == 100:
    print("Is the same")
else:
    print("Smaller")