#!/usr/bin/python

import dparse
import dmanip
import dstats

txt = ""

with open("../data/new.txt", 'r') as f:
        next(f); next(f)

        for line in f:
                if line[:3] == "---":
                        break
                txt += line
                print len(line)

bRaw = ""

for c in txt:
        if c == '\t':
                bRaw += "1"
        elif c == ' ':
                bRaw += "0"

        

print dparse.intToAsc(dparse.binToInt(dparse.txtToBin(bRaw)))
