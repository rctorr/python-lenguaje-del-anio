#!/usr/bin/python
# -*- coding: utf-8 -*-

CIFRADO = "80 121 116 104 111 110 44 32 101 108 32 108 101 110 103 117 97 106 101 32 100 101 108 32 97 241 111 33"

msg = ""
for num in CIFRADO.split():
    msg = msg + chr(int(num))

print(msg)
