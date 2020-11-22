# -*- coding: utf-8 -*-
'''
A través de este script podemos cambiar la resolución de cualquier vídeo.
'''

import os
import subprocess

print("Insert the name of the video you want to resize (extension included): ")
inp = input()

print("Insert the new width: ")
w = input()

print("Insert the new height: ")
h = input()

name = os.path.splitext(inp)[0]  # Extraemos el nombre
ext = os.path.splitext(inp)[1]  # Extraemos la extension
oname = name + "_" + w + "x" + h + ext  # Cambiamos el nombre y añadimos extensión

string = 'ffmpeg -i {} -vf scale={}:{} {}'.format(inp, w, h, oname)

subprocess.call(string, shell=True)
