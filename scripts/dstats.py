#!/usr/bin/python

import operator

import dparse
import dmanip

def allStats(i):
        h = dparse.intToHex(i)

        print "=== EXT MAGIC NUMBERS ==="
        extMagNum(h)
        print ""

        print "=== FREQUENCIES ==="
        graphDict(i)
        print ""

        print "=== UNUSED ==="
        print getUnused(i) 

def getFreq(l):
	count = {}
	
	for i in l:
		if i in count:
                	count[i] = count[i] + 1
               	else:
               		count[i] = 1
        
        return count

def printDict(d, sort):
        total = 0.0
        longestStr = 0
        for key in d:
                total += d[key]
                if len(str(key)) > longestStr:
                        longestStr = len(str(key))
        
        
	for i in sorted(d.items(), key=operator.itemgetter(sort)):
                key = str(i[0])
                
                # Make sure keys are same length for niceness
                while len(key) < longestStr:
                        key = " " + key

                # Print it out
		print str(key) + " - {0:.3f}".format(float((i[1]) / total)) + " - " + str(i[1])
                


def graphDict(d, sort):
        total = 0.0
        longestStr = 0
        for key in d:
                total += d[key]
                if len(str(key)) > longestStr:
                        longestStr = len(str(key))
        
        
	for i in sorted(d.items(), key=operator.itemgetter(sort)):
		xs = ""
		
                # Add right amount of X's
                for j in range(int((float(i[1]) / total) * 300.0)):
			xs += "X"
                
                key = str(i[0])
                
                # Make sure keys are same length for niceness
                while len(key) < longestStr:
                        key = " " + key

                # Print it out
		print str(key) + " " + xs

def printFreq(l, sort):
        printDict(getFreq(l), sort)

def graphFreq(l, sort):
        graphDict(getFreq(l), sort)

def getUnused(i):
        unused = range(256)
        for byte in i:
                if byte in unused:
                        unused.remove(byte)
        return unused

def searchForBytes(d, bs):
        for i in range(len(d) - len(bs) + 1):
                match = True
                for j in range(len(bs)):
                        if (d[i+j] != bs[j]):
                                match = False
                                break
                if match:
                        return i
        return -1

magNums = [
["mp4(1)", "00 00 00 nn 66 74 79 70"],
["mp4(2)", "33 67 70 35"],
["gif(1)", "47 49 46 38 37 61"],
["gif(2)", "47 49 46 38 39 61"],
["jpg",    "FF D8 FF"],
["exe",    "4D 5A"],
["zip(empt)", "50 4B 03 04, 50 4B 05 06"],
["zip(span}", "50 4B 07 08"],
["rar(1.5)", "52 61 72 21 1A 07 00"],
["rar(5.0)", "52 61 72 21 1A 07 01 00"]]

def magNumSearch(h):
        found = False
        for mn in magNums:
                mHex = dparse.txtToHex(mn[1])
                i = searchForBytes(h, mHex)
                if i != -1:
                        print "FOUND " + mn[0] + " AT " + str(i)
                        found = True

        if not found:
                print "Nothing found"

def extMagNum(h):
        print "Creating flipped data"
        i = dparse.hexToInt(h)
        b = dparse.intToBin(i)
        bFlip = dmanip.flipBits(b)
        bRev = dmanip.flipBinOrder(b)
        bRevFlip = dmanip.flipBits(bRev)
        
        hFlip = dparse.intToHex(dparse.binToInt(bFlip))
        hRev = dparse.intToHex(dparse.binToInt(bRev))
        hRevFlip = dparse.intToHex(dparse.binToInt(bRevFlip))
        
        print "> Searching normal"
        magNumSearch(h)

        print "> Searching flipped bits"
        magNumSearch(hFlip)

        print "> Searching reversed order"
        magNumSearch(hRev)

        print "> Searching flipped bits and reversed order"
        magNumSearch(hRevFlip)
