#!/usr/bin/python

# TODO: flip order, flip bits

import math
import dparse

def sepList(l, n):
        ret = []

        for i in range(int(math.ceil(len(l)/n))+1): # Create list with right amount of lists
                ret.append([])

        for i in range(len(l)): # Add items to appropriate list
                ret[int(math.floor(i/n))].append(l[i])
        
        return ret

def sepStr(s, n):
        ret = []
        
        for i in range(len(s)/n):
                ret.append(s[i*n : ((i+1)*n)])

        return ret


def xor(i1, i2):
        ret = []

        size = 0
        if len(i1) < len(i2):
                size = len(i1)
        else:
                size = len(i2)

        for i in range(size):
                ret.append(i1[i] ^ i2[i])

        return ret

# Put data into an image
def castToImage(data, x, y):
        sepInts = seperateList(data, 1) # Separate data into groups of 4 (RGBA)
        img = Image.new('RGB', (x, y), "black") # Create a new black image
        pixels = img.load() # Create the pixel map

        for i in range(x): # For every pixel:
                for j in range(y):
                        color = sepInts[(i*x) + j]
                        pixels[i,j] = (color[0], color[0], color[0]) # Set the colour accordingly

        img.save("/home/misha/Dropbox/3301/2015/misc/dataout.bmp", "bmp")

def flipBinOrder(b):
        ret = []

        for i in range(len(b)):
                ret.append(b[len(b) - i - 1][::-1])

        return ret

def flipOrder(d):
        return d[::-1]

def flipBits(b):
        ret = []

        i = dparse.binToInt(b)
        
        for byte in i:
                ret.append(xor([byte], [255])[0])
        
        return dparse.intToBin(ret)
