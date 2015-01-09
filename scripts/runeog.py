#!/usr/bin/python

import os  
import dparse
import dstats
import dmanip

# Load all files
data = []

for fn in os.listdir('../outguesses/runebook'):
        print fn
        f = open("../outguesses/runebook/" + fn, 'r')
        cur = ""
        for line in f:
                cur += line
        
        data.append(dparse.ascToInt(dparse.txtToAsc(cur)))

print len(data)

relData = []

for i in data:
        if len(i) == 58152:
                relData.append(i)

print len(relData)

relData = [dparse.txtToAsc(i) for i in relData]

xored = relData[0]

for i in range(1, len(relData)):
        xored = dmanip.xor(xored, relData[i])

dstats.extMagNum(dparse.intToHex(xored))

with open("../data/xorrunes.asc", 'w') as f:
        f.write(dparse.intToAsc(xored))

# Search for suffs and prefs
# count = 2
# prevPref = 0
# prevSuff = 0
# while(True):
#         prefs = [', '.join([str(j) for j in i[:count]])  for i in data]
#         suffs = [', '.join([str(j) for j in i[-count:]]) for i in data]
#         
#         curPref = len(dstats.getFreq(prefs))
#         curSuff = len(dstats.getFreq(suffs))
# 
#         if curPref != prevPref:
#                 print "Pref change from " + str(prevPref) + " to " + str(curPref) + " at " + str(count)
# 
#         if curSuff != prevSuff:
#                 print "Suff change from " + str(prevSuff) + " to " + str(curSuff) + " at " + str(count)
#         
#         prevPref = curPref
#         prevSuff = curSuff
# 
#         count += 1
