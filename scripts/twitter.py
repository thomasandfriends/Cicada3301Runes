#!/usr/bin/python

import dparse
import dstats
import dmanip

print "starting"

txt = ""
with open("../data/twitter.hex", 'r') as f:
        for line in f:
                if line[:3] == "Off":
                        continue
                txt += line[9:]

print "parsing"

tInt = dparse.hexToInt(dparse.txtToHex(txt))
sInt = dparse.ascToInt(dparse.txtToAsc(dparse.readFile("761.MP3")))

dstats.magNumSearch(sInt)

print len(tInt)
print len(sInt)

outFile = open("../pics/twitter.jpg", 'w')
outFile.write(dparse.intToAsc(dmanip.xor(tInt, sInt)))
outFile.close()

