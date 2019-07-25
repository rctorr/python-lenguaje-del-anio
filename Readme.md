## Python, el lenguaje del año!

### Herrammientas

Para la instalación del lenguaje de programación Python

- Python en base a miniconda https://docs.conda.io/en/latest/miniconda.html
- Python oficial https://www.python.org/

Para la elección e instalación de un editor de código:

- Atom https://atom.io/
- Sublime text https://www.sublimetext.com/
- Notepad++ https://notepad-plus-plus.org/
- VS Code https://code.visualstudio.com/
- Vim, Emacs

### CASO 1: Primeros pasos en Python (Hola mundo)

__Descripción:__ Crear un programa en el lenguaje de programación Python que imprima en la pantalla el mensaje "Hola Mundo".

__Desarrollo:__
1. Crear una carpeta llamada `WSPython`
1. Abrir el editor de código de tu preferencia y crear un nuevo documento
1. Guardar el documento con el nombre `hola-mundo.py` en la carpeta `WSPython`
1. Escribir el siguiente código y guardar el documento:
   ```python
   #!/usr/bin/python
   # -*- coding: utf-8 -*-

   print("Hola Mundo!")
   ```
1. Para ejecutar el programa abrir una terminal o consola:
  - En Max OS y Linux abrir la aplicación terminal
  - En Windows abrir el Anaconda Promot si se ha instalado miniconda o un Consola de comandos si se ha instalado Python Oficial.

1. Cambiarse a la carpeta `WSPython` y ejecutar el siguiente comando:
   ```console
   $ cd WSPython
   WSPython $ python hola-mundo.py
   Hola Mundo!

   WSPython $
   ```

__FELICIDADES, ACABAS DE ESCRIBIR TU PRIMER PROGRAMA EN PYTHON__

### CASO 2: Primeros pasos en programación (generando claves)

__Descripción:__ Crear un programa en el lenguaje de programación Python que imprima N claves de L letras (caracteres) de longitud. Ejemplo, si N=3 y L=10 el resultado debe ser similar a:

   ```console
   WSPython $ python claves.py
   speXAzrJfk
   KBKAvSSnxZ
   ztFMicgvmo
   ```

__Desarrollo:__
1. En el editor de código crear un nuevo documento
1. Guardar el documento con el nombre `claves.py` en la carpeta `WSPython`
1. Escribir el siguiente código y guardar el documento:
   ```python
   #!/usr/bin/python
   # -*- coding: utf-8 -*-

   from random import choices

   N = 3
   L = 10

   minusculas = "abcdefghijklmnopqrstuvwxyz"
   mayusculas = minusculas.upper()

   alf = minusculas + mayusculas

   for i in range(N):
       clave = choices(alf, k=L)
       clave = "".join(clave)
       print(clave)
  ```

1. Para ejecutar el programa en la terminal o consola ejecutar el comando:
   ```console
   WSPython $ python claves.py
   speXAzrJfk
   KBKAvSSnxZ
   ztFMicgvmo

   WSPython $
   ```

__AHORA CON LA AYUDA DE PYTHON YA NO TIENES PRETEXTO PARA USAR CLAVES SEGURAS ¿CIERTO?__

### RETO 1: Primeros pasos en programación (generando claves un poco más seguras)

__Descripción:__ Modificar el script `claves.py` para que las claves incluyan dígitos y algunos símbolos. Por ejemplo:

   ```console
   WSPython $ python claves.py
   mNSYl/kbIg
   s(qy(i--&B
   %Wg)z&lobM
   ```

__Desarrollo:__
1. En el editor de código abrir el archivo `claves.py`
1. Realizar las modificaciones ...
   ```python

   minusculas = "abcdefghijklmnopqrstuvwxyz"
   mayusculas = minusculas.upper()
   # tus modificaciones

   alf = minusculas + mayusculas  # tus modificaciones

   for i in range(N):
       clave = choices(alf, k=L)
       clave = "".join(clave)
       print(clave)
  ```

1. Para ejecutar el programa en la terminal o consola ejecutar el comando:
   ```console
   WSPython $ python claves.py
   mNSYl/kbIg
   s(qy(i--&B
   %Wg)z&lobM

   WSPython $
   ```

__AHORA YA NO TIENES PRETEXTO PARA USAR CLAVES UN POCO MÁS SEGURAS__

### CASO 3: Python en la seguridad (cifrando y descifrando)

__Descripción:__ Crear un programa en el lenguaje de programación Python que dado un mensaje de texto lo cifre asignando un número a cada letra, por lo que el resultado final será un mensaje conteniendo solamente números, por ejemplo:

   ```console
   WSPython $ python cifra.py
   80 121 116 104 111 110 44 32 101 108 32 108 101 110 103 117 97 106 101 32 100 101 108 32 97 241 111 33
   ```

__Desarrollo:__
1. En el editor de código crear un nuevo documento
1. Guardar el documento con el nombre `cifra.py` en la carpeta `WSPython`
1. Escribir el siguiente código y guardar el documento:
   ```python
   #!/usr/bin/python
   # -*- coding: utf-8 -*-

   MSG = "Python, el lenguaje del año!"

   cifrado = ""
   for letra in MSG:
       cifrado = cifrado + str(ord(letra)) + " "

   print(cifrado)
  ```

1. Para ejecutar el programa en la terminal o consola ejecutar el comando:
   ```console
   WSPython $ python cifra.py
   80 121 116 104 111 110 44 32 101 108 32 108 101 110 103 117 97 106 101 32 100 101 108 32 97 241 111 33

   WSPython $
   ```

### RETO 2: Python en la seguridad (cifrando y descifrando)

__Descripción:__ Crear un programa en el lenguaje de programación Python que dado un mensaje cifrado en números, descifre el mensaje oculto y lo imprima en pantalla, por ejemplo:

   ```console
   WSPython $ python descifra.py
   Python, el lenguaje del año!
   ```

__Desarrollo:__
1. En el editor de código crear un nuevo documento
1. Guardar el documento con el nombre `descifra.py` en la carpeta `WSPython`
1. Escribir el código que resuelva el reto:
   ```python
   #!/usr/bin/python
   # -*- coding: utf-8 -*-

   CIFRADO = "80 121 116 104 111 110 44 32 101 108 32 108 101 110 103 117 97 106 101 32 100 101 108 32 97 241 111 33"

   msg = ""
   # tu código aquí

   print(msg)
  ```

1. Para ejecutar el programa en la terminal o consola ejecutar el comando:
   ```console
   WSPython $ python descifra.py
   Python, el lenguaje del año!

   WSPython $
   ```

### RETO FINAL: Python en la seguridad (cifrando y descifrando)

__Descripción:__ Encontrar el mensaje oculto en los siguientes números:

   ```
   82 106 37 106 115 104 102 115 121 102 37 85 126
   121 109 116 115 37 126 37 118 122 110 106 119 116
   37 121 116 114 102 119 37 122 115 37 104 122 119
   120 116 37 106 115 37 71 106 105 122
   ```

   Considerando que la llave de cifrado es 5.

__Medalla al primero que lo descifre__
