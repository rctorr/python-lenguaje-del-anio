#!/usr/bin/python
# -*- coding: utf-8 -*-

MSG = "Python, el lenguaje del año!"

cifrado = ""
for letra in MSG:
    cifrado = cifrado + str(ord(letra)) + " "

print(cifrado)
