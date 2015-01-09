#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import enchant
import operator

import dparse
import dstats
import dmanip
import gemprim
import simple_crypto

import rkeys
import rappls

eng = enchant.Dict("en_US")

def tryDecrypt(p, k, s, a):
        plainPage = []
        count = 0
        for word in pages[p]:
                plainWord = []
                for char in word:
                        key = rkeys.allKeys[k]
                        newChar = rappls.allAppls[a](char, key[count % len(key)], s)
                        plainWord.append(newChar)
                        #print str(char) + " = " + str(newChar)
                        count += 1
                plainPage.append(plainWord)

        print [gemprim.ascToStr(gemprim.primeToAsc(gemprim.intToPrime(word))) for word in plainPage]

def getEng(page):
        txtPage = [gemprim.primeToAsc(gemprim.intToPrime(word)) for word in page] 
        engPage = []
        
        for word in txtPage:
                curWord = ""
                for letter in word:
                        for c in letter:
                                if c == "/":
                                        break
                                curWord += c
                engPage.append(curWord.lower())
        
        correct = 0
        for word in engPage:
                if word != '' and len(word) > 1 and eng.check(word):
                        correct += 1
                        if len(word) > 6:
                                print word
                        #print word
                if word in ["pilgrim", "instar", "fibonacci", "prime", "primes", "emerge", "cicada", "onion", "sacred"]:
                        print word
      return float(correct)/float(len(engPage))

def bruteOut(s):
        if s[5] != ">":
                print s

print eng.check("instar")

raw = "" #dparse.readFile("runes.rune.old")

with open("../data/runes.rune.old", 'r') as f:
        for line in f:
                #print [gemprim.runeToPrime(dmanip.sepStr(i, 3)) for i in line.split("•")]
                if line[:2] == "||" or line[:2] == "//":
                        #raw += "\n\n"
                        continue
                raw += line

rawPages = raw.split("\n\n")

# List of pages
pages = []
for page in rawPages:
        page = page
        curPage = []
        for word in page.split("•"):
                primeWord = []
                for letter in dmanip.sepStr(word, 3):
                        primeWord.append(gemprim.runeToPrime([letter])[0])
                curPage.append(primeWord)
        pages.append(curPage)

# Cast to indexes
pages = [[gemprim.primeToInt(word) for word in page] for page in pages]

tryDecrypt(25, 3, 14, 3)

sys.exit()
 
# Brute force it
pltxtDetails = []

for ipage in range(25,26):#len(pages)):
        page = pages[ipage]
        bruteOut("Page " + str(ipage))
        for ikey in range(len(rkeys.allKeys)):
                key = rkeys.allKeys[ikey]
                bruteOut("> Key " + str(key[:5]))
                for shift in range(29):
                        bruteOut(">> Shift " + str(shift))
                        for iappl in range(len(rappls.allAppls)):
                                appl = rappls.allAppls[iappl]
                                bruteOut(">>> Application " + str(iappl))

                                # For every page, key, shift, and application:
                                plainPage = []
                                count = 0
                                for word in page:
                                        plainWord = []
                                        for char in word:
                                                plainWord.append(appl(char, key[count%len(key)], shift))
                                                count += 1
                                        plainPage.append(plainWord)
                                
                                # Got potential plaintext!
                                dets = [ipage, ikey, shift, iappl, getEng(plainPage)]
                                if dets[4] > 0.4:
                                        print dets
                                pltxtDetails.append(dets)




pltxtDetails = sorted(pltxtDetails, key=operator.itemgetter(4))

with open("../data/bruterunes_findings.txt", 'w') as f:
        for det in pltxtDetails:
                f.write(str(det))

# Print 5 best results:

print ""
for det in pltxtDetails[-5:]:
        print det
        tryDecrypt(det[0], det[1], det[2], det[3])
        print ""

# Possible applications:
# 3301-n (and variations)

# Numbers from runes:
# Primes
# Index
# From IRC: Sets of aetts??
# Combinations

# Applied to:
# Pages
# Whole book
