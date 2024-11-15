#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:47:55 2024

@author: ugte0917
"""

import hashlib
import time

def skaiciuoti_sha256(slaptazodis):
    encoded_slaptazodis = slaptazodis.encode()
    return hashlib.sha256(encoded_slaptazodis).hexdigest()

def nuskaityti_slaptazodzius():
    slaptazodziai = []
    f = open('testyou.txt', 'r', encoding="utf8", errors="ignore")
    for eilute in f:
        slaptazodis = eilute.strip()
        slaptazodziai.append(slaptazodis)
    return slaptazodziai

def rasti_slaptazodi_pagal_hash(sha256_checksum, slaptazodziai):
    patikrinta_slaptazodziu_skaicius = 0
    slaptazodis = "Nerasta"
    for zodis in slaptazodziai:
        patikrinta_slaptazodziu_skaicius += 1
        if skaiciuoti_sha256(zodis) == sha256_checksum:
            slaptazodis = zodis
            break
    return slaptazodis,patikrinta_slaptazodziu_skaicius

def apskaiciuoti_hashrate(patikrinta_slaptazodziu_skaicius, uzimtas_laikas):
    if uzimtas_laikas > 0:
        return patikrinta_slaptazodziu_skaicius / uzimtas_laikas
    return 0

def apskaiciuoti_stipraus_slaptazodzio_nulauzimo_laika(hashrate):
    imanomu_slaptazodziu_skaicius = 95 ** 8
    laikas_nulauzti_sekundemis = imanomu_slaptazodziu_skaicius / hashrate
    laikas_nulauzti_metais = laikas_nulauzti_sekundemis / (365*24*60*60)
    return laikas_nulauzti_metais

slaptazodziai = nuskaityti_slaptazodzius()

sha256_checksum = "4b529ac375b4217be17fef1a4a6f1624185cc99909e92278c0759e12ab3d61fa"
pradzios_laikas = time.time()
slaptazodis,patikrinta_slaptazodziu_skaicius = rasti_slaptazodi_pagal_hash(sha256_checksum, slaptazodziai)
pabaigos_laikas = time.time()
uzimtas_laikas = pabaigos_laikas - pradzios_laikas
hashrate = apskaiciuoti_hashrate(patikrinta_slaptazodziu_skaicius, uzimtas_laikas)
stipraus_slaptazodzio_nulauzimo_laikas = apskaiciuoti_stipraus_slaptazodzio_nulauzimo_laika(hashrate)
print("Rastas slaptažodis: " + slaptazodis)
print("Prastą slaptažodį atspėjome per: " + str(uzimtas_laikas) + " sekundžių.")
print("Galime patikrinti: " + str(hashrate) + " slaptažodžių per sekundę")
print("Stiprų 8 simbolių slaptažodį užtruktų nulaužti su esama įranga: " + str(stipraus_slaptazodzio_nulauzimo_laikas) + " metų")

