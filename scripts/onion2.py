#!/usr/bin/python

import dparse
import dstats
import dmanip

def createPictures():
        print "Reading file"
        raw = dparse.readFile("onion2.hex")

        print "Parsing"
        dHex = dparse.txtToHex(raw)
        dInt = dparse.hexToInt(dHex)
        dBin = dparse.intToBin(dInt)

        print "Flipping"
        dBinFlipped = dmanip.flipBits(dBin)

        for i in range(3):
                if i == 2:
                        dBinFlipped = dmanip.flipOrder(dBinFlipped)
                

                print "Searching"
                start = dstats.searchForBytes(dBinFlipped, dparse.intToBin(dparse.hexToInt(['FF', 'D8'])))
                end   = dstats.searchForBytes(dBinFlipped, dparse.intToBin(dparse.hexToInt(['FF', 'D9']))) + 2

                print "Separating: " + str(start) + ", " + str(end)
                iBin = dBinFlipped[start : end]
                
                print dBinFlipped[:5]
                print dBinFlipped[-5:]
                print "---"
                print iBin[:5]
                print iBin[-5:]
                print "---"
                
                dBinFlipped = dBinFlipped[end:] # Cut off beginning of file for next iteration
                iInt = dparse.binToInt(iBin)
                iAsc = dparse.intToAsc(iInt)

                print "Writing"
                outFile = open("../pics/out" + str(i) + ".jpg", 'w')
                outFile.write(iAsc)
                outFile.close()

        print "Done"

def exOutguess():
        from subprocess import call

        call("./outguess_all.sh")

def xorOutguess():
        data = []

        for i in range(3):
                cur = ""
                f = open("../outguesses/out" + str(i) + ".jpg.out", 'r')
                
                next(f); next(f)
                for line in f:
                        if line[:3] == "---":
                                break
                        else:
                                cur += line

                data.append(dparse.hexToInt(dparse.txtToHex(cur)))
        
        xored = dmanip.xor(data[0], dmanip.xor(data[1], data[2]))
        
        print dparse.intToAsc(xored)

createPictures()
exOutguess()
xorOutguess()
