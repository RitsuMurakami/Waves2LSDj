import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import argparse
from PIL import Image

# args
parser = argparse.ArgumentParser(description="Hz to LSDj wave")
parser.add_argument("-f", help="name of csv file")
args = parser.parse_args()

if args.f == None:
    raise ValueError

# read csv file
df = pd.read_csv(args.f)
A = df['A'].values
f = df['f'].values

g = np.zeros((33, 33))

# Synthesise sin waves.
def wave(A, f, rad):
    x = 0
    for i, k in zip(A, f):
        x += i  * np.sin(k * rad)
    return x

# Drop sin waves into the LSDj wave grid.
def Cul(DIVIDER):
    for i in range(33):
        rad = 2 * np.pi * i / DIVIDER
        m = wave(A, f, rad)
        m = round(16 * m) + 16
        #m = math.ceil(16 * m) + 16
        if m > DIVIDER: m = DIVIDER
        g[m][i] = 1

def OutPut(DIVIDER):
    # y
    print(f'----DIVIDER: {DIVIDER} ----')
    for i in range(0, 33):
        p = str(i - 16).zfill(3)
        p += ' '
        # x
        for k in range(0, 32):
            if g[32 - i][k]:
                p += '■ '
            else:
                p += '□ '
        print(p)

# Output with several values
for i in range(5, 8):
    g = np.zeros((33, 33))
    Cul(2 ** i)
    OutPut(2 ** i)
