#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:27:18 2024

@author: ugte0917
"""

import sys

SKAICIUS_MIN = -10000
SKAICIUS_MAX = 10000

def patikrinkRezius(skaicius, skaiciusMin, skaiciusMax):
    if skaicius > skaiciusMax:
        print("Klaida: Įvestas skaičius negali virsyti reikšmės", str(skaiciusMax) + ".")
        sys.exit(0)
    if skaicius < skaiciusMin:
        print("Klaida: Įvesto skaičiaus reikšmė negali būti mažesnė už", str(skaiciusMin) + ".")
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
        print("Klaida: Privaloma įvesti sveikąjį skaičių!")
        sys.exit(0)
    return verte

print("N-tojo laipsnio šaknies traukimo iš skaičiaus programa. Įveskite šiuos duomenis:")
print("Daugiklį prieš šaknį a, šaknies laipsnį n ir pošaknį b")
daugiklis = input("Įveskite daugiklį prieš šaknį a: ")
daugiklis = patikrinkSkaiciu(daugiklis)
patikrinkRezius(daugiklis, SKAICIUS_MIN, SKAICIUS_MAX)
laipsnis = input("Įveskite šaknies laipsnį n: ")
laipsnis = patikrinkSkaiciu(laipsnis)
patikrinkRezius(laipsnis, 2, SKAICIUS_MAX)
posaknis = input("Įveskite pošaknį b: ")
if (laipsnis % 2 == 0) and (int(posaknis) < 0):
    print("Klaida: Iš lyginio skaičiaus laipsnio šaknies galime ištraukti tik neneigiamą pošaknį!") 
    sys.exit(0)
posaknis = patikrinkSkaiciu(posaknis)
if laipsnis % 2 == 0:
    patikrinkRezius(posaknis, 0, SKAICIUS_MAX)
else:
    patikrinkRezius(posaknis, SKAICIUS_MIN, SKAICIUS_MAX)
    
if posaknis < 0:
    print("Jūsų įvesta sąlyga:", daugiklis, "*", laipsnis, "√", "(" + str(posaknis) + ")")
else:
    print("Jūsų įvesta sąlyga:", daugiklis, "*", laipsnis, "√", posaknis)
    
posaknioModulis = abs(posaknis)
potencialiSaknis = 0
atsakymasGautas = 0
neigiamas = 0

if posaknis == -1:
    saknis = -1
    atsakymasGautas = 1
elif posaknis == 1:
    saknis = 1
    atsakymasGautas = 1
elif posaknis == 0:
    saknis = 1
    atsakymasGautas = 1
else:
    for i in range(2, posaknioModulis - 1):
        potencialiSaknis = i ** laipsnis
        temp = potencialiSaknis
        while potencialiSaknis < posaknioModulis:
            temp = potencialiSaknis
            potencialiSaknis *= (i ** laipsnis)
        if potencialiSaknis == posaknioModulis:
            if posaknis < 0:
                neigiamas = 1
            posaknis = 0
            atsakymasGautas = 1
            break
            
        potencialiSaknis = temp
        for j in range(potencialiSaknis - 1, 1, -1):
            if potencialiSaknis * j == posaknioModulis:
                if posaknis < 0:    
                    posaknis = -j 
                    neigiamas = 1
                    break
                else:
                    posaknis = j
                    atsakymasGautas = 1
                    break
            
            if atsakymasGautas == 1:
                break
        
        if atsakymasGautas == 1:
            break
    
    if atsakymasGautas == 1:
        saknis = potencialiSaknis ** (1 / laipsnis)
        saknis = int(round(saknis, 1))

if atsakymasGautas == 1:
    daugiklis *= saknis
    
if neigiamas == 1:
    daugiklis *= -1

if posaknis == 0:
    print("Gautas rezultatas:", daugiklis)
    sys.exit(0)
if daugiklis == 1 and posaknis > 0:
    print("Gautas rezultatas:", laipsnis, "√", posaknis)
    sys.exit(0)
else:
    if posaknis < 0:
        print("Gautas rezultatas:", daugiklis, "*", laipsnis, "√", "(" + str(posaknis) + ")")
    else:
        print("Gautas rezultatas:", daugiklis, "*", laipsnis, "√", posaknis)
                
            
    