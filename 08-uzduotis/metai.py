#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:39:36 2024

@author: ugte0917
"""

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
print(ilgiausiasZodis)
    