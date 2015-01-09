#!/usr/bin/python

import dparse
import dstats
import dmanip

def createPictures():
        print "Reading file"
        raw = dparse.readFile("onion5.hex")

        print "Parsing"
        dHex = dparse.txtToHex(raw)
        dInt = dparse.hexToInt(dHex)
        dBin = dparse.intToBin(dInt)
        
        print "Searching"
        start = dstats.searchForBytes(dHex, ['FF', 'D8', 'FF'])
        end   = dstats.searchForBytes(dHex, ['FF', 'D9']) + 2

        print "Separating: " + str(start) + ", " + str(end)
        iBin = dBin[start : end]
        
        iInt = dparse.binToInt(iBin)
        iAsc = dparse.intToAsc(iInt)

        print "Writing"
        outFile = open("../pics/2out0.jpg", 'w')
        outFile.write(iAsc)
        outFile.close()
       
        remains = dBin[end:]

        remains = dmanip.flipOrder(remains)
        rAsc = dparse.intToAsc(dparse.binToInt(remains))
        with open("../pics/2out1.jpg", 'w') as f:
                f.write(rAsc)

createPictures()
