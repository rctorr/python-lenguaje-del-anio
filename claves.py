#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choices

N = 3
L = 10

minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = minusculas.upper()
digitos = "1234567890"
simbolos = "#$%&/()=+-"

alf = minusculas + mayusculas + digitos + simbolos

for i in range(N):
    clave = choices(alf, k=L)
    clave = "".join(clave)
    print(clave)
