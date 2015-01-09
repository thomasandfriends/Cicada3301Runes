#!/usr/bin/python

import dparse
import dstats
import dmanip

# hRaw = dparse.readFile("time.hex")
# hHex = dparse.txtToHex(hRaw)
# hInt = dparse.hexToInt(hHex)
# 
# bRaw = dparse.readFile("binTest.bin")
# bBin = dparse.txtToBin(bRaw)
# bInt = dparse.binToInt(bBin)
# 
# # d1 = [15, 7, 3]
# # d2 = [2, 2, 2]
# # print dparse.intToBin(d1)
# # print dparse.intToBin(d2)
# # print dparse.intToBin(dmanip.xor(d1, d2))
# 
# print hHex
# print hInt
# print "-----"
# print bBin
# print dmanip.flipOrder(bBin)
# print dmanip.flipBits(bBin)
# 
# # print hInt[0:dstats.searchForBytes(hInt, [73, 254])

gRaw = dparse.readFile("../../../../Downloads/hello.gif")
gAsc = dparse.txtToAsc(gRaw)
gInt = dparse.ascToInt(gAsc)
gHex = dparse.intToHex(gInt)
dstats.magNumSearch(gHex)

print "---"


oRaw = dparse.readFile("../data/onion2.hex")
oHex = dparse.txtToHex(oRaw)
dstats.extMagNum(gHex)
