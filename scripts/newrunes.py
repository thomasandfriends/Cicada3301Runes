#!/usr/bin/python

import dparse
import dstats
import dmanip

raw1 = ""

with open("../outguesses/2out0.jpg.out", 'r') as f:
        for i in range(9):
                next(f)

        for line in f:
                if line[:3] == "---":
                        break
                
                raw1 += line

#raw2 = dparse.readFile("../outguesses/2out1.jpg.out")

h1Hex = dparse.txtToHex(raw1)
h1Int = dparse.hexToInt(h1Hex)
h1Asc = dparse.intToAsc(h1Int)

with open("../pics/newrunes.jpg", 'w') as f:
        f.write(h1Asc)
