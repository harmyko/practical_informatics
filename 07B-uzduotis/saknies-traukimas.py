#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:27:18 2024

@author: ugte0917
"""

import sys

skaiciusMin = -10000
skaiciusMax = 10000

def patikrinkRezius(skaicius, skaiciusMin, skaiciusMax):
    if skaicius > skaiciusMax:
        print("Įvestas skaičius negali virsyti reikšmės", str(skaiciusMax) + ".")
        sys.exit(0)
    if skaicius < skaiciusMin:
        print("Įvesto skaičiaus reikšmė negali būti mažesnė už", str(skaiciusMin) + ".")
        sys.exit(0)
        
def paverskSkaiciumi(ivestis):
    skaicius = None
    try:
        skaicius = int(ivestis)
    except ValueError:
        pass
    return skaicius

def patikrinkSkaiciu(skaicius):
    verte = paverskSkaiciumi(skaicius)
    if verte == None:
        print("Privaloma įvesti sveikąjį skaičių!")
        sys.exit(0)
    return verte

print("N-tojo laipsnio šaknies traukimo iš skaičiaus programa.")
daugiklis = input("Įveskite daugiklį prieš laipsnį (1 jei nėra): ")
daugiklis = patikrinkSkaiciu(daugiklis)
patikrinkRezius(daugiklis, skaiciusMin, skaiciusMax)
laipsnis = input("Įveskite šaknies laipsnį: ")
laipsnis = patikrinkSkaiciu(laipsnis)
patikrinkRezius(laipsnis, 2, skaiciusMax)
posaknis = input("Įveskite pošaknį: ")
posaknis = patikrinkSkaiciu(posaknis)
if laipsnis % 2 == 0:
    patikrinkRezius(posaknis, 0, skaiciusMax)
else:
    patikrinkRezius(posaknis, skaiciusMin, skaiciusMax)
    
if posaknis < 0:
    print(daugiklis, "*", laipsnis, "√", "(" + str(posaknis) + ")")
else:
    print(daugiklis, "*", laipsnis, "√", posaknis)
    
