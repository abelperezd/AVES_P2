# -*- coding: utf-8 -*-
'''
Ref:
    https://www.youtube.com/watch?v=1ymYwSQFodU
'''

import os
import subprocess


print("Would you like to see a list of the possible audio and video codecs?")
print("any: No  -  1: Yes")
codec_list = input()

if codec_list == "1":
    subprocess.call('ffmpeg -codecs', shell=True)

print("Insert the name of the original video (extension included): ")
inp = input()

print("Insert the new video codec (insert \"copy\" to keep the original): ")
v = input()
if v == "copy":
    v_ = ""  # variable para introducir en el nombre y no poner copy
else:
    v_ = v

print("Insert the new audio codec (insert \"copy\" to keep the original): ")
a = input()
if a == "copy":
    a_ = ""  # variable para introducir en el nombre y no poner copy
else:
    a_ = a

name = os.path.splitext(inp)[0]  # Nombre original
ext = os.path.splitext(inp)[1]  # Extraemos la extension

oname = name + "_" + v_ + "_" + a_ + ext  # Cambiamos el nombre y añadimos extensión

string = 'ffmpeg -i {} -c:v {} -c:a {} {}'.format(inp, v, a, oname)

subprocess.call(string, shell=True)
