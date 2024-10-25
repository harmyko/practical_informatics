#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def arPirminis(skaicius):
    dalinasi = 0
    for i in range(1, skaicius + 1):
        if skaicius % i == 0:
            dalinasi += 1
        if dalinasi == 3:
            return False
    return True

def ieskotiPirminiu(pradzia, pabaiga):
    for i in range(pradzia, pabaiga + 1):
        if arPirminis(i) == True:
            print(i)
    pass

def paversti_i_skaiciu(ivestis):
    skaicius = None
    try:
        skaicius = int(ivestis)
    except ValueError:
        pass
    return skaicius

def patikrinti_skaiciu(skaicius):
    verte = paversti_i_skaiciu(skaicius)
    if verte == None:
        print("Privaloma įvesti sveikąjį skaičių.")
        sys.exit(0)
    if verte < 1:
        print("Privaloma įvesti teigiamą skaičių.")
        sys.exit(0)
    return verte

print("Pirminių skaičių paieškos programa.")
print("Programa ras pirminius skaičius nurodytame intervale.")
skaicius_nuo = input("Įveskite intervalo pradžią: ")
skaicius_nuo = patikrinti_skaiciu(skaicius_nuo)
skaicius_iki = input("Įveskite intervalo pabaigą: ")
skaicius_iki = patikrinti_skaiciu(skaicius_iki)
if skaicius_nuo > skaicius_iki:
    tmp = skaicius_nuo
    skaicius_nuo = skaicius_iki
    skaicius_iki = tmp
print("Pirminių skaičių ieškoma intervale [" + str(skaicius_nuo) + ", " +str(skaicius_iki) + "]")
ieskotiPirminiu(skaicius_nuo, skaicius_iki)



