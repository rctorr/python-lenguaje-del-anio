#!/usr/bin/python
# -*- coding: utf-8 -*-

CIFRADO = "82 106 37 106 115 104 102 115 121 102 37 85 126 121 109 116 115 37 126 37 118 122 110 106 119 116 37 121 116 114 102 119 37 122 115 37 104 122 119 120 116 37 106 115 37 71 106 105 122"
LLAVE = 5

msg = ""
for num in CIFRADO.split():
    msg = msg + chr(int(num))

print(msg)
