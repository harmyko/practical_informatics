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

slaptazodziai = nuskaityti_slaptazodzius()
print(skaiciuoti_sha256("labas"))

