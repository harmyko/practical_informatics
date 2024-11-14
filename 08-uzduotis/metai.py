#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:39:36 2024

@author: ugte0917
"""

from collections import Counter

f = open("Metai.txt", "r", encoding="utf8")

def pasalinkSkyrybosZenklus(eilute):
    skyrybosZenklai = "-–—„“.,!?:(;)"
    for simbolis in skyrybosZenklai:
        eilute = eilute.replace(simbolis, " ")
    return eilute

def raskIlgiausiaZodi(zodziaiFiltruoti):
    maxIlgis = 0
    for zodis in zodziaiFiltruoti:
        if len(zodis) >= maxIlgis:
            maxIlgis = len(zodis)
            ilgiausiasZodis = zodis
    return ilgiausiasZodis

def raskZodziuDazni(zodziaiFiltruoti):
    zodziuDazniai = Counter(zodziaiFiltruoti)
    surikiuotiPagalDazni = zodziuDazniai.most_common()
    isvestis = '\n'.join([f"{i + 1}. '{zodis}': {daznis}" for i, (zodis, daznis) in enumerate(surikiuotiPagalDazni[:100])])
    return isvestis

zodziai = []
for eilute in f:
    eilute = pasalinkSkyrybosZenklus(eilute)
    eilute = eilute.strip().split(" ")
    zodziai += eilute
    
zodziaiFiltruoti = []
for zodis in zodziai:
    zodis = zodis.lower()
    if len(zodis) > 0 and zodis.isalpha():
        zodziaiFiltruoti.append(zodis)
        
ilgiausiasZodis = raskIlgiausiaZodi(zodziaiFiltruoti)
print("Ilgiausias rastas žodis: " + ilgiausiasZodis)

zodziuSkaicius = len(zodziaiFiltruoti)
print("Apskaičiuotas žodžių skaičius: " + str(zodziuSkaicius))

dazniai = raskZodziuDazni(zodziaiFiltruoti)
print("Dažniausiai naudojami žodžiai: " + dazniai)
    