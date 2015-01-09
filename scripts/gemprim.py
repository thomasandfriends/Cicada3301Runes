#!/usr/bin/python
# -*- coding: utf-8 -*-

runeDict = [
        [2, "F", "ᚠ"],
        [3, "U", "ᚢ"],
        [5, "TH", "ᚦ"],
        [7, "O", "ᚩ"],
        [11, "R", "ᚱ"],
        [13, "C/K", "ᚳ"],
        [17, "G", "ᚷ"],
        [19, "W", "ᚹ"],
        [23, "H", "ᚻ"],
        [29, "N", "ᚾ"],
        [31, "I", "ᛁ"],
        [37, "J", "ᛂ"],
        [41, "EO", "ᛇ"],
        [43, "P", "ᛈ"],
        [47, "X", "ᛉ"],
        [53, "S/Z", "ᛋ"],
        [59, "T", "ᛏ"],
        [61, "B", "ᛒ"],
        [67, "E", "ᛖ"],
        [71, "M", "ᛗ"],
        [73, "L", "ᛚ"],
        [79, "NG/ING", "ᛝ"],
        [83, "OE", "ᛟ"],
        [89, "D", "ᛞ"],
        [97, "A", "ᚪ"],
        [101, "AE", "ᚫ"],
        [103, "Y", "ᚣ"], #
        [107, "IA/IO", "ᛡ"], #
        [109, "EA", "ᛠ"]
]

def primeToAsc(p):
        return changeList(p, 0, 1)

def primeToRune(p):
        return changeList(p, 0, 2)
        
def primeToInt(p):
        ret = []
        for i in p:
                index = 0
                for j in range(len(runeDict)):
                        if runeDict[j][0] == i:
                                index = j 
                                break
                ret.append(index)


        return ret

def ascToPrime(a):
        return [int(i) for i in changeList(p, 1, 0)]

def runeToPrime(r):
        return [int(i) for i in changeList(r, 2, 0)]      
 
def ascToStr(a):
        ret = ""
        
        for i in a:
                ret += str(i) + "-"

        return ret[:-1]

def intToPrime(i):
        ret = []
        
        for rune in i:
                ret.append(runeDict[rune][0])

        return ret

def changeList(p, x1, x2):
        ret = []
        
        for i in p:
                cur = "0"
                for j in runeDict:
                        if j[x1] == i:
                                cur = str(j[x2])
                                break
                
                ret.append(cur)

                #if cur == "0":
                #        print "No value found for " + str(ord(i[2]))

        return ret
