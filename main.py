# -*- coding: utf-8 -*-
'''
Este es el script principal.
'''

import os
import sys


def enunciado():
    print("\nIntroduce un número para realizar una de las siguientes operaciones en un vídeo:")
    print("\n[1]: Ver resolución y bit rate.")
    print("\n[2]: Cambiar el nombre.")
    print("\n[3]: Cambiar la resolución.")
    print("\n[4]: Cambiar codec de audio y/o vídeo.")
    print("\n[0]: Exit")
    x = input()

    return x


while (True):
    x = enunciado()
    print(x)

    if x == "1":
        os.system("python3 ex1.py")
    elif x == "2":
        os.system("python3 ex2.py")
    elif x == "3":
        os.system("python3 ex3.py")
    elif x == "4":
        os.system("python3 ex4.py")
    elif x == "0":
        sys.exit()
    else:
        print('Introducir opción válida')
