#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:47:55 2024

@author: ugte0917
"""

def nuskaityti_slaptazodzius():
    slaptazodziai = []
    f = open('testyou.txt', 'r', encoding="utf8", errors="ignore")
    for eilute in f:
        slaptazodis = eilute.strip()
        slaptazodziai.append(slaptazodis)
    return slaptazodziai

slaptazodziai = nuskaityti_slaptazodzius()
print(slaptazodziai)

