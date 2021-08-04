# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:25:34 2021

@author: amey
"""

import colorsys

r = 255
g = 255
b = 0

print(r)
print(g)
print(b)

r = r/255
g = g/255
b = b/255

hls = colorsys.rgb_to_hls(r, g, b)

hue = hls[0]

print('hue:' + str(hue))