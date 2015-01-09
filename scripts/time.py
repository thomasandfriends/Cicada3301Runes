#!/usr/bin/python

import hashlib

import dparse
import dmanip
import dstats

def checkHashes(l, h):
        for i in l:
                cur = hashlib.sha512(i).hexdigest()
                if cur == h:
                        print "Found! " + i
                        return

        print "None found."

nums = [17, 13, 55, 1]
expHash = "36367763ab73783c7af284446c59466b4cd653239a311cb7116d4618dee09a8425893dc7500b464fdaf1672d7bef5e891c6e2274568926a49fb4f45132c2a8b4"

# Import timed files
t1Int = dparse.hexToInt(dparse.txtToHex(dparse.readFile("time1.hex")))
t2Int = dparse.hexToInt(dparse.txtToHex(dparse.readFile("time2.hex")))
t3Int = dparse.hexToInt(dparse.txtToHex(dparse.readFile("time3.hex")))
xored1 = dmanip.xor(t1Int, t2Int)
xored2 = dmanip.xor(xored1, t3Int)

# Import segag file
sSex = dparse.txtToSex(dparse.readFile("sexag.sex"))
sInt = dparse.sexToInt(sSex)
xored3 = dmanip.xor(xored2, sInt)

# tried:
# data1 = all raws, and xored t1+t2, t1+t2+t3, tn+sexag
# data1 mod 36
# (data1 + num[i]) mod 36 
# 

allLists = [t1Int, t2Int, t3Int, sInt, xored1, xored2, xored3]
total = []
for i in allLists:
        total.extend(i)

possTorEnc = dmanip.sepList(total, 16)
possTorInt = []

for i in range(len(possTorEnc)):
        curEnc = possTorEnc[i]
        tor = []
        for byte in curEnc:
                # IMPORTANT CODE
                cur = ((byte + nums[i%len(nums)]) % 32)
                # END

                tor.append(cur)

        possTorInt.append(tor)

possTor = [dparse.intToTor(i) for i in possTorInt]

print possTor

checkHashes(possTor, expHash)
