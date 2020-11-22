# -*- coding: utf-8 -*-
'''
A través de este script obtenemos el ancho y el alto del vídeo (en pixels) y el bitrate.
Ref:
    https://trac.ffmpeg.org/wiki/FFprobeTips
'''

import subprocess

print("Insert the name of the video (extension included): ")
inp = input()

string = 'ffprobe -v error -show_entries stream=width:stream=height:format=bit_rate -of default=noprint_wrappers=1 {}'.format(inp)

subprocess.call(string, shell=True)
