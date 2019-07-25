#!/usr/bin/python
# -*- coding: utf-8 -*-

MSG = "Me van a cifrar usando el método César"
LLAVE = 5

cifrado = ""
for letra in MSG:
    cifrado = cifrado + str(ord(letra)+LLAVE) + " "

print(cifrado)
