#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:47:55 2024

@author: ugte0917
"""

import hashlib

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

slaptazodziai = nuskaityti_slaptazodzius()

sha256_checksum = "4b529ac375b4217be17fef1a4a6f1624185cc99909e92278c0759e12ab3d61fa"
slaptazodis,patikrinta_slaptazodziu_skaicius = rasti_slaptazodi_pagal_hash(sha256_checksum, slaptazodziai)
print(slaptazodis,patikrinta_slaptazodziu_skaicius)

