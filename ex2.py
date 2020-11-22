# -*- coding: utf-8 -*-
'''
Con este script podemos cambiar el nombre de cualquier archivo
Ref:
    https://stackoverflow.com/questions/38596511/python-how-to-retain-the-file-extension-when-renaming-files-with-os
'''

import os

print("Insert the name of the file you want to change the name from (extension included): ")
name1 = input()

print("Insert the new name (without extension): ")
name2 = input()

oldext = os.path.splitext(name1)[1]  # Extraemos la extension
os.rename(name1, name2 + oldext)  # Cambiamos el nombre y añadimos extensión
