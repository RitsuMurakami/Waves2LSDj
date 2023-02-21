import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


def wave(A, f, rad):
    x = 0
    for i, k in zip(A, f):
        x += i  * np.sin(k * rad)
    return x

df = pd.read_csv('i.csv')
A = df['A'].values
f = df['f'].values

DIVIDER = 128
g = np.zeros((33, 33))

A = [0.07, 0.09, 0.08, 0.19, 0.08]
f = [260, 520, 780, 1040, 1300]

for i in range(33):
    rad = 2 * np.pi * i / DIVIDER
    m = wave(A, f, rad)
    m = int(16 * m) + 16
    if m > DIVIDER: m = DIVIDER
    g[m][i] = 1

# y
for i in range(0, 33):
    p = str(i - 16).zfill(3)
    p += ' '
    # x
    for k in range(0, 33):
        if g[32 - i][k]:
            p += '■ '
        else:
            p += '□ '
    print(p)

