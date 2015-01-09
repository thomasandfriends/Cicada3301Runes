#!/usr/bin/python

# All data should be in arrays of *bytes*
# So: bin - 8, hex - 2, asc - 1, sex - 2, int - number less than 256.

# Bin and asc should be in string format, so without 0x or 0b beforehand.

# TODO:
# Split - parsing, stats(counts, pics), manipulation(xor)

import math
import dmanip

# Misc. functions:

def readFile(path):
        ret = ""
        f = open("../data/" + path, 'r')
        for line in f:
                ret += line

        return ret

def dataToTxt(d):
        ret = ""
        
        size = 0
        if d[1] == 'x':
                size = 2
        elif d[1] == 'b':
                size = 8
        else:
                print "Not recognised"
                return []
        
        ret = d[2:]

        while(len(ret) < size):
                ret = "0" + ret
        
        return ret

# Converting text to data:

def txtToBin(t):
        for c in t:
                if c != '0' and c != '1':
                        t = t.replace(c, "")
        
        return dmanip.sepStr(t, 8)

def txtToHex(t): # TODO VERY slow, could just be this one
        t = t.lower()
        for c in t:
                if not (('0' <= c <= '9') or ('a' <= c <= 'f')):
                        t = t.replace(c, "")
        
        return dmanip.sepStr(t, 2)

def txtToAsc(t):
        return t

def txtToSex(t):
        for c in t:
                if not (('0' <= c <= '9') or ('A' <= c <= 'Z') or ('a' <= c <= 'x')):
                        t = t.replace(c, "")
        
        return dmanip.sepStr(t, 2)

# Converting data to ints:

def binToInt(b):
        ret = []
        for byte in b:
                ret.append(int(byte, 2))

        return ret

def hexToInt(h):
        ret = []
        for byte in h:
                ret.append(int(byte, 16))

        return ret

def ascToInt(a):
        ret = []
        for byte in a:
                ret.append(ord(byte))

        return ret

def sexToInt(s):
        ret = []
        for byte in s:
                cur = (int(byte[0])) * 60 # First int is worth 60

                if('0' <= byte[1] and byte[1] <= '9'):
                        cur += ord(byte[1]) - ord('0') # 0-9 is worth 0-9

                if('A' <= byte[1] and byte[1] <= 'Z'):
                        cur += ord(byte[1]) - ord('A') + 10 # A-Z is worth 10-36

                if('a' <= byte[1] and byte[1] <= 'z'):
                        cur += ord(byte[1]) - ord('a') + 26 + 10 # a-x is worth 36-60

                ret.append(cur)

        return ret

# Converting ints to data:

def intToBin(i):
        ret = []
        for byte in i:
                ret.append(dataToTxt(bin(byte)))
        
        return ret

def intToHex(i):
        ret = []
        for byte in i:
                ret.append(dataToTxt(hex(byte)))
        
        return ret

def intToAsc(i):
        ret = ""
        for byte in i:
                ret += chr(byte)
        
        return ret

def intToSex(i):
        print "Haven't done intToSex"

def intToTor(i):
        ret = ""
        
        for byte in i:
                if byte < 6:
                        ret += chr(byte + ord('2'))
                else:
                        ret += chr(byte + ord('a') - 6)

        return ret
